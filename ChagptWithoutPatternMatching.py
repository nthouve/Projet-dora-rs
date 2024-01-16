from openai import OpenAI
import os

os.environ["OPENAI_API_KEY"] = "mykey"

def ask_gpt(commande, file):
  # Ouvrir le fichier en mode lecture ('r' pour read)
  with open(file, 'r') as fichier:
      # Lire tout le contenu du fichier dans une variable
      contenu = fichier.read()

  client = OpenAI()

  Prompt = "this is a python code :\n" + contenu + "\n" + commande + "Format your response by: Showing the whole modified code"


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

def save_as(content, path):
  #use at the end of replace_2 as save_as(end_result, "file_path")
  with open(path, 'w') as file:
    file.write(content)
  print("file saved !")

ask = ask_gpt("Change les symboles des joueurs dans ce jeu de morpion", "openFile.py")
save_as(extract_command(ask)[0], "openFile.py")
