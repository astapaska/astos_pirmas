import requests
data = requests.get("https://www.assorti.lt/")
print(data.text)