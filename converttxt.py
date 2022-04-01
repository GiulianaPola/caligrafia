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
    print(syllables)
    return syllables

#Importing Library
from PIL import Image#Open the text file which you have to convert into handwriting
txt='A conversão da glicose em glicose-6-fosfato por hexoquinase, a fosforilação do frutose-6-fosfato em frutose-1,6-bifosfato por fosfofrutoquinase-1, e a conversão do fosfoenolpiruvato em piruvato por piruvato quinase são essencialmente irreversíveis e não podem ser utilizados em gliconeogênese. As reações de compromisso são processos irreversíveis da glicólise. Como resultado, elas ajudam na continuação da reação. O primeiro processo irreversível impede que a glicose escape da célula. O segundo garante que os produtos lisados (gliceraldeído-3-fosfato + diidroxiacetona-fosfato) não recombinem, e o terceiro garante que o piruvato não retorne à sua posição original na via. ' # path of your text file#path of page(background)photo (I have used blank page)
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
#BG.save("teste.png")