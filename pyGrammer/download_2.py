# -*- coding : utf-8 -*-
# @Author   :   stone
# @Github   :   https://github.com/stonedada
import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True,verify=False)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True,verify=False)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

if __name__ == "__main__":
    # file_id = 'TAKE ID FROM SHAREABLE LINK'
    file_id='1pB25UcE2nL5ZOuOaoAxTFHf1D3rbnH3f'
    # destination = 'DESTINATION FILE ON YOUR DISK'
    destination='./data_downloaded/mouse_brain_downloaded.zip'
    download_file_from_google_drive(file_id, destination)
    print("downloaded")