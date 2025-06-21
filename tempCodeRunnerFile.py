import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, jsonify
from utils.extractors import ContentExtractor
from core.semantic_processor import SemanticProcessor
from core.metadata_generator import MetadataGenerator
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

extractor = ContentExtractor()
processor = SemanticProcessor()
generator = MetadataGenerator()

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed. Supported: PDF, DOCX, TXT, PNG, JPG"}), 400
    
    try:
        file_id = str(uuid.uuid4())
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{file_id}.{file_ext}")
        file.save(file_path)
        content = extractor.extract_text(file_path, file_ext)
        semantic_data = processor.analyze_content(content[:10000])
        file_info = {
            'name': file.filename,
            'type': file_ext,
            'size': os.path.getsize(file_path)
        }
        metadata = generator.generate_metadata(file_info, semantic_data)
        os.remove(file_path)
        return jsonify(metadata)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
