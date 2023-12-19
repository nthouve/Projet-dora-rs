from openai import OpenAI

import os

# Replace "your_actual_api_key" with your OpenAI API key
os.environ["OPENAI_API_KEY"] = "mykey"
# Ouvrir le fichier en mode lecture ('r' pour read)
with open('openFile.py', 'r') as fichier:
    # Lire tout le contenu du fichier dans une variable
    contenu = fichier.read()

commande = "Affiche les 20 premiers nombres au lieu des 10 premiers"

client = OpenAI()
#Prompt = "J'ai un fichier python que je veux modifier légèrement pour respecter la commande que je t'ai envoyé, envoie moi le code python en entier que tu auras modifié afin de respecter la commande. Ce que tu me renvoies doit pouvoir être copier collé directement dans un fichier python et ainsi prêt à l'utilisation. Voici le fichier python dont je parle :\n" + contenu + "\nRenvoies le moi avec ces modifications"+"Voici la commande dont je parle : " + commande
Prompt = "Voici un fichier python :\n" + contenu + "\nModifie le pour respecter la condition suivante :\n" + commande + "\nRenvoie le fichier en entier"
print(Prompt)
response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=Prompt
)

print(response.choices[0].text)

