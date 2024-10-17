import requests
import json
from pprint import pp


url = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"
token = "dict.1.1.20241016T152324Z.3a8754097cfb6bdf.92b7c310f5f3015b4f28474957f0873a7e8e0390"

def translate_word(word):
    trans_word = []
    params = {
        "key": token,
        "lang": "ru-en",
        "text": word,
        "ui": "ru"
    }

    response = requests.get(url=url, params=params)
    data = json.loads(response.text)

    for i in data["def"]:
        for res in i["tr"]:
            trans_word.append(res["text"])
    trans_word = trans_word[0]
    return trans_word


if __name__ == "__main__":
    word = "машина"
    assert translate_word(word) == "car"
