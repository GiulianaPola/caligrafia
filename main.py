#Importing Library
from PIL import Image#Open the text file which you have to convert into handwriting
txt="enzima desta forma." # path of your text file#path of page(background)photo (I have used blank page)
BG=Image.open("myfont/bg.png") 
sheet_width=BG.width
gap, ht = 0, 0
for i in txt:
    print(i,str(ord(i)))
    try:
        cases = Image.open("sem fundo/{}.png".format(str(ord(i))))
    except:
        print("\nMISSING")
        print(i,str(ord(i)))
        pass
    else:
        BG.paste(cases, (gap, ht))
        size = cases.width
        height=cases.height
        #print(size)
        gap+=size
        if sheet_width < gap or len(i)*115 >(sheet_width-gap):
            #print(i,str(ord(i)))
            gap,ht=0,ht+300
print(gap)
print(sheet_width)
#BG.show()
BG.save("teste.png")