from pprint import pprint
import requests


class yandex_disk:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        '''Создаем заголовки для авторизации'''
        headers = {'Content-Type': 'application/json', 'Authorization': f"OAuth {self.token}"}
        return headers

    def get_files_list(self):
        '''Получаем список файлов на Я.Диск в json'''
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files/'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_href_upload(self, yadisk_file_path):
        '''получаем ссылку для загрудки на Я.Диск'''
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload/"
        headers = self.get_headers()
        parameters = {'path': yadisk_file_path, 'overwrite': 'True'}
        response = requests.get(upload_url, headers=headers, params=parameters)
        return response.json()

    def upload(self, yadisk_file_path, filename):
        '''Метод загружает выбранный файлы на Я.Диск'''
        href = self._get_href_upload(yadisk_file_path=yadisk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print(f"Код:201 - Файл {file_name} загружен!")

    def makedir(self, yadisk_file_path):
        '''Метод создает папку указанную для загрузки файла'''
        headers = self.get_headers()
        href = self._get_href_upload(yadisk_file_path=yadisk_file_path).get("href", "")
        response = requests.put(f'https://cloud-api.yandex.net/v1/disk/resources?path={new_dir}', headers=headers)
        if response.status_code == 201:
            print(f"Код:201 - Папка {new_dir} создана!")
        elif response.status_code == 409:
            print(f"Код:409 - Папка {new_dir} уже существует!")
        else:
            response.raise_for_status()


    def filepath(self, new_dir, file_name):
        '''Метод собирает путь загрузки файла на я.диск (зачем ему надо с именем файла - я не понял)'''
        filepath = new_dir + file_name  # путь файла на Я.Диске.
        return filepath


if __name__ == '__main__':
    user_token = 'token'  # введите токен Я.Диска
    user = yandex_disk(token=user_token)
    new_dir = '/new folder/'  # введите в какую папку загрузить (папка может не существовать!)
    file_name = 'test.txt'  # введите имя файла.
    file_path = user.filepath(new_dir, file_name)

    user.makedir(new_dir)
    # user.upload(file_path, file_name)
    # pprint(user.get_files_list())