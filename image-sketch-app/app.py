from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def image_to_base64(image):
    """Convert OpenCV image to base64 string"""
    _, buffer = cv2.imencode('.png', image)
    return base64.b64encode(buffer).decode('utf-8')

def convert_to_sketch(image_path):
    """Convert image to pencil sketch with intermediate steps"""
    # Read the original image
    original_image = cv2.imread(image_path)
    
    # Step 1: Convert to grayscale
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    
    # Step 2: Invert the grayscale image
    inverted_gray_image = 255 - gray_image
    
    # Step 3: Apply Gaussian blur to the inverted image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    
    # Step 4: Invert the blurred image back
    inverted_blurred_image = 255 - blurred_image
    
    # Step 5: Create the pencil sketch effect
    pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    
    # Convert all images to base64 for web display
    return {
        'gray_image': 'data:image/png;base64,' + image_to_base64(gray_image),
        'inverted_image': 'data:image/png;base64,' + image_to_base64(inverted_gray_image),
        'blurred_image': 'data:image/png;base64,' + image_to_base64(blurred_image),
        'inverted_blurred_image': 'data:image/png;base64,' + image_to_base64(inverted_blurred_image),
        'sketch_result': 'data:image/png;base64,' + image_to_base64(pencil_sketch)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'image' not in request.files:
        return jsonify({'success': False, 'error': 'No image uploaded'})
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'})
    
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            result = convert_to_sketch(filepath)
            return jsonify({'success': True, **result})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
        finally:
            # Clean up uploaded file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    return jsonify({'success': False, 'error': 'Unknown error'})

if __name__ == '__main__':
    app.run(debug=True)