import pygetwindow as gw
import cv2
import numpy as np
from d3dshot import D3DShot
import asyncio
import websockets
import json
import threading

# Get the Chrome window and broadcast the content using OpenCV
bounding_boxes = []


async def handle_websocket():
    async with websockets.serve(handle_connection, "localhost", 8080):
        print("WebSocket server started on ws://localhost:8080")
        await asyncio.Future()  # Run forever


# Define the handler for incoming WebSocket connections
async def handle_connection(websocket, path):
    global bounding_boxes
    print("Client connected")
    try:
        async for message in websocket:
            # Parse the incoming JSON data (which is a list of element info)
            elements_data = json.loads(message)

            # Ensure it's a list and iterate over each element's data
            if isinstance(elements_data, list):
                for data in elements_data:
                    xpath = data.get("xpath")
                    x = data.get("x")
                    y = data.get("y")
                    width = data.get("width")
                    height = data.get("height")

                    # Remove existing bounding box with the same xpath
                    bounding_boxes = [box for box in bounding_boxes if box[0] != xpath]

                    # Add the new bounding box
                    if xpath and x is not None and y is not None and width and height:
                        bounding_boxes.append((xpath, int(x), int(y), int(width), int(height)))

                # print("Received element info:", elements_data)
            else:
                print("Unexpected data format received.")
    except websockets.exceptions.ConnectionClosed as e:
        print("Connection closed", e)


# Get the Chrome window and broadcast the content using OpenCV
def broadcast_chrome_content():
    # Get the Chrome window
    chrome_windows = [window for window in gw.getWindowsWithTitle('Chrome') if 'Chrome' in window.title]
    toolbar_height = 100  # Adjust this value as needed based on your system

    if not chrome_windows:
        print("No Chrome window found.")
        return

    chrome_window = chrome_windows[0]

    # Get the window's bounding box
    left, top, right, bottom = chrome_window.left, chrome_window.top + toolbar_height, chrome_window.right, chrome_window.bottom

    # Initialize D3DShot to capture the specified region
    d3d = D3DShot()

    # Start WebSocket server in a separate thread
    ws_thread = threading.Thread(target=lambda: asyncio.run(handle_websocket()))
    ws_thread.daemon = True
    ws_thread.start()

    while True:
        # Capture a frame using D3DShot
        frame = d3d.screenshot(region=(left, top, right, bottom))
        frame = np.array(frame)

        # Draw bounding boxes on the frame
        for (_, x, y, w, h) in bounding_boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame in an OpenCV window
        cv2.imshow("Chrome Content Broadcast", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the OpenCV window
    cv2.destroyAllWindows()


if __name__ == "__main__":
    broadcast_chrome_content()