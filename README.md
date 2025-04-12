
<h1 align="center">Image to Pencil Sketch </h1>
<h3 align="center">Python & JavaScript</h1>
<div align="center">
	<img src="/image-sketch-app/images/final.png">
</div>


## Background.
This project transforms any standard RGB image into a pencil sketch using Python's OpenCV library. 
It was originally designed as an assignment for the LGM Data Science Virtual Internship but has been expanded into a full-fledged web application with Flask.

## Folder Structure
<div align="center">
	<img src="/image-sketch-app/images/filestructure.png">
</div>

## Software & Dependencies
- Prerequisites
  - Python 3.7+
  - pip (Python package manager)
  
## Required Libraries
- Install dependencies using (bash):
  - pip install -r requirements.txt

## The conversion process.
- Grayscale conversion
- Image inversion (negative effect)
- Gaussian blurring
- Blending techniques to create the final sketch effect

## Backend Python File (app.py) Overview
This Flask-based server handles the image upload, processing, and sketch conversion for the web application. Key functionalities:

- Flask Configuration
  - Sets up upload folder (static/uploads) with a 16MB file size limit.
  - Uses secure_filename to sanitize uploaded filenames.

- Core Functions
  - image_to_base64(): Converts OpenCV images to base64 for web display.
  - convert_to_sketch(): Implements the 5-step pencil sketch algorithm:
    - Grayscale conversion → Inversion → Gaussian blur → Re-inversion → Blending.

- API Endpoints
  - /: Serves the HTML interface (index.html).
  - /convert: Accepts image uploads, processes them, and returns JSON with:
    - Base64-encoded intermediate steps (grayscale, inverted, blurred).
    - Final pencil sketch result.
    - Error handling for invalid uploads.

- Cleanup
- Automatically deletes uploaded files after processing to save space.
- Execution
  - Runs in debug mode for development (app.run(debug=True)).
- Dependencies: Flask (web framework), OpenCV (image processing), NumPy (array operations).
- Role: Acts as the bridge between the user-facing UI and the OpenCV sketch algorithm, ensuring secure and efficient image processing.

## Download & Execution (git bash)
- Clone the Repository
  - git clone https://github.com/Walgama123/image-sketch-app.git
  - cd image-sketch-app
- Install Dependencies
  - pip install -r requirements.txt
- Run the Flask App
  - python app.py
- Open in Browser
  - http://localhost:5000
- Upload & Convert!
  - Click "Select Image" to upload a photo.
  - Click "Convert" to generate the pencil sketch.
  - Click "Download Sketch" to save the result.

## Requirements File (requirements.txt)
<div align="center">
	<img src="/image-sketch-app/images/Requirment.png">
</div>

## Future Improvements
  - Multiple sketch styles (charcoal, watercolor)
  - Batch processing (convert multiple images at once)
  - User accounts to save sketches
  
## Credits
- OpenCV for image processing
- Flask for the web backend
- LGMVIP for the original project idea


