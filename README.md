

   AutoMetalysis:
                  ![Screenshot 2025-06-21 220200](https://github.com/user-attachments/assets/7f0abdaf-7a0d-4da9-bcb2-792c97901dbe)

  The Semantic Document Analyzer is a Flask-based web application designed for automated extraction and analysis of semantic information from documents in formats such as PDF, DOCX, TXT, PPTX, and images. It leverages advanced NLP models to provide summaries, keywords, topics, named entities, readability, sentiment analysis, and visualizations.

  Key Features

Multi-format Support: Handles PDFs, Word/PowerPoint files, text, and images.
Content Extraction: Retrieves text from documents and images (using OCR).
Semantic Analysis: Generates summaries, keywords (KeyBERT), topics (LDA), and named entities (spaCy).
Readability & Sentiment: Calculates Flesch Reading Ease and sentiment scores.
Visualizations: Produces word clouds and keyword bar plots.
Page-wise Analysis: For PDFs, each page is analyzed individually.
REST API: Offers endpoints for easy integration.

System Architecture

ContentExtractor: Extracts text from uploaded files.
SemanticProcessor: Performs all NLP tasks and visualization.
MetadataGenerator: Adds file info and processing metrics.
Flask Web App: Manages uploads, processing, and API responses.

Implementation Highlights
        ![image](https://github.com/user-attachments/assets/f10dd7c0-02ef-4057-bea6-7d16659647b7)


Built with Python and Flask.
Utilizes transformers, KeyBERT, spaCy, TextBlob, textstat, scikit-learn, matplotlib, and wordcloud.
Dynamic parameter handling in topic modeling prevents errors with small datasets.
Robust error handling and user feedback.

Usage
Run the app:(before load all python libraries like 

    python app.py

Upload files via the web interface or use the /upload API endpoint.
Receive JSON output with all extracted features and base64-encoded visualizations.

Results

Returns summaries, keywords, topics, named entities, readability, sentiment, and visualizations.
Handles both single and multi-page documents reliably.
            ![Screenshot 2025-06-21 220700](https://github.com/user-attachments/assets/8834e862-1c6b-4967-b185-5875a41b46d6)
            ![Screenshot 2025-06-21 220730](https://github.com/user-attachments/assets/331d8726-785f-42fc-8e02-50430dc4db20)
            ![Screenshot 2025-06-21 220744](https://github.com/user-attachments/assets/764dfcbd-b540-4c2f-9401-4e0636931f90)


