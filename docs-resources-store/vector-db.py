import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from huggingface_hub import hf_hub_download

print("Pobieranie pliku final_corpus.pkl z Hugging Face...")
file_path = hf_hub_download(
    repo_id="Sagarika-Singh-99/medical-rag-corpus", 
    repo_type="dataset", 
    filename="final_corpus.pkl"
)

df = pd.read_pickle(file_path)
print(f"Udało się! Cały zbiór ma {len(df)} dokumentów.")

# LIMIT DO TESTÓW, head bierze n dokumentów, df całość
df_subset = df.head(10000)
print(f"Do bazy wektorowej wrzucamy na razie {len(df_subset)} dokumentów w ramach testu.")

chroma_client = chromadb.PersistentClient(path="./medical_db")

embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = chroma_client.get_or_create_collection(
    name="medical_knowledge",
    embedding_function=embedding_function
)

documents = []
metadatas = []
ids = []

print("Przygotowywanie danych do wektoryzacji...")
for index, row in df_subset.iterrows():
    doc_id = str(row.get('doc_id', f"doc_{index}"))
    text_content = str(row.get('text', ''))
    
    metadata = {
        "title": str(row.get('title', 'Brak tytułu')),
        "source": str(row.get('source', 'Nieznane')),
        "category": str(row.get('category', 'Inne'))
    }
    
    if text_content.strip():
        ids.append(doc_id)
        documents.append(text_content)
        metadatas.append(metadata)

print(f"Rozpoczynam wektoryzację {len(documents)} dokumentów")

batch_size = 250
for i in range(0, len(ids), batch_size):
    print(f"Zapisuję partię {i} do {min(i + batch_size, len(ids))}...")
    collection.add(
        ids=ids[i : i + batch_size],
        documents=documents[i : i + batch_size],
        metadatas=metadatas[i : i + batch_size]
    )

print("✅ Gotowe! Twoja medyczna baza wektorowa RAG została pomyślnie zasilona danymi.")