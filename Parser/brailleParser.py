from louis import *


def readFile(fname):
    with open(fname) as f:
        content = f.readlines()
    d = {}
    rev_d = {}
    for i in content:
        r = i.split(' ')
        if r[1][-1] == '\n':
            r[1] = r[1][:-1]
        d[r[0]] = r[1]
        rev_d[r[1]] = r[0]
    return d,rev_d

def readFileUnicode(fname):
    with open(fname) as f:
        content = f.readlines()
    d = {}
    rev_d = {}
    for i in content:
        r = i.split(' ')
        if r[1][-1] == '\n':
            r[1] = r[1][:-1]
        r[0] = unichr(int(r[0],16))
        d[r[0]] = r[1]
        rev_d[r[1]] = r[0]
    return d,rev_d

# take a number in string and convert to corresponding 9 bit code
# eg: 1 -> 100000000, 12 -> 110000000, 19 -> 100000001
# for sending to RBC, etc:
def convertToBinary(s):
    r = 9*['0']
    for i in s:
        r[int(i)-1] = '1'
    return "".join(r)

#take a 9 bit code and convert to number, basically inverse of what above function does
#eg: 100000000 -> 1, 110000000 -> 12, 100000001 -> 19
# assuming input from perkins keyboard.
def convertFromBinary(s):
    a = 0
    ar = list(s)
    for  i in range(9):
        if ar[i]=='1':
            a = a*10 + (i+1)
    return str(a)


# convert the given string to braille seq, list of 9-bit binary code
# this function take the string in english and translates it using translation tables by liblouis
# then the translated string it converted to binary code. We select each character and use the dictionary provided in symbols.txt to convert
# to binary code.
def toBrailleGeneral(s, tbl_nm, dic):
    r = translateString([tbl_nm], s)
    l = []
    for i in r:
        l.append(convertToBinary(dic[i]))
    return l



# takes list of 9-bit string and convert to string equivalent, inverse of above function
# here we must handle the case where user presses something which does not have a mapping.
# For those characters return a character '\0' implying that user had just pressed something which is invalid.
# this can be done using the rev_dic, we can have a separate file for rev_dic
# only 6 does not have a mapping in 
def fromBrailleGeneral(st, tbl_nm, rev_dic):
    s = []
    for i in st:
        s.append(rev_dic[convertFromBinary(i)])
    stemp = "".join(s)
    return backTranslateString([tbl_nm], stemp)