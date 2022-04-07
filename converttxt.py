import packages

try:
  import unicodedata
  import re
  import os
  from unidecode import unidecode
  from PIL import Image#Open the text file which you have to convert into handwriting
  import cv2
  import numpy as np
except:
  packages.run()

import removebg
import measureletters
removebg.run()
measureletters.run()

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def writeletter(letter,upperl,gap,ht):
  try:
    if upperl and letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      filename="sem fundo/upper{}.png".format(str(ord(letter)))
    else:
      filename="sem fundo/{}.png".format(str(ord(letter)))
    cases = Image.open(filename)
  except:
    print("\n42 MISSING")
    print(letter,str(ord(letter)),filename)
    quit()
  else:
    BG.paste(cases, (gap, ht))

with open("sizeletters.txt",'r') as arquivo:
    sizeletters=eval(arquivo.read())

def sylsplit(word):
    #print(word)
    vogals='aãáàâeéèêiíìîoóòõôuAÁÀÃÂEÉÈÊIÍÌÎOÓÒÕÔU'
    syllables=[]
    if len(word)<3 or word==word.upper():
        syllables.append(word)
    else:
        j=0
        for i in range(len(word)-2):
            a=word[i]
            b=word[i+1]
            c=word[i+2]
            ab=a+b
            bc=b+c
            if unidecode(b)==unidecode(c) and b in vogals: #CVV
                syllables.append(word[j:i+2])
                j=i+2
            elif bc=='rr' or bc=='ss' or bc=='sc' or bc=='sç' or bc=='xc': #VCC
                syllables.append(word[j:i+2])
                j=i+2
            elif bc=='ch' or bc=='lh' or bc=='nh' or bc=='qu' or bc=='gu':
                syllables.append(word[j:i+1])
                j=i+1
            elif a in vogals and b not in vogals and c not in vogals: #VCC
                if not c in 'rlh':
                    syllables.append(word[j:i+2])
                    j=i+2
                else:
                    syllables.append(word[j:i+1])
                    j=i+1
            elif a in vogals and c in vogals and b not in vogals:
                syllables.append(word[j:i+1])
                j=i+1
            elif a in vogals and b in vogals and c in vogals and not a=='u':
                syllables.append(word[j:i+2])
                j=i+2
            if i>=len(word)-3 and not ''.join(syllables)==word:
                syllables.append(word[j:])
    if '' in syllables:
        syllables.remove('')
    #print(syllables)
    return syllables

txt="3. O primeiro processo parcial, a carboxilação de biotina, supõe-se que leve duas fases, a primeira das quais é a ativação do bicarbonato por ATP para produzir um intermediário de carboxi-fosfato. O 1'-nitrogênio da biotina covalentemente ligado é posteriormente carboxilado, seja diretamente com carboxifosfato ou, mais comumente, via descarboxilação do intermediário para criar CO2, que então funciona como agente carboxilante. O aceptor do grupo carboxil é a forma enol da biotina, que tem um 1'-nitrogênio nucleofílico consideravelmente maior do que a forma keto. A carboxilação (transcarboxilação), a segunda reação parcial, parece ocorrer de forma gradual, com etapas de transferência de prótons flanqueando a etapa de transferência do núcleo carboxil entre a carboxilbiotina e a forma de enol de piruvato."# path of your text file#path of page(background)photo (I have used blank page)
txt=txt.replace('.','. ')
txt=txt.replace('  ',' ')
from PIL import Image
BG=Image.open("bg.png") 
sizehyp=sizeletters["{}.png".format(str(ord('-')))]
sheet_width=BG.width
gap, ht = 0, 0
end=False
last=''
for word in txt.split():
    upperl=False
    if word==word.upper() and len(word)>1:
      upperl=True
    if '-' in word:
        ws=[]
        words=word.split('-')
        for w in words:
            ws.extend(sylsplit(w))
            if not w==words[-1]:
                ws.append('-')
        syllables=ws
        #print(ws)
    else:
        syllables=sylsplit(word)
    for syl in syllables:
        #print(syl, last)
        end=False
        sizesyl=[]
        for letter in syl:
            try:
                sizeletters["{}.png".format(str(ord(letter)))]
            except:
                print("\n 125 MISSING")
                print(letter,str(ord(letter)))
                quit()
            else:
                sizesyl.append(sizeletters["{}.png".format(str(ord(letter)))])
        if syl==syllables[-1]:
            newgap=gap+sum(sizesyl)
        else:
            newgap=gap+sum(sizesyl)+sizehyp
        if sheet_width < newgap:
            #print(True)
            if end==False and (last.isalpha() or last.isnumeric()):
                try:
                    cases = Image.open("sem fundo/{}.png".format(str(ord('-'))))
                except:
                    print("\n 140 MISSING")
                    print(letter,str(ord(letter)))
                    quit()
                else:
                    BG.paste(cases, (gap, ht))
                    last='hypen'
                    gap+=sizeletters['{}.png'.format(str(ord('-')))]-2
            gap,ht=0,ht+130
            if gap==0 and last=='-':
              writeletter('-',False)
              last=letter
            for letter in syl:
              writeletter(letter,upperl,gap,ht)
              last=letter
              gap+=sizeletters['{}.png'.format(str(ord(letter)))]-2
        else:
            for letter in syl:
              writeletter(letter,upperl,gap,ht)
              last=letter
              gap+=sizeletters['{}.png'.format(str(ord(letter)))]-2
    end=True
    writeletter(' ',False,gap,ht)
    last=' '
    gap+=sizeletters['{}.png'.format(str(ord(' ')))]-2
BG.show()
BG.save("{}.png".format(slugify(' '.join(txt.split(' ')[0:6]))))