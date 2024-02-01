# Text2ImageSearch

# System Architecture Overview

This system is designed to facilitate semantic search for car images based on user queries. It utilizes the CLIP (Contrastive Language-Image Pretraining) model to generate embeddings for both text and images, enabling efficient similarity search.

## Backend Components

### 1. Embed.py
- **Description**: Contains classes responsible for generating embeddings for images and text using the CLIPProcessor.
- **Functionality**: Utilizes the CLIPProcessor to encode images and text into embeddings.

### 2. Scrape_images.py
- **Description**: A script responsible for scraping images of cars from DuckDuckGo search engine and storing them in the images directory.
- **Functionality**: Automates the process of fetching images from DuckDuckGo and saving them locally for further processing.

### 3. Vectorize.py
- **Description**: Creates embeddings for the scraped images and stores them in the image collection.
- **Functionality**: Utilizes Embed.py to generate embeddings for images scraped by Scrape_images.py and stores them for later retrieval.

### 4. Main.py
- **Description**: Serves as the main API endpoint.
- **Functionality**: Accepts user queries, performs vector search using the generated embeddings, and returns up to 3 relevant results from the image collection.

## Frontend

- **Description**: A simple frontend interface for users to input queries and view semantic search results.
- **Functionality**: Accepts user queries, sends them to the backend API (Main.py), and displays the retrieved search results in a user-friendly manner.

# Setup and Run Instructions

### 1. Installation
In a location where you want to place this repo, use the following commands:

    git clone https://github.com/JS12540/Text2ImageSearch.git

## Backend Setup:

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Create necessary directories:
   ```
   mkdir data
   mkdir images
   ```

5. Deactivate the virtual environment:
   ```
   deactivate
   ```

## Frontend Setup:

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Ensure Node.js version 21.5.0 is being used:
   ```
   nvm use 21.5.0
   ```

3. Install dependencies:
   ```
   npm install
   ```

## Running the Application:

### Backend:

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

3. Run the FastAPI server using Uvicorn:
   ```
   uvicorn main:app --reload
   ```

4. To run the vectorize.py script to store embeddings in qdrant:
   ```
   python vectorize.py
   ```

5. Deactivate the virtual environment:
   ```
   deactivate
   ```

### Frontend:

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Start the frontend server:
   ```
   npm start
   ```
