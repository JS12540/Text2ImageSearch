from embed import ImageEmbedder
from pathlib import Path
import chromadb
from qdrant_client import QdrantClient
from qdrant_client.http import models
import uuid
from qdrant_client.http.models import PointStruct

# https://docs.trychroma.com/getting-started

# chroma_client = chromadb.PersistentClient(path="./data") #(host='localhost', port=50051)

client = QdrantClient(
    url="https://f9d44fbb-cb67-4370-b88b-586479eecd68.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="G0pElefNG9sKURZMmQ9-gHUw_TXna9cP69WoX_aaQbiGYSnXBrR2lA",
)

# Get image paths
image_folder = "./images"
image_files = list(Path(image_folder).rglob('*'))
image_files = [file for file in image_files if file.suffix in {'.jpeg', '.jpg', '.png'}]  # adapt this if you have different image formats

# Embedder
embedder = ImageEmbedder()

# collection = chroma_client.get_or_create_collection(name="image_collection") # (dimension=512, metric='Cosine')
collection = client.recreate_collection( collection_name="image-collection",
    vectors_config=models.VectorParams(size=512 , distance=models.Distance.COSINE))


points = []

# Add vectors to the collection
for i, image_file in enumerate(image_files):
    
    embedding = embedder([
        image_file
    ])[0]

    print(embedding)

    point_id = str(uuid.uuid4())
    points.append(PointStruct(id=point_id,payload={"uri": str(image_file), "document" : [str(image_file)]},vector=embedding, ))

    print("Points added")
    # client.upsert(
    #     embeddings=embedding,
    #     metadatas=[{"uri": str(image_file)}],
    #     documents=[str(image_file)],
    #     ids=[f"{i}"],
    # )

print(points[0])

# Putting up the points on vector store
client.upsert(
    collection_name="image-collection",
    wait=True,
    points=points
)

# print(collection.count())