#You must make and submit your own test file and txt file with this assignment.

def toString():
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open("6_02_HW.txt")
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine():
    #Given a file return the longest line from within that file
    f = open("6_02_HW.txt")
    longestLine = ""
    for line in f:
        if len(line) > len(longestLine):
            longestLine = line
    return longestLine


def toBinary():
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    f = open("binaryfile.txt")
    data = ""
    for line in f:
        if line[-1] == "\n":
            data += line[:-1]
        else:
            data += line
    byte = []
    for i in range(0, len(data), 8):
        byte.append(data[i:i+8])
    return byte

