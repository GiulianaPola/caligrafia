import unicodedata
import re

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

import os
import removebg
import measureletters
import packages

packages.run()
removebg.run()
measureletters.run()

with open("sizeletters.txt",'r') as arquivo:
    sizeletters=eval(arquivo.read())

from unidecode import unidecode
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

#Importing Library
from PIL import Image#Open the text file which you have to convert into handwriting
txt="3. O primeiro processo parcial, a carboxilação de biotina, supõe-se que leve duas fases, a primeira das quais é a ativação do bicarbonato por ATP para produzir um intermediário de carboxi-fosfato. O 1'-nitrogênio da biotina covalentemente ligado é posteriormente carboxilado, seja diretamente com carboxifosfato ou, mais comumente, via descarboxilação do intermediário para criar CO2, que então funciona como agente carboxilante.O aceptor do grupo carboxil é a forma enol da biotina, que tem um 1'-nitrogênio nucleofílico consideravelmente maior do que a forma keto. A carboxilação (transcarboxilação), a segunda reação parcial, parece ocorrer de forma gradual, com etapas de transferência de prótons flanqueando a etapa de transferência do núcleo carboxil entre a carboxilbiotina e a forma de enol de piruvato."# path of your text file#path of page(background)photo (I have used blank page)
BG=Image.open("bg.png") 
sizehyp=sizeletters["{}.png".format(str(ord('-')))]
sheet_width=BG.width
gap, ht = 0, 0
end=False
last=''
for word in txt.split():
    upper=False
    if word==word.upper():
      upper=True
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
                print("\nMISSING 103")
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
                    print("\nMISSING 109")
                    print(letter,str(ord(letter)))
                    quit()
                else:
                    BG.paste(cases, (gap, ht))
                    size = cases.width
                    height=cases.height
                    last='hypen'
                    gap+=size-2
            gap,ht=0,ht+130
            if gap==0 and last=='-':
                try:
                    cases = Image.open("sem fundo/{}.png".format(str(ord('-'))))
                except:
                    print("\nMISSING 123")
                    print(letter,str(ord(letter)))
                    quit()
                else:
                    BG.paste(cases, (gap, ht))
                    size = cases.width
                    height=cases.height
                    last='-'
                    gap+=size-2
            for letter in syl:
                try:
                    cases = Image.open("sem fundo/{}.png".format(str(ord(letter))))
                except:
                    print("\nMISSING 136")
                    print(letter,str(ord(letter)))
                    quit()
                else:
                    BG.paste(cases, (gap, ht))
                    size = cases.width
                    height=cases.height
                    last=letter
                    gap+=size-2 
        else:
            for letter in syl:
                try:
                    cases = Image.open("sem fundo/{}.png".format(str(ord(letter))))
                except:
                    print("\nMISSING 150")
                    print(letter,str(ord(letter)))
                    quit()
                else:
                    BG.paste(cases, (gap, ht))
                    size = cases.width
                    height=cases.height
                    #print(size)
                    gap+=size-2
                    last=letter
    end=True
    try:
        cases = Image.open("sem fundo/{}.png".format(str(ord(' '))))
    except:
        print("\nMISSING 164")
        print(' ',str(ord(' ')))
        quit()
    else:
        BG.paste(cases, (gap, ht))
        size = cases.width
        height=cases.height
        last=' '
        gap+=size-2
BG.show()
BG.save("{}.png".format(slugify(' '.join(txt.split(' ')[0:6]))))