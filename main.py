from flask import Flask, request, send_file, render_template_string
from pydub import AudioSegment
import os
import tempfile

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template_string('''
        <!doctype html>
        <title>Audio Converter</title>
        <h1 style="color: blue; text-align: center; font-size: 24px;">Upload an audio file to convert</h1>
        <form method=post enctype=multipart/form-data action="/convert" style="text-align: center;">
          <input type=file name=file>
          <select name="format">
            <option value="wav">WAV</option>
            <option value="mp3">MP3</option>
            <option value="ogg">OGG</option>
          </select>
          <input type=submit value=Convert>
        </form>
    ''')


# Convert route
@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    format = request.form['format']

    # Create a temporary file to save the uploaded file
    with tempfile.NamedTemporaryFile(delete=False) as temp_input_file:
        file.save(temp_input_file.name)
        temp_input_file_path = temp_input_file.name

    # Set the output file path and format
    temp_output_file_path = f"{tempfile.mktemp()}.{format}"

    # Convert the audio file
    audio = AudioSegment.from_file(temp_input_file_path)
    audio.export(temp_output_file_path, format=format)

    # Send the converted file to the user
    return send_file(temp_output_file_path, as_attachment=True, download_name=f"converted.{format}")

if __name__ == "__main__":
    app.run(debug=True)
