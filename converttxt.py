txt="1. Variações no número de moléculas enzimáticas ou mudanças na atividade catalítica de cada molécula enzimática presente atualmente podem afetar o fluxo através de um processo catalisado por enzimas. Mudanças na concentração local de uma pequena molécula: um substrato da rota na qual essa reação é um passo, um produto do caminho, ou um metabólito ou cofator crítico que reflete o estado metabólico da célula, muitas vezes geram mudanças alostéricas muito rápidas na atividade enzimática. A regulação alostérica é mediada por segundos mensageiros produzidos intracelularmente em resposta a sinais extracelulares (1), em uma escala de tempo um pouco mais lenta ditada pelo ritmo do processo de transdução do sinal. Sinais hormonais ou neurais, assim como fatores de crescimento ou citocinas, são exemplos de sinais extracelulares. As taxas relativas de síntese e decomposição de uma enzima específica determinam a quantidade de moléculas dessa enzima em uma célula. A ativação de um fator de transcrição (2) em resposta a um sinal externo pode alterar a taxa de síntese. Os fatores de transcrição são proteínas nucleares que, quando ativadas, ligam determinado DNA ao promotor de um gene e ativam ou reprimem a transcrição desse gene, resultando no aumento ou redução da síntese da proteína codificada. A ativação de um fator de transcrição pode ocorrer como consequência de sua ligação a um ligante particular ou como resultado de sua fosforilação ou desfosforilação. A estabilidade dos RNAs mensageiros (3), ou sua resistência à destruição por ribonucleases celulares, varia, e a quantidade de mRNA em uma célula é em função de sua taxa de produção e de decomposição. A taxa na qual os ribossomos (4) transcrevem um mRNA em uma proteína é igualmente controlada, e é influenciada por uma série de variáveis. As taxas de decomposição da proteína (5) variam de acordo com a proteína e as circunstâncias na célula. A ligação covalente da ubiquitina a certas proteínas marca a sua decomposição em proteasomas. O sequestro da enzima e de seu substrato em compartimentos separados (6) é outra forma de alterar a atividade efetiva da enzima. Certas enzimas e sistemas enzimáticos são segregados dentro das células por compartimentos ligados por membranas, e o transporte do substrato através dessas membranas intracelulares pode ser o fator limitante na função enzimática. A concentração de seu substrato afeta todas as enzimas (7). Quando a concentração do substrato é menor que o Km, a atividade diminui e a taxa de reação se torna linearmente dependente da concentração do substrato. Um efetor alostérico (8) pode ou aumentar ou reduzir a atividade enzimática. A cinética hiperbólica é frequentemente convertida em cinética sigmóide por efetores alostéricos, e vice versa. Uma pequena alteração na concentração do substrato ou do efetor alostérico pode ter uma influência substancial na taxa de reação na seção mais íngreme da curva sigmóide. Em segundos ou minutos após um sinal regulatório, geralmente um sinal extracelular, ocorrem mudanças covalentes de enzimas ou outras proteínas (9). A fosforilação e a desfosforilação são de longe as mudanças mais prevalentes. A célula deve ser capaz de devolver a enzima alterada ao seu estado de atividade anterior para que a modificação covalente seja benéfica na regulação. Por fim, a conexão e a dissociação de outra proteína reguladora regula várias enzimas (10)."
import packages
nfile=0

try:
  import unicodedata
  import re
  import os
  from unidecode import unidecode
  from PIL import Image,ImageEnhance#Open the text file which you have to convert into handwriting
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

import os
my_dir = os.getcwd()
for fname in os.listdir(my_dir):
    if fname.startswith(slugify(' '.join(txt.split(' ')[0:6]))):
        os.remove(os.path.join(my_dir, fname))

