from fastembed import ImageEmbedding
import time
from typing import List
from qdrant_client import QdrantClient
from config import QDRANT_URL, QDRANT_API_KEY, EMBEDDINGS_MODEL

class ImageSearcher:
    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self.qdrant_client = QdrantClient(
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            prefer_grpc=True,
        )
        self.model = ImageEmbedding(model_name=EMBEDDINGS_MODEL)
    
    def search(self, query_image_path: str, top: int = 5) -> List[dict]:
        start_time = time.time()
        hits = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=next(self.model.embed(query_image_path)).tolist(),
            limit=top
        )
        print(f"Search took {time.time() - start_time:.2f} seconds")
        
        return [hit.payload for hit in hits]