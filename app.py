from flask import Flask, request, jsonify
import os

# Create the Flask app
app = Flask(__name__)

# Folder to save uploaded files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Set the maximum upload size to 60GB (optional)
app.config['MAX_CONTENT_LENGTH'] = 60 * 1024 * 1024 * 1024  # 60GB

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is included in the request
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'message': 'No file selected'}), 400

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({'message': f'File {file.filename} uploaded successfully!', 'path': file_path})

if __name__ == '__main__':
    app.run(debug=True)

