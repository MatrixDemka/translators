import requests
import json
from pprint import pp


word = "red"
ya_token = "dict.1.1.20241016T152324Z.3a8754097cfb6bdf.92b7c310f5f3015b4f28474957f0873a7e8e0390"
translate_word = []
url = f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={ya_token}&lang=en-ru&text={word}"

response = requests.get(url)
data = json.loads(response.text)
for i in data["def"]:
    for res in i["tr"]:
        translate_word.append(res["text"])
return translate_word