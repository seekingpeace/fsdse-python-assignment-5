#Question - 5: Write a function, countWord(filename, word), that should count and return how many
#times word appears in file.create a file and put some dummy content to that.
def countWord(fileName, word):
    try:
        file = open(fileName,"r")
    except:   # If exception is not known you can leave this blank
        print ("file does't exist")
        return
    count = 0;
    line = file.readline()
    while (line != ""):
        words = line.split()
        for i in words:
            if i == word:
                count = count + 1
        line = file.readline()
    file.close()
    return count