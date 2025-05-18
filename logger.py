import requests
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s',handlers=[logging.StreamHandler(sys.stdout)])

status_codes = [200, 301, 100, 404, 500]

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

if __name__ == "__main__":
    try:
        for code in status_codes:
            process_response(code)
        exit(0)
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        exit(1) 
