import requests

text = "besok ku bunuh kau"

resp = requests.post("https://model-ml-7vvpza7dfa-et.a.run.app", data={'sentence': text}) #ganti url sama yang API ML Model

json_response = resp.json()
prediction = json_response.get('prediction')

print(json_response)