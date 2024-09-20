# Image Search API

This project implements an image search API using FastAPI and Qdrant for vector similarity search. It allows users to upload an image and find similar images from a pre-indexed collection.

## Features

- Image similarity search using vector embeddings
- FastAPI backend for handling image upload and search requests
- Integration with Qdrant for efficient vector similarity search
- CORS middleware for cross-origin requests
- Static file serving for frontend assets

## Prerequisites

- Python 3.11+
- Docker (optional, for containerization)

## Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
The project uses environment variables for configuration. You can set these in a `.env` file or directly in your environment:
```
QDRANT_URL=http://localhost:6333/
QDRANT_API_KEY=your_api_key
COLLECTION_NAME=nocnoc
EMBEDDINGS_MODEL=Qdrant/clip-ViT-B-32-vision
```

## Usage
1. Start the FastAPI server:
```bash
python main.py
```

2. The API will be available at `http://localhost:8000`.

3. To search for similar images, send a POST request to `/image/search` with the image file in the request body.

## API Endpoints

- `POST /image/search`: Upload an image to search for similar images in the collection.

## Docker Support

A Dockerfile is provided for containerization. To build and run the Docker image:
```bash
docker build -t image-search-api .
docker run -p 8000:8000 image-search-api
```

## Project Structure

- `main.py`: FastAPI application and main entry point
- `config.py`: Configuration settings and environment variables
- `image_searcher.py`: Image search functionality using Qdrant
- `requirements.txt`: Python dependencies
- `Dockerfile`: Docker configuration for containerization
- `static/`: Directory for static frontend assets (if applicable)

## Data Processing

The project includes a Jupyter notebook (`image_search_processing.ipynb`) for data preprocessing and indexing. This notebook demonstrates how to:

1. Load and preprocess image data
2. Generate image embeddings using a pre-trained model
3. Index the embeddings in Qdrant for efficient similarity search

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Specify your license here]




