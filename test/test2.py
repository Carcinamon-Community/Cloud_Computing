import requests

url = "URL_ENDPOINT_CLOUD_FUNCTION"  # Ganti dengan URL endpoint Cloud Function Anda

data = {
    "sentence": "Ini adalah contoh kalimat"
}

response = requests.post(url, json=data)
print(response.text)