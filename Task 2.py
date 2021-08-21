from pprint import pprint
import requests


class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    amount_of_files = int(input("Пожалуйста, введите количество фалов: "))
    files_list = []
    for i in range(amount_of_files):
        path_to_file = input("Введите путь к файлу: ")
        filename = input('Введите имя файла: ')
        files_list.append([path_to_file, filename])
    token = input("Введите свой токен: ")
    uploader = YaUploader(token)
    for path_to_file, filename in files_list:
        result = uploader.upload(disk_file_path=path_to_file, filename=filename)

