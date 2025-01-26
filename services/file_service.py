
import os
from flask import send_from_directory

def serve_file(static_folder, path):
    if path != "" and os.path.exists(static_folder + '/' + path):
        return send_from_directory(static_folder, path)
    else:
        return send_from_directory(static_folder, 'index.html')