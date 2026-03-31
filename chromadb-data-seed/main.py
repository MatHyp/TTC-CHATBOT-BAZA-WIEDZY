import os
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
from sentence_transformers import SentenceTransformer
import glob

folder = 'folder'

# BGEM3EmbeddingFunction method 
class BGEM3EmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-m3")

    def __call__(self, input: Documents) -> Embeddings:
        embeddings = self.model.encode(input)
        return embeddings.tolist()


# load files 
def load_files(folder_path, chunk_size=1000, overlap=200):
    
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    pattern = os.path.join(folder_path, "*.txt")
    txt_files = glob.glob(pattern)
    
    if not txt_files:
        print(f"Warning: No .txt files found in folder {folder_path}")
        return [], [], []

    all_chunks = []
    all_metadata = []
    all_ids = []
    
    global_chunk_counter = 0

    for file_path in txt_files:
        file_name = os.path.basename(file_path)
        print(f"Processing file: {file_name}...")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        text = " ".join(text.split())
        text_length = len(text)
        start = 0

        while start < text_length:
            end = start + chunk_size
            chunk = text[start:end]
            
            all_chunks.append(chunk)
            
            all_metadata.append({"source": file_name}) 
            
            all_ids.append(f"id_{global_chunk_counter}")
            
            start += (chunk_size - overlap)
            global_chunk_counter += 1

    return all_chunks, all_metadata, all_ids


texts, metadata, ids = load_files(folder_path=folder, chunk_size=1000, overlap=200)

# Initialize chrome db

client = chromadb.PersistentClient(path="../school_vector_db")
collection = client.get_or_create_collection(
    name="school_documents",
    embedding_function=BGEM3EmbeddingFunction()
)

if not texts:
    print("No data to insert. Exiting.")
    exit()


# load 100 elements batch to db from [0] - [100] and so on
BATCH_SIZE = 100

for i in range(0, len(texts), BATCH_SIZE):
    
    batch_texts = texts[i : i + BATCH_SIZE]
    batch_metadata = metadata[i : i + BATCH_SIZE]
    batch_ids = ids[i : i + BATCH_SIZE]


    collection.upsert(
        documents=batch_texts,
        metadatas=batch_metadata,
        ids=batch_ids
    )

print("Database seeding completed successfully!")
