import requests
url = "https://jsonplaceholder.typicode.com/posts"

def menu():
    print("1.получить post")
    print("2.получить все post")
    print("3.создать post")
    print("4.выйти")

def get_post(post_id):
    try:
        response = requests.get(f"{url}/{post_id}")
        if response.status_code == 200:
            print(response.json())
        else:
            print("пост не найден")
    except Exception as e:
        print(f"ошибка {e}")


def all_posts():
    try:
        response = requests.get(url)
        posts = response.json()
        for i in posts [:10]:
            print(i["title"])
    except Exception as e:
        print(f"ошибка {e}")

def create_post():
    try:
        title = input("введите title: ")
        body = input("введите Body: ")
        data = {
        "title": title,
        "body": body,
        "userId": 1
        }
        response = requests.post(url, json=data)
        print(f"создан {response.json}")
    except Exception as e:
        print(f"ошибка {e}")

def main():
    while True:
        menu()
        try:
            num = int(input("Введите цифру команды: "))
            if num == 1:
                post_id = input("введите id: ")
                get_post(post_id)
            elif num == 2:
                all_posts()
            elif num == 3:
                create_post()
            elif num == 4:
                break
            else:
                print("неверный выбор")
        except ValueError:
            print("Введите число а не букву")

if __name__ == "__main__":
    main()   
