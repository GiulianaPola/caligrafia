# import required module
import os
# assign directory
directory = 'myfont'
sizes=dict()
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        cases = Image.open(f)
        sizes[f]=cases.width()

with open("sizeletters.txt") as arquivo:
    arquivo.write(str(dict1))