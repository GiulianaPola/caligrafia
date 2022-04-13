#file=open("ASCIIchars.txt","w")
for i in range(500):
    try:
        print("{}\t{}\n".format(i,chr(i)))
    except:
        pass
#char="û"
#print(char,str(ord(char)))
# i=244
# print(i,chr(i))
# file.close()