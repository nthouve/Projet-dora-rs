from openai import OpenAI

import os

# Replace "your_actual_api_key" with your OpenAI API key
os.environ["OPENAI_API_KEY"] = "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"

def ask_gpt(commande, file):
  # Ouvrir le fichier en mode lecture ('r' pour read)
  with open(file, 'r') as fichier:
      # Lire tout le contenu du fichier dans une variable
      contenu = fichier.read()

  client = OpenAI()

  Prompt = "this is a python code :\n" + contenu + "\n" + commande + "Format your response by:\n1. first showing the block to replace to replace\n2. Showing the modified block of code"


  response = client.chat.completions.create(
    model="gpt-4-1106-preview",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": Prompt}
    ]
  )

  answer = response.choices[0].message.content
  return answer

def extract_command(gptCommand):
      
  blocks = []
  temp = ""
  writing = False

  for line in gptCommand.splitlines():
    if line == "```" : 
      writing = False
      blocks.append(temp)
      temp = ""

    if writing :
      temp += line
      temp+="\n"

    if line == "```python" : 
      writing = True

  return blocks

#print(ask_gpt("Change les symboles du jeu du morpion",'openFile.py'))
