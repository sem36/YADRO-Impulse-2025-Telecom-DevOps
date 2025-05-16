import requests
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Список тестовых кодов статуса для проверки
status_codes = [200, 301, 100, 404, 500]

# Функция обработки ответа
def process_response(code):
    url = f"https://httpstat.us/{code}"
    try:
        response = requests.get(url)
        status = response.status_code

        if 100 <= status < 400:
            logging.info(f"Response from {url}: Status {status}, Body: {response.text.strip()}")
        elif 400 <= status < 600:
            raise Exception(f"Error response from {url}: Status {status}, Body: {response.text.strip()}")
        else:
            logging.warning(f"Unhandled status code: {status}")
    except Exception as e:
        logging.error(f"Exception occurred: {e}")

# Основной блок выполнения
if __name__ == "__main__":
    for code in status_codes:
        process_response(code)