def writeletter(letter,upperl,gap,ht):
  try:
    if upperl and letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
      filename="newfont/upper{}.png".format(str(ord(letter)))
    else:
      filename="newfont/{}.png".format(str(ord(letter)))
    cases = Image.open(filename)
  except:
    print("\n42 MISSING")
    print(letter,str(ord(letter)),filename)
    quit()
  else:
    BG.paste(cases, (gap, ht),cases)

with open("sizeletters.txt",'r') as arquivo:
    sizeletters=eval(arquivo.read())

def sylsplit(word):
    #print(word)
    vogals='aãáàâeéèêiíìîoóòõôuAÁÀÃÂEÉÈÊIÍÌÎOÓÒÕÔU'
    syllables=[]
    if len(word)<=3 or word==word.upper():
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

txt=txt.replace('\n',' \n ')
txt=txt.replace('.','. ')
txt=txt.replace('  ',' ')
from PIL import Image
BG=Image.open("bg.png") 
sizehyp=sizeletters["{}.png".format(str(ord('-')))]
sheet_width=BG.width
sheet_height=BG.height
gap, ht = 0, 0
endword=False
last=''
for word in txt.split(' '):
    if word=='\n':
        if ht+160>=sheet_height:
            if nfile==0:
                BG.save("{}.png".format(slugify(' '.join(txt.split(' ')[0:6]))))
            else:
                BG.save("{}({}).png".format(slugify(' '.join(txt.split(' ')[0:6])),nfile))
            nfile+=1
            BG.close()
            BG=Image.open("bg.png") 
            gap,ht=0,0
        else:
            gap,ht=0,ht+147
        last="\n"
    elif '-' in word:
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
    if not syllables==[]:
        for syl in syllables:
            upperl=False
            if len(syl)>1 and not syl[1:]==syl[1:].lower():
                upperl=True
            #print(syl, last)
            endword=False
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
                endline=True
                if endword==False and (last.isalpha() or last.isnumeric()):
                    try:
                        cases = Image.open("newfont/{}.png".format(str(ord('-'))))
                    except:
                        print("\n 140 MISSING")
                        print(letter,str(ord(letter)))
                        quit()
                    else:
                        BG.paste(cases, (gap, ht),cases)
                        last='hypen'
                        gap+=sizeletters['{}.png'.format(str(ord('-')))]-5
                if ht+152>=sheet_height:
                    if nfile==0:
                        BG.save("{}.png".format(slugify(' '.join(txt.split(' ')[0:6]))))
                    else:
                        BG.save("{}({}).png".format(slugify(' '.join(txt.split(' ')[0:6])),nfile))
                    nfile+=1
                    BG.close()
                    BG=Image.open("bg.png") 
                    gap,ht=0,0
                else:
                    gap,ht=0,ht+147
                if gap==0 and last=='-':
                    writeletter('-',False,gap,ht)
                    last=letter
                for letter in syl:
                    writeletter(letter,upperl,gap,ht)
                    last=letter
                    gap+=sizeletters['{}.png'.format(str(ord(letter)))]-5
            else:
                for letter in syl:
                    writeletter(letter,upperl,gap,ht)
                    last=letter
                    gap+=sizeletters['{}.png'.format(str(ord(letter)))]-5
    syllables=[]
    endword=True
    writeletter(' ',False,gap+5,ht)
    last=' '
    gap+=sizeletters['{}.png'.format(str(ord(' ')))]-5
if nfile==0:
    BG.save("{}.png".format(slugify(' '.join(txt.split(' ')[0:6]))))
else:
    BG.save("{}({}).png".format(slugify(' '.join(txt.split(' ')[0:6])),nfile))

import os
my_dir = os.getcwd()
for fname in os.listdir(my_dir):
    if fname.startswith(slugify(' '.join(txt.split(' ')[0:6]))):
        removebg.remove(os.path.join(my_dir, fname),False)
        img = Image.open(fname)
        converter = ImageEnhance.Color(img)
        img2 = converter.enhance(0.5)
        #img2.show()
        img2.save(fname)