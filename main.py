from flask import Flask, render_template, request, send_from_directory # Import render_template and send_from_directory
from flask_headers import headers
from flask_cors import CORS

import os
from services.file_service import serve_file


app = Flask(__name__, static_folder='./resources')  # Specify static folder  (important!)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html template


# Serve static files from the React app's build directory
@app.route('/<path:path>')
def serve_static(path):
    return serve_file(app.static_folder, path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('FLASK_PORT', 5000), debug=os.environ.get('FLASK_DEBUG', True))
