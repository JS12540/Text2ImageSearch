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
