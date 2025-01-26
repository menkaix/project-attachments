from flask import Flask, render_template, request, send_from_directory # Import render_template and send_from_directory
from flask_headers import headers
from flask_cors import CORS

import os
from services.file_service import serve_file
from services.google_cloud_storage_service import upload_file_to_gcs  # Import the upload function

app = Flask(__name__, static_folder='./resources')  # Specify static folder  (important!)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html template

# Serve static files from the React app's build directory
@app.route('/<path:path>')
def serve_static(path):
    return serve_file(app.static_folder, path)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    bucket_name = request.form.get('bucket_name')
    destination_blob_name = request.form.get('destination_blob_name', file.filename)

    if not bucket_name:
        return 'Bucket name is required', 400

    upload_file_to_gcs(bucket_name, file.stream, destination_blob_name)

    return 'File successfully uploaded', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('FLASK_PORT', 5000), debug=os.environ.get('FLASK_DEBUG', True))
