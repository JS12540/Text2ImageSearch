from embed import LanguageEmbedder
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from qdrant_client import QdrantClient

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
    """
    Retrieves search results based on a given query string.

    Parameters:
        query (str | None): The query string to search for. Defaults to None.

    Returns:
        dict: A dictionary containing the search results. If a query is provided, the dictionary will have a "result" key with the search results. If no query is provided, an empty dictionary is returned.
    """
    if query:
        query_embedding = lang_embedder([query])

        search_result = client.search(collection_name= "image-collection", query_vector=query_embedding, limit =3)

        return {
            "result" : search_result
        }
    else:
        return {}
