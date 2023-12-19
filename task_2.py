import requests

token = input('введите ваш токен: ')

class Ya_disc:
    base_url = 'https://cloud-api.yandex.net'
    # ya_token = input('input your ya.disc_oauth_token: ')
    # folder_name = input('input folder name for upload image\images:')

    def __init__(self):
        self.token = f'OAuth {token}'
    def create_folder(self, folder_name):
        headers = {'Authorization': self.token}
        params = {'path': folder_name}
        response = requests.put(f'{self.base_url}/v1/disk/resources', params=params, headers=headers)
        res = response.status_code
        if res == 409:
            print(f"папка c именем - {folder_name} уже существует")
            return res
        elif res == 201:
            print(f"папка с именем - {folder_name} успешно создана")
            return res

ya_disk = Ya_disc()
ya_disk.create_folder("mymymy")
