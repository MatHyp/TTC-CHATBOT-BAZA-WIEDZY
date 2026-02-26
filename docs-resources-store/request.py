import requests
import json

# # Konfiguracja
URL = "https://api.ttc.ovh/v1/generate"
API_KEY = "" 

# def ask_llm(prompt):
#     payload = {
#         "prompt": f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
#         "max_tokens": 200,
#         "temperature": 0.7
#     }
    
#     headers = {
#         "X-API-Key": API_KEY,
#         "Content-Type": "application/json"
#     }

#     print(f"🤔 Pytam model: {prompt}")
    
#     try:
#         response = requests.post(URL, json=payload, headers=headers)
#         response.raise_for_status() 
        
#         result = response.json()
#         print("\n🤖 Odpowiedź modelu:")
#         print(result["response"])
        
#     except requests.exceptions.HTTPError as err:
#         print(f"❌ Błąd HTTP: {err.response.status_code} - {err.response.text}")
#     except Exception as e:
#         print(f"❌ Wystąpił błąd: {e}")

# if __name__ == "__main__":
#     pytanie = "Dlaczego Warszawa jest ciekawym miastem? Napisz w 3 punktach."
#     ask_llm(pytanie)

payload = {
    "prompt": "Jakie jest najwieksze miasto w Polsce?",
    "max_tokens": 200,
    "temperature": 0.2
}

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}



response = requests.post(URL,json=payload ,headers=headers)

result = response.json()

print("\nOdpowiedź modelu:")
print(result)
        