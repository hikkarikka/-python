import requests


class APIClient:
    def __init__(self, url):
        self.url = url

# def get(self, endpoint):
#     try:
#         response = requests.get(f"{self.url}/{endpoint}")
#         if response.status_code == 200:
#             print(response.json())
#         else:
#             print("пост не найден")
#     except Exception as e:
#         print(f"ошибка {e}")

    def get(self, url):
        try:
            response = requests.get(f"{self.url}/{endpoint}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'ошибка GET: {e}')
            return None
            

class PostService:
    pass
class App:
    pass





if __name__ == "__main__":
    app = App()
    app.run()
