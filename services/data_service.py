import logging
from config import PROCESS_URL, TAR_FILE

def request_data(oauth, request_payload):
    try:
        response = oauth.post(PROCESS_URL, json=request_payload, headers={"Accept": "application/tar"})
        if response.status_code == 200:
            with open(TAR_FILE, "wb") as f:
                f.write(response.content)
            logging.info("Data successfully retrieved.")
            return True
        else:
            logging.error("Request failed: %s - %s", response.status_code, response.text)
            return False
    except Exception as e:
        logging.error("Error requesting data: %s", e)
        return False