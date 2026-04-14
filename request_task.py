import requests
url = "https://jsonplaceholder.typicode.com/posts"

def menu():
    print("1.получить post")
    print("2.получить все post")
    print("3.создать post")
    print("4.выйти")

def get_post(post_id):
    response = requests.get(f"{url}/{post_id}")
    print(response.json())