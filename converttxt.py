txt="Bioquímica 2\nAtividade 4 - Ciclo do Ácido Cítrico\nGiuliana Lopes Pola - 11779802"
import packages
nfile=0

lowers='abcçdefghijklmnopqrstuvwxyzáàãâéèêíìîóòõôúùû'
uppers='ABCÇDEFGHIJKLMNOPQRSTUVWXYZÁÀÃÂÉÈÊÍÌÎÓÒÕÔÚÙÛ'
vogals='aeiouáàãâéèêíìîóòõôúùûAEIOUÁÀÃÂÉÈÊÍÌÎÓÒÕÔÚÙÛ'

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
    if upperl and letter in uppers:
      filename="newfont/upper{}.png".format(str(ord(letter)))
    else:
      filename="newfont/{}.png".format(str(ord(letter)))
    cases = Image.open(filename)
  except:
    print("\n42 MISSING")
    print(letter,str(ord(letter)),filename)
    quit()
  else:
    cases = Image.open(filename)
    # if upperl and letter in uppers:
    #     gap+=5
    # elif letter in lowers and gap>0 and last in lowers:
    #     gap+=-5
    BG.paste(cases, (gap, ht),cases)

with open("sizeletters.txt",'r') as arquivo:
    sizeletters=eval(arquivo.read())

def sylsplit(word):
    #print(word)
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
    upperl=False
    syllables=[]
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
        if word==word.upper() and len(word)>1:
            syllables=[word]
            upperl=True
        else:
            syllables=sylsplit(word)
    if not syllables==[]:
        for syl in syllables:
            if gap>0:
                gap+=-5
            if len(syl)>1 and not syl[1:]==syl[1:].lower():
                upperl=True
                print("if len(syl)>1 and not syl[1:]==syl[1:].lower():")
            elif len(syl)==1 and not syl==syllables[0]:
                upperl=True
                print("elif len(syl)==1 and not syl in 'OAÉ':")
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
                        gap+=sizeletters['{}.png'.format(str(ord('-')))]
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
                    gap+=sizeletters['{}.png'.format(str(ord(letter)))]
                for letter in syl:
                    writeletter(letter,upperl,gap,ht)
                    last=letter
                    gap+=sizeletters['{}.png'.format(str(ord(letter)))]
            else:
                for letter in syl:
                    writeletter(letter,upperl,gap,ht)
                    last=letter
                    gap+=sizeletters['{}.png'.format(str(ord(letter)))]
    syllables=[]
    endword=True
    writeletter(' ',False,gap+5,ht)
    last=' '
    gap+=sizeletters['{}.png'.format(str(ord(' ')))]
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