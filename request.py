import requests
import json

# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# print(response.status_code)
# print(response.text)

# if response.status_code == 200:
#     print("успешно")
# else:
#     print("Ошибка")

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "my post",
    "body": "my body",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.json())

# response = requests.get(url)
# data = response.json()

# print(f'title: {data["title"]}')
# print(f'body: {data["body"]}')

# print(json.dumps(data, indent=4))

# for post in data[:5]:
#     print(post["title"])

