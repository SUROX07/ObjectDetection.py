# Person Detection System

The Person Detection System is a Python-based application that detects when a person is in front of the camera. The project leverages the OpenCV2 library for real-time person detection. The system includes a frontend for user interaction and a backend server to handle requests and execute the detection program. It was built using:

- **Python** and **OpenCV2** for the detection logic.
- **HTML**, **CSS**, and **JavaScript** for the frontend interface.
- **Flask** for the backend server.

---

## Project Structure

### **1. `program/`**
- **Description:** Contains the core program for the Person Detection System.
- **Files:**
  - `camera.py`: The main Python script responsible for detecting the presence of a person using OpenCV2.

### **2. `frontend/`**
- **Description:** Contains the website code, providing a user interface to view project details and run the detection system.
- **Key Features:**
  - The `index.html` file serves as the entry point for the website.
  - Navigate to the "Trial" section in the website to trigger the main detection program.
- **Technologies Used:**
  - HTML, CSS, and JavaScript.

### **3. `backend/`**
- **Description:** Contains the backend server code written in Python using Flask.
- **Functionality:**
  - Handles requests from the frontend.
  - Executes the main detection program (`camera.py`) when the user clicks the "Trial" button on the frontend.

---

## How to Run the Project

### Prerequisites
- Python 3.x
- Flask library
- OpenCV2 library
- A web browser for the frontend

### Steps
1. Clone the repository.
2. Install the required Python libraries:
   ```bash
   pip install flask opencv-python
   ```
3. Navigate to the `backend/` directory and start the Flask server:
   ```bash
   python app.py
   ```
4. Open the `frontend/index.html` file in a web browser.
5. Navigate to the "Trial" section and click the button to run the detection program.

---

## Acknowledgments
- OpenCV community for providing robust computer vision tools.
- Flask for its lightweight and efficient web framework.
