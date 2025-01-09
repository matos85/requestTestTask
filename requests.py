import requests

# URL для запроса
url = "https://dev.whatcrm.net/v3/tariffs?currency=RUB&crm=lk"

# Заголовки запроса
headers = {
    "X-Whatsapp-Token": "5d8af8faaeb61680883a850be0c577e2"
}

# Выполнение GET-запроса
response = requests.get(url, headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    # Парсинг JSON-ответа
    json_result = response.json()
    print(json_result)
else:
    print(f"Ошибка: {response.status_code}, {response.text}")
