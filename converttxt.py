import os
os.system("removebg.py")
os.system("measureletters.py")
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
txt='O tema Cidadania no Brasil envolve diversos subtópicos super importantes de ressaltar, como os tópicos da Cidadania política, cidadania social e também a cidadania ambiental. O termo cidadania envolve uma afinidade entre o povo e o Estado, seja por meio dos direitos ou dos deveres, mostrando o que o povo pode e deve reivindicar(os direitos) e também o que o povo deve e pode fazer (os deveres). Os direitos intrínsecos na cidadania são os direitos civis, que garantem aos cidadãos direitos de movimentação social, e comunicação; há também os direitos políticos que garantem a movimentação política e expressão de opinião política do povo; além também da existência dos direitos sociais que garantem ao povo o acesso aos serviços que o Estado tem a obrigação de fornecer aos cidadãos.' # path of your text file#path of page(background)photo (I have used blank page)
BG=Image.open("bg.png") 
sizehyp=sizeletters["{}.png".format(str(ord('-')))]
sheet_width=BG.width
gap, ht = 0, 0
end=False
last=''
for word in txt.split():
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
        sizesyl=[sizeletters["{}.png".format(str(ord(letter)))] for letter in syl]
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
                    print("\nMISSING")
                    print(letter,str(ord(letter)))
                    quit()
                else:
                    BG.paste(cases, (gap, ht))
                    size = cases.width
                    height=cases.height
                    last='hypen'
                    gap+=size 
            gap,ht=0,ht+180
            if gap==0 and last=='-':
                try:
                    cases = Image.open("sem fundo/{}.png".format(str(ord('-'))))
                except:
                    print("\nMISSING")
                    print(letter,str(ord(letter)))
                    quit()
                else:
                    BG.paste(cases, (gap, ht))
                    size = cases.width
                    height=cases.height
                    last='-'
                    gap+=size 
            for letter in syl:
                try:
                    cases = Image.open("sem fundo/{}.png".format(str(ord(letter))))
                except:
                    print("\nMISSING")
                    print(letter,str(ord(letter)))
                    quit()
                else:
                    BG.paste(cases, (gap, ht))
                    size = cases.width
                    height=cases.height
                    last=letter
                    gap+=size 
        else:
            for letter in syl:
                try:
                    cases = Image.open("sem fundo/{}.png".format(str(ord(letter))))
                except:
                    print("\nMISSING")
                    print(letter,str(ord(letter)))
                    quit()
                else:
                    BG.paste(cases, (gap, ht))
                    size = cases.width
                    height=cases.height
                    #print(size)
                    gap+=size
                    last=letter
    end=True
    try:
        cases = Image.open("sem fundo/{}.png".format(str(ord(' '))))
    except:
        print("\nMISSING")
        print(letter,str(ord(letter)))
        quit()
    else:
        BG.paste(cases, (gap, ht))
        size = cases.width
        height=cases.height
        last=' '
        gap+=size
BG.show()
BG.save("teste.png")