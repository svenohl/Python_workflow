print("Start parsing ...")

#show content in working directory

# open a file
f = open("booklist.txt",'r')
fout = open("output.txt",'w')

cnt = 0
for x in f:
    cnt = cnt + 1
    outputs = "Diese Zeile ist so lange: "
    outputx = outputs + str(len(x))
    #print(outputx)
    words = x.split()
    for word in words:
        if word == "book":
            print("We need to act on this key word")
            fout.write(x)
            fout.write(x[len(x)::-1])

f.close()
fout.close()