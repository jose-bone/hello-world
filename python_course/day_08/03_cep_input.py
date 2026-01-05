#%%
import requests

cep = input("Enter with a CEP:")

url = "https://viacep.com.br/ws/{cep}/json/"

getResponse = requests.get(url.format(cep=cep))

if getResponse.status_code == 200:
    print(getResponse.json())