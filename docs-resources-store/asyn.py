# 20 requests to check api 
import asyncio
import httpx
import time


URL = "https://api.ttc.ovh/v1/generate"
API_KEY = ""
L_ZAPYTAN = 20

# Treść pytania
PYTANIE = "Jakie jest największe miasto w Polsce?"

payload_template = {
    "prompt": f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{PYTANIE}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
    "max_tokens": 50,
    "temperature": 0.2
}

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

async def send_request(client, user_id):
    start_time = time.perf_counter()
    try:
        data = payload_template.copy()
        
        response = await client.post(URL, json=data, headers=headers, timeout=120.0)
        end_time = time.perf_counter()
        duration = end_time - start_time
        
        if response.status_code == 200:
            result = response.json()
            ai_text = result.get("response", "Brak pola 'response'")
            
            clean_text = ai_text.replace(data["prompt"], "").strip()
            
            print(f"✅ Użytkownik {user_id:02d} ({duration:.2f}s):")
            print(f"   🤖: {clean_text}\n")
        else:
            print(f"❌ Użytkownik {user_id:02d}: Błąd {response.status_code} - {response.text}\n")
            
    except Exception as e:
        print(f"🔥 Użytkownik {user_id:02d}: Wyjątek: {e}\n")

async def run_simulation():
    print(f"🚀 Rozpoczynam symulację: {L_ZAPYTAN} równoległych zapytań...\n")
    start_total = time.perf_counter()
    
    async with httpx.AsyncClient() as client:
        tasks = [send_request(client, i) for i in range(1, L_ZAPYTAN + 1)]
        await asyncio.gather(*tasks)
    
    end_total = time.perf_counter()
    print(f"--- SYMULACJA ZAKOŃCZONA ---")
    print(f"Całkowity czas: {end_total - start_total:.2f}s")
    print(f"Średni czas oczekiwania: {(end_total - start_total) / L_ZAPYTAN:.2f}s")

if __name__ == "__main__":
    asyncio.run(run_simulation())