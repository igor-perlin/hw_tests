import requests
import unittest

class YandexDiskAPITest(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.token = "token"  # Замените на свой токен Яндекс Диска
        self.headers = {'Authorization': f'OAuth {self.token}'}
        self.folder_name = "TestFolder"

    def test_create_folder_success(self):
        url = f"{self.base_url}/resources"
        params = {'path': self.folder_name}
        response = requests.put(url, headers=self.headers, params=params)

        self.assertEqual(response.status_code, 201)  # Проверка кода ответа
        self.assertIn(self.folder_name, response.json().get('path'))  # Проверка создания папки в списке файлов

    # Пример отрицательного теста на попытку создания папки, которая уже существует

    def test_create_folder_already_exists(self):
        url = f"{self.base_url}/resources"
        params = {'path': self.folder_name}
        response = requests.put(url, headers=self.headers, params=params)

        self.assertEqual(response.status_code, 409)  # Проверка кода ответа
        self.assertEqual(response.json().get('message'), 'Resource already exists')  # Проверка сообщения об ошибке

if __name__ == '__main__':
    unittest.main()
