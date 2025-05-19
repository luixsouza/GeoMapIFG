import os

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
TOKEN_URL = 'https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token'
PROCESS_URL = 'https://sh.dataspace.copernicus.eu/api/v1/process'

TAR_FILE = 'retrieved_files.tar'
EXTRACT_PATH = 'retrieved_files'
TIF_FILE = os.path.join(EXTRACT_PATH, 'default.tif')
JSON_FILE = 'ndvi_statistics.json'