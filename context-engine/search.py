import chromadb
from chromadb.utils import embedding_functions

# ==========================================
# 1. PODŁĄCZENIE DO ISTNIEJĄCEJ BAZY
# ==========================================
print("Podłączanie do lokalnej bazy ChromaDB...")
chroma_client = chromadb.PersistentClient(path="./medical_db")

# MUSISZ użyć dokładnie tego samego modelu do wyszukiwania, 
# którego użyliśmy wcześniej do zapisywania danych!
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Pobieramy naszą kolekcję z bazy
collection = chroma_client.get_collection(
    name="medical_knowledge",
    embedding_function=embedding_function
)

print(f"Baza podłączona! Liczba dokumentów w bazie: {collection.count()}\n")

# ==========================================
# 2. WYSZUKIWANIE (PROMPT UŻYTKOWNIKA)
# ==========================================
# Tutaj wpisujesz medyczne zapytanie (np. objawy)
user_query = "I have a lot of sinus pain, green runny nose, sinus pain when I tilt my head forward" 
# Uwaga: Ten dataset z HF jest prawdopodobnie po angielsku, więc pytamy po angielsku!

print(f"🔍 Szukam informacji dla zapytania: '{user_query}'...\n")

# Przeszukujemy bazę
results = collection.query(
    query_texts=[user_query],
    n_results=3  # Pobieramy 3 najbardziej trafne dokumenty (Top-K)
)

# ==========================================
# 3. WYŚWIETLANIE WYNIKÓW
# ==========================================
print("-" * 50)
# ChromaDB zwraca listy w listach, dlatego używamy indeksu [0]
for i in range(len(results['documents'][0])):
    tekst = results['documents'][0][i]
    metadane = results['metadatas'][0][i]
    dystans = results['distances'][0][i]
    
    print(f"📄 WYNIK NR {i+1}")
    print(f"Źródło: {metadane.get('source')} | Kategoria: {metadane.get('category')}")
    print(f"Dopasowanie (Dystans): {dystans:.4f} (Im mniej, tym lepiej!)")
    print(f"Tekst: {tekst}")
    print("-" * 50)