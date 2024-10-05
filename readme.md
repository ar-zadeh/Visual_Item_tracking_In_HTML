# XPath Tracker Repository

This repository contains tools for tracking and monitoring HTML elements on web pages using XPath. It consists of two main components: a Tampermonkey script for collecting XPaths and a Python script for visualizing the tracked elements.

## Prerequisites

- Google Chrome browser
- Tampermonkey extension for Chrome
- Python 3.x
- Required Python libraries: `pygetwindow`, `opencv-python`, `numpy`, `d3dshot`, `websockets`

## Installation

1. Install the Tampermonkey extension for Google Chrome.
2. Clone this repository or download the files to your local machine.
3. Install the required Python libraries:
   ```
   pip install pygetwindow opencv-python numpy d3dshot websockets
   ```

## Usage

### Step 1: Collect XPaths

1. Open Tampermonkey in Chrome and create a new script.
2. Copy and paste the content of `Xpath_download_tampermonkey.txt` into the new Tampermonkey script.
3. Save the script and enable it.
4. Navigate to the web page you want to track.
5. Click the blue selection button that appears in the top-left corner of the page to enter selection mode.
6. Click on the elements you want to track. Their XPaths will be collected.
7. When finished, click the green download button to save the collected XPaths as a JSON file.

### Step 2: Set Up Bounding Box Tracker

1. Open Tampermonkey and create another new script.
2. Copy and paste the content of `bounding_box_reporter_tampermonkey.txt` into this new script.
3. In the script, locate the `xpathsToTrack` array and replace its content with the XPaths you collected in Step 1.
4. Save the script but keep it disabled for now.

### Step 3: Disable XPath Collector and Enable Bounding Box Tracker

1. In Tampermonkey, disable the script from Step 1 (XPath collector).
2. Enable the script from Step 2 (Bounding box tracker).

### Step 4: Run the Python Script

1. Open a terminal or command prompt.
2. Navigate to the directory containing the Python script.
3. Run the Python script:
   ```
   python bounding_box_tracker.py
   ```

### Step 5: Track Elements

1. Refresh the web page you want to track.
2. The Python script will open a window showing the Chrome browser content with green bounding boxes around the tracked elements.
3. The script will continuously update the positions of the tracked elements.

## Files in the Repository

- `Xpath_download_tampermonkey.txt`: Tampermonkey script for collecting XPaths.
- `bounding_box_reporter_tampermonkey.txt`: Tampermonkey script for reporting element positions.
- `bounding_box_tracker.py`: Python script for visualizing tracked elements.
- `README.md`: This file, containing instructions and information about the project.

## Troubleshooting

- If the bounding boxes are not appearing, ensure that the XPaths in the Tampermonkey script match those of the elements you want to track.
- Make sure the WebSocket server URL in both the Tampermonkey script and Python script match (default is `ws://localhost:8080`).
- If the Python script fails to capture the Chrome window, adjust the `toolbar_height` variable in the script.

## Contributing

Contributions to improve the scripts or extend functionality are welcome. Please submit a pull request or open an issue to discuss proposed changes.


 
 #   V i s u a l _ I t e m _ t r a c k i n g _ I n _ H T M L 
 
 
