while 1:
    f = open("score.txt",'r')
    text = str(f.read())
    for line in f:
        text = text + str(f.readlines())
    #text.split("\n")
    print(text)
