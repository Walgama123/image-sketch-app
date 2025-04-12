document.addEventListener('DOMContentLoaded', function() {
    const selectBtn = document.getElementById('selectBtn');
    const convertBtn = document.getElementById('convertBtn');
    const downloadBtn = document.getElementById('downloadBtn');
    const imageUpload = document.getElementById('imageUpload');
    
    const originalImage = document.getElementById('originalImage');
    const grayImage = document.getElementById('grayImage');
    const invertedImage = document.getElementById('invertedImage');
    const blurredImage = document.getElementById('blurredImage');
    const invertedBlurredImage = document.getElementById('invertedBlurredImage');
    const sketchResult = document.getElementById('sketchResult');
    
    let selectedFile = null;
    
    // Select image button click
    selectBtn.addEventListener('click', function() {
        imageUpload.click();
    });
    
    // Handle file selection
    imageUpload.addEventListener('change', function(e) {
        if (e.target.files && e.target.files[0]) {
            selectedFile = e.target.files[0];
            const reader = new FileReader();
            
            reader.onload = function(event) {
                originalImage.src = event.target.result;
                
                // Clear previous results
                grayImage.src = '#';
                invertedImage.src = '#';
                blurredImage.src = '#';
                invertedBlurredImage.src = '#';
                sketchResult.src = '#';
            };
            
            reader.readAsDataURL(selectedFile);
        }
    });
    
    // Convert button click
    convertBtn.addEventListener('click', function() {
        if (!selectedFile) {
            alert('Please select an image first');
            return;
        }
        
        const formData = new FormData();
        formData.append('image', selectedFile);
        
        // Show loading state
        convertBtn.disabled = true;
        convertBtn.textContent = 'Processing...';
        
        fetch('/convert', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                grayImage.src = data.gray_image;
                invertedImage.src = data.inverted_image;
                blurredImage.src = data.blurred_image;
                invertedBlurredImage.src = data.inverted_blurred_image;
                sketchResult.src = data.sketch_result;
            } else {
                alert('Error: ' + data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred during conversion');
        })
        .finally(() => {
            convertBtn.disabled = false;
            convertBtn.textContent = 'Convert';
        });
    });
    
    // Download button click
    downloadBtn.addEventListener('click', function() {
        if (!sketchResult.src || sketchResult.src === '#') {
            alert('Please convert an image first');
            return;
        }
        
        const link = document.createElement('a');
        link.href = sketchResult.src;
        link.download = 'pencil_sketch.png';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });
});