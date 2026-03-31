import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
from sentence_transformers import SentenceTransformer

# Embedding class
class BGEM3EmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-m3")

    def __call__(self, input: Documents) -> Embeddings:
        embeddings = self.model.encode(input)
        return embeddings.tolist()

# Search vector db
def retrival_search(prompt):
    client = chromadb.PersistentClient(path="../school_vector_db") 

    collection = client.get_collection(
        name="school_documents", 
        embedding_function=BGEM3EmbeddingFunction()
    )

    results = collection.query(
        query_texts=[prompt],
        n_results=3
    )

    return results['documents'][0]
