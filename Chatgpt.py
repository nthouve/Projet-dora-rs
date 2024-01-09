from openai import OpenAI
import dora
import pyarrow as pa
import inspect
import numpy as np
import pandas as pd
import pylcs
import textwrap
import sys
import time

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

def strip_indentation(code_block):
    # Use textwrap.dedent to strip common leading whitespace
    dedented_code = textwrap.dedent(code_block)

    return dedented_code


def replace_code_with_indentation(original_code, replacement_code):
    # Split the original code into lines
    lines = original_code.splitlines()

    # Preserve the indentation of the first line
    indentation = lines[0][: len(lines[0]) - len(lines[0].lstrip())]

    # Create a new list of lines with the replacement code and preserved indentation
    new_code_lines = indentation + replacement_code

    return new_code_lines

def replace_2(nom_fichier, commande_chatGPT):
      
  with open(nom_fichier, 'r') as fichier:
    content = fichier.read()

  commande = extract_command(commande_chatGPT)
  ligne_a_modifier = commande[0]
  ligne_modifiee = commande[1]
  replacement = strip_indentation(ligne_modifiee.replace("```python\n", "").replace("\n```", "").replace("\n", ""))
  int_result=replace_code_with_indentation(ligne_a_modifier, replacement)
  end_result = content.replace(ligne_a_modifier, int_result)
  return end_result

print(replace_2("openFile.py", ask_gpt("Change les symboles du jeu du morpion",'openFile.py')))
