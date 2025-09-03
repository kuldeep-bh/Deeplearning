# Real-time Color Detection (OpenCV + Streamlit)

This is a small project where we use OpenCV and Streamlit to detect colors from your webcam in real-time.
You can choose to detect Red, Green, Blue, or All colors. The app will show the detected areas with bounding boxes and labels.

# What this project does
Opens your webcam in the browser using Streamlit
Lets you choose which color to detect (Red, Green, Blue, or All)
Cleans up noise so only real objects are detected
Draws a box and label around detected colors
# Setup Instructions
1. Clone or download this project
git clone https://github.com/your-username/color-detection-app.git
cd color-detection-app

2. Create a virtual environment (recommended)
python -m venv venv

3. Activate the environment
Windows (PowerShell)
.\venv\Scripts\Activate.ps1
Linux / Mac
source venv/bin/activate
4. Install the required packages
pip install -r requirements.txt
# How to Run
Run this command inside the project folder:
streamlit run app.py
Then open the link shown in the terminal (usually http://localhost:8501
# How to Use
Select the color you want to detect from the dropdown.
Click Start Camera.
The app will show live detection with bounding boxes.
Click Stop Camera to exit.
# Files in the project
app.py → Main Streamlit app
requirements.txt → List of dependencies
README.md → Instructions (this file)
# Example requirements.txt
opencv-python
numpy
streamlit
👨‍💻 Built with Python, OpenCV, and Streamlit.
