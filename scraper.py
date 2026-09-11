import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com/"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")
citas = soup.find_all("div", class_="quote")

datos = []
for cita in citas:
    frase = cita.find("span", class_="text").text.replace("“", "").replace("”", "")
    autor = cita.find("small", class_="author").text
    etiquetas = [tag.text for tag in cita.find_all("a", class_="tag")]
    
    datos.append({
        "frase": frase,
        "autor": autor,
        "etiquetas": ", ".join(etiquetas)
    })

df = pd.DataFrame(datos)
df.to_csv("dataset_citas.csv", index=False)
print("Scraping exitoso y archivo dataset_citas.csv creado.")
