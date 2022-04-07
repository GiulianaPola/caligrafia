def run():
    print("\nMeasuring the size of the letter's image...")
    from PIL import Image
    # import required module
    import os
    # assign directory
    #os.chdir('..')
    #print(os.listdir(os.getcwd()))
    directory = 'sem fundo'
    sizes=dict()
    
    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            cases = Image.open(f)
            sizes[filename]=cases.width

    with open("sizeletters.txt","w") as arquivo:
        arquivo.write(str(sizes))

run()