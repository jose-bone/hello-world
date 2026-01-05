# %%
import requests
import json
from tqdm import tqdm

import pandas as pd

ceps = [
    "01519000",
    "01310930",
    "20040002",
    "30140071",
    "70040900",
    "80010000",
    "60020020",
    "50020000",
    "65020010",
    "19060100",
    "58038200",
]

url = "https://viacep.com.br/ws/{ceps}/json/"
datas = []
for cep in tqdm(ceps):
    getResponse = requests.get(url.format(ceps=cep))
    if getResponse.status_code == 200:
        datas.append(getResponse.json())

datas

# %%
dataset = pd.DataFrame(datas)
dataset.to_csv("ceps.csv", sep=";")

# %%
with open("ceps.json", "w", encoding="UTF-8") as open_file:
    json.dump(datas, open_file, ensure_ascii=False, indent=4)