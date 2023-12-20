from openai import OpenAI

import os

# Replace "your_actual_api_key" with your OpenAI API key
os.environ["OPENAI_API_KEY"] = "mykey"
def ask_gpt(commande, file):
  # Ouvrir le fichier en mode lecture ('r' pour read)
  with open(file, 'r') as fichier:
      # Lire tout le contenu du fichier dans une variable
      contenu = fichier.read()

  client = OpenAI()

  Prompt = "this is a python code :\n" + contenu + "\n" + commande + "Format your response by:\n1. first showing the block to replace to replace\n2. Showing the modified code"


  response = client.chat.completions.create(
    model="gpt-4",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": Prompt}
    ]
  )

  print(response.choices[0].message.content)

ask_gpt("Change the O signs by F signs in the tic tac toe game please",'openFile.py')
