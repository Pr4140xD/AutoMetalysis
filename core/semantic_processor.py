from transformers import pipeline
from keybert import KeyBERT
import spacy

class SemanticProcessor:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.kw_model = KeyBERT()
        self.ner = spacy.load("en_core_web_sm")
    
    def analyze_content(self, text):
        try:
            # Summarization
            summary = self.summarizer(
                text, 
                max_length=150, 
                min_length=40, 
                do_sample=False
            )[0]['summary_text']
            
            # Keyword extraction
            keywords = self.kw_model.extract_keywords(
                text, 
                keyphrase_ngram_range=(1, 2),
                stop_words='english',
                top_n=8
            )
            
            # Entity recognition
            doc = self.ner(text)
            entities = {ent.label_: ent.text for ent in doc.ents}
            
            return {
                "summary": summary,
                "keywords": [kw[0] for kw in keywords],
                "entities": entities
            }
        except Exception as e:
            return {
                "summary": "Analysis failed",
                "keywords": [],
                "entities": {}
            }
