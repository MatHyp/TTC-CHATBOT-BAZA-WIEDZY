# 🩺 TTC Chatbot Doctor

> **Projekt tworzony w ramach Koła Sztucznej Inteligencji w Technikum Technologii Cyfrowych (TTC) w Szczecinie** 🚀

**TTC Chatbot Doctor** medyczny asystent diagnostyczny oparty na architekturze **RAG (Retrieval-Augmented Generation)**.  

---

## 🎯 Cel Projektu

Celem projektu jest stworzenie **aplikacji medycznej**, składającej się z następujących elementów:

1. **Web Panel (Frontend)**  
   Przyjazny interfejs użytkownika, w którym pacjent może opisać swoje objawy oraz otrzymać odpowiedź w formie czatu.

2. **Silnik Kontekstowy (Context Engine)**  
   Moduł wyszukujący najbardziej trafne artykuły medyczne i wytyczne kliniczne w **zamkniętej bazie wektorowej (ChromaDB)**.

3. **Prywatne API AI (LLM API)**  
   Serwer zarządzający lokalnym modelem językowym, który:
   - korzysta wyłącznie z dostarczonego kontekstu,
   - generuje **bezpieczne i merytoryczne odpowiedzi**,
   - minimalizuje ryzyko halucynacji.

---

## 🏗️ Architektura Systemu (RAG Pipeline)

Poniższy diagram przedstawia pełen **przepływ danych (Data Flow)** — od momentu wpisania objawów przez użytkownika, aż do wygenerowania odpowiedzi przez model LLM.

```mermaid
graph TD
    A[👨‍⚕️ Użytkownik / Web Panel] -->|1. Wpisuje objawy| B(🧠 API)
    B -->|2. Zapytanie wektorowe| C(🔍 Context Engine - Serwis Wyszukiwania)
    C -->|3. Wyszukiwanie semantyczne| D[(📚 ChromaDB - Medyczna Baza Wiedzy)]
    D -->|4. Artykuły i wytyczne| C
    C -->|5. Oczyszczony kontekst medyczny| B
    B -->|6. Prompt: Pytanie + Kontekst| E[🤖 Lokalny Model LLM]
    E -->|7. Bezpieczna odpowiedź| B
    B -->|8. Odpowiedź asystenta| A

    classDef frontend fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff;
    classDef backend fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#fff;
    classDef db fill:#f1c40f,stroke:#f39c12,stroke-width:2px,color:#fff;
    classDef llm fill:#9b59b6,stroke:#8e44ad,stroke-width:2px,color:#fff;

    class A frontend;
    class B,C backend;
    class D db;
    class E llm;
```

## 📂 Struktura Repozytorium
Obecna struktura repo (w trakcie):
```
.
├── frontend/
│   └── Web Panel (interfejs czatu dla użytkownika)
│
├── llm-api/
│   └── Lokalny model LLM wystawiony jako API (FastAPI)
│
├── context-engine/
│   └── Silnik wyszukiwania kontekstu (Retrieval + Embeddings)
│
├── docs/
│   └── Storage na pliki tymczasowe, pomocnicze  
│
└── README.md
```
