from datetime import datetime
import hashlib

class MetadataGenerator:
    def generate_metadata(self, file_info, semantic_data):
        return {
            "document_id": self._generate_id(file_info['name']),
            "original_filename": file_info['name'],
            "file_type": file_info['type'],
            "file_size_bytes": file_info['size'],
            "processing_date": datetime.utcnow().isoformat() + "Z",
            "content_summary": semantic_data['summary'],
            "key_phrases": semantic_data['keywords'],
            "identified_entities": semantic_data['entities'],
            "system_version": "1.0.2"
        }
    
    def _generate_id(self, filename):
        return hashlib.sha256(filename.encode()).hexdigest()[:16]
