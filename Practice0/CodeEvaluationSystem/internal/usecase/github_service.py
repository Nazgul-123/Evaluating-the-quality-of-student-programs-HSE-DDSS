import requests
import os

file_name = "GithubAccessToken"
file_path = os.path.join(os.path.dirname(__file__), file_name)

# Чтение токена из файла
try:
    with open(file_path, 'r') as file:
        token = file.readline().strip()  # Читаем первую строку и убираем лишние пробелы
        print("Токен успешно прочитан:", token)
except FileNotFoundError:
    print("Файл не найден. Проверьте путь к файлу.")
except Exception as e:
    print("Произошла ошибка при чтении файла:", e)

# Замените эти переменные на свои значения
GITHUB_TOKEN = token
REPO_OWNER = 'Nazgul-123'
REPO_NAME = 'CSharp-LabWorks-HSE-Perm'

# Заголовки для авторизации
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json',
}

# Получаем список форков
forks_url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/forks'

def get_forks() -> list:
    """
    Получает список форков репозитория с GitHub.
    :return: Список форков или None в случае ошибки.
    """

    try:
        # Выполняем GET-запрос
        response = requests.get(forks_url, headers=headers)

        # Проверяем статус ответа
        if response.status_code == 200:
            forks = response.json()
            print(f"Успешно получено {len(forks)} форков.")
            return forks
        else:
            print(f'Ошибка при получении форков: {response.status_code} - {response.text}')
            return None

    except Exception as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")
        return None


def clone_forks(forks: list) -> None:
    """
    Клонирует форки репозитория в локальную файловую систему.

    :param forks: Список форков.
    """
    if not forks:
        print("Нет форков для клонирования.")
        return

    for fork in forks:
        fork_owner = fork['owner']['login']
        fork_repo_name = fork['name']
        clone_url = fork['clone_url']

        print(f'Клонирование форка: {fork_owner}/{fork_repo_name}')
        os.system(f'git clone {clone_url} {fork_repo_name}')
