with open("sizeletters.txt",'r') as arquivo:
    sizeletters=eval(arquivo.read())

vowels = 'AEIOU'
consts = 'BCDFGHJKLMNPQRSTVWXYZ'
consts = consts + consts.lower()
vowels = vowels + vowels.lower()

def is_vowel(letter):
    return letter in vowels 
def is_const(letter):
    return letter in consts

def sylsplit(word):
    segment_length = 4 # because this pattern needs four letters to check
    pattern = [is_vowel, is_const, is_const, is_vowel] # functions above
    split_points = []

    # find where the pattern occurs
    for i in range(len(word) - segment_length):
        segment = word[i:i+segment_length]

        # this will check the four letter each match the vc/cv pattern based on their position
        # if this is new to you I made a small note about it below
        if all([fi(letter) for letter, fi in zip(segment, pattern)]):
            split_points.append(i+segment_length/2)

    # use the index to find the syllables - add 0 and len(word) to make it work
    split_points.insert(0, 0)
    split_points.append(len(word))
    syllables = []\
    for i in range(len(split_points) - 1):
        start = split_points[i]
        end = split_points[i+1]
        syllables.append(word[start:end])
    return syllables

#Importing Library
from PIL import Image#Open the text file which you have to convert into handwriting
txt="enzima desta forma." # path of your text file#path of page(background)photo (I have used blank page)
BG=Image.open("myfont/bg.png") 
sheet_width=BG.width
gap, ht = 0, 0
for syllable in sylsplit(word):
    syl=''
    sizesyl=0
    for letter in word:
        try:
            syl+=letter
            sizesyl+=sizeletters["{}.png".format(str(ord(letter)))]
            if letter in "aeiouAEIOU":
                if letter==word[-1]:
                    newgap=gap+sizessyl
                else:
                    newgap=gap+sizessyl+sizeletters["{}.png".format(str(ord('-')))]
                if sheet_width < newgap or len(letter)*115 >(sheet_width-newgap):
                    gap,ht=0,ht+300
                for letter2 in syl:
                syl=''
                sizesyl=0
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