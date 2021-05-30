import zipfile

with zipfile.ZipFile('offline-gmaven-stable.zip', 'r') as zip_ref:
    zip_ref.extractall('./')