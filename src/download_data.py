import os
import requests

from constants.roboflow import DATASET_URL 

print("Dowloading data...")
files = requests.get(DATASET_URL)
open('./data.zip', 'wb').write(files.content)
print("Download concluded!")



