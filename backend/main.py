import chromadb
from embed import LanguageEmbedder
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from qdrant_client import QdrantClient

# chroma_client = chromadb.PersistentClient(path="./data")
# collection = chroma_client.get_collection("image_collection")
lang_embedder = LanguageEmbedder()

client = QdrantClient(
    url="https://f9d44fbb-cb67-4370-b88b-586479eecd68.us-east4-0.gcp.cloud.qdrant.io:6333", 
    api_key="G0pElefNG9sKURZMmQ9-gHUw_TXna9cP69WoX_aaQbiGYSnXBrR2lA",
)

client.get_collection("image-collection")

app = FastAPI()

origins = ["http://localhost", "http://localhost:8080", "http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/images", StaticFiles(directory="images/"), name="images")


@app.get("/")
async def root(query: str | None = None):
    if query:
        query_embedding = lang_embedder([query])

        search_result = client.search(collection_name= "image-collection", query_vector=query_embedding, limit =3)

        # return {
        #     "result": collection.query(
        #         query_embeddings=[query_embedding],
        #         n_results=3,
        #         ## This needs to be improved:
        #         # where={"metadata_field": "is_equal_to_this"},
        #         # where_document={"$contains":"search_string"}
        #     )
        # }

        return {
            "result" : search_result
        }
    else:
        return {}


def test():
    chroma_client = chromadb.PersistentClient(path="./data")
    collection = chroma_client.get_collection("image_collection")
    print("First 5 items from collection:")
    print(collection.peek())