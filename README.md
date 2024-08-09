# Audio Converter

This project is a simple web-based application that allows users to upload audio files and convert them to different formats such as WAV, MP3, and OGG.

audio-converter/
│
├── app.py # Main application file
├── templates/
│ └── index.html # HTML template
├── static/
│ └── styles.css # CSS file for styling
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Features

- Upload audio files in various formats.
- Convert uploaded audio files to WAV, MP3, or OGG formats.
- Simple and intuitive web interface.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Jinja2**: A templating engine for Python used within Flask.
- **HTML/CSS**: For creating the frontend of the web application.

## Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Flask (install using `pip install Flask`)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/audio-converter.git
    ```
2. Navigate to the project directory:
    ```bash
    cd audio-converter
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    python app.py
    ```
5. Open your web browser and go to `http://localhost:5000`.

## Usage

1. Upload an audio file by clicking on the "Choose File" button.
2. Select the desired output format (WAV, MP3, OGG) from the dropdown menu.
3. Click on the "Convert" button.
4. Download the converted file.

## Project Structure

