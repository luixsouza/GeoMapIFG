import tarfile
import logging

def extract_tar_file(tar_path, extract_to):
    try:
        with tarfile.open(tar_path) as tar:
            tar.extractall(path=extract_to)
        logging.info("Files extracted to %s", extract_to)
    except Exception as e:
        logging.error("Error extracting TAR file: %s", e)
        raise

def save_to_json(data, json_file):
    import json
    try:
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info("Data saved to %s", json_file)
    except Exception as e:
        logging.error("Error saving JSON: %s", e)
        raise