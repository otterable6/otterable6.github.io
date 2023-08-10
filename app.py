import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'upload'  # Replace with the actual path on your server
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'uploadFile' not in request.files:
            return jsonify({'success': False, 'message': 'No file part'})

        file = request.files['uploadFile']

        if file.filename == '':
            return jsonify({'success': False, 'message': 'No selected file'})

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'success': True, 'message': 'File uploaded successfully'})

        return jsonify({'success': False, 'message': 'Error uploading file'})
    except Exception as e:
        return jsonify({'success': False, 'message': 'An error occurred'})

if __name__ == '__main__':
    app.run()
