# AI-Powered Visual and Voice Product Search

A modern e-commerce search engine that combines the power of visual recognition and voice commands. Upload product images to find visually similar items, or use voice commands in multiple languages (English, Arabic, and Amazigh) for a hands-free shopping experience. The application uses TensorFlow for image similarity detection and advanced speech recognition for accurate voice-to-text conversion, making product discovery more intuitive and accessible.

## Features

- **Multilingual Search**: Search products in multiple languages:
  - English
  - Arabic
  - Amazigh (Tamazight)
- **Image Similarity Search**: Find similar products based on image features
- **Speech-to-Text Integration**: Voice search capability
- **Pagination**: Organized product display with 12 items per page
- **Automatic Language Detection**: Automatically detects input language
- **Real-time Translation**: Translates search queries between supported languages

## Prerequisites

- Python 3.x
- Flask web framework
- TensorFlow for image processing
- Google Translate API
- SerpAPI for Tamazight translations

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [project-directory]
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root and add:
```
SERPAPI_KEY=your_serp_api_key
FLASK_SECRET_KEY=your_secret_key
```

## Project Structure

- `app.py`: Main Flask application with routing and core functionality
- `amazighTranslate.py`: Handles Amazigh (Tamazight) language translation
- `arabicTranslate.py`: Arabic language translation functionality
- `features.py`: Product feature extraction and processing
- `json_maker.py`: JSON data handling and formatting
- `static/`: Static files (JS, CSS, images)
- `templates/`: HTML templates
- `uploads/`: Directory for user-uploaded files

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open a web browser and navigate to:
```
http://localhost:5000
```

3. Use the search bar to search for products in any supported language
4. Upload images to find similar products
5. Use the voice search feature for hands-free searching

## API Endpoints

- `/`: Home page with search interface
- `/search`: Handles product search requests
- Additional endpoints for image processing and translation

## Dependencies

- Flask
- TensorFlow
- NumPy
- scikit-learn
- googletrans
- langdetect
- requests
- python-dotenv

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Translate API for translation services
- SerpAPI for Tamazight translation capabilities
- TensorFlow for image processing capabilities
