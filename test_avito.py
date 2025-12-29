import requests
import pytest
import random

BASE_URL = "https://qa-internship.avito.com"

# 1. Тест: Создание объявления
def test_create_item():
    seller_id = random.randint(111111, 999999)
    payload = {
        "sellerID": seller_id,
        "name": "Тестовый товар",
        "price": 1000,
        "description": "Описание тестового товара",
        "category_id": 1, # Добавлен ID категории
        "statistics": {
            "likes": 1,
            "contacts": 6,
            "viewCount": 1
        }
    }
    response = requests.post(f"{BASE_URL}/api/1/item", json=payload)
    print(response.json()) # Или print(response.text)
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    print(f"\nОбъявление создано для продавца {seller_id}")


# 2. Тест: Получение всех объявлений продавца
def test_get_seller_items():
    # ID 963791 для примера
    seller_id = 963791
    response = requests.get(f"{BASE_URL}/api/1/{seller_id}/item")
    assert response.status_code == 200
    assert isinstance(response.json(), list) # ответ = список
    print(f"\nПолучен список объявлений для продавца {seller_id}")

# 3. Тест: Получение объявления по ID 
def test_get_item_by_id():
    # Запрашиваем существующий айтем 
    item_id = "495c9daf-5692-496c-a7dc-5c49d27f072f" 
    response = requests.get(f"{BASE_URL}/api/1/item/{item_id}")
    print(response.json())
    assert response.status_code in [200, 404]

# 4. Тест: Получение статистики
def test_get_stats():
    item_id = "495c9daf-5692-496c-a7dc-5c49d27f072f"
    response = requests.get(f"{BASE_URL}/api/1/statistic/{item_id}")
    print(response.json())
    assert response.status_code == 200