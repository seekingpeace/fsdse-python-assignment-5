
def countWord(fname,word):
    k = 0
    with open(fname, 'r') as f:
        for line in f:
            # print(line)
            words = line.split()
            for i in words:
                if(i==word):
                    k=k+1
    return k

print(countWord('./files/testfile.txt', 'dummy'))
