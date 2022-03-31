#Importing Library
from PIL import Image#Open the text file which you have to convert into handwriting
txt="enzima desta forma." # path of your text file#path of page(background)photo (I have used blank page)
BG=Image.open("myfont/bg.png") 
sheet_width=BG.width
gap, ht = 0, 0
for word in txt.split():
    for letter in word:
        try:
            cases = Image.open("sem fundo/{}.png".format(str(ord(letter))))
        except:
            print("\nMISSING")
            print(letter,str(ord(letter)))
            quit()
        newgap=gap+cases.width
        if letter==word[-1]:

        print(i,str(ord(i)))
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
            if sheet_width < gap or len(letter)*115 >(sheet_width-gap):
                #print(i,str(ord(i)))
                gap,ht=0,ht+300
print(gap)
print(sheet_width)
#BG.show()
BG.save("teste.png")