from brailleParser import *
import os
language = {'eng1':'../tables/en-us-g1.ctb', 'eng2':'../tables/en-us-g2.ctb', 'hindi':'hi.ctb'}
lang = 'eng1'
dic, rev_dic = readFile(os.getcwd()+'/Parser/englishSymbols.txt')
 
# create mapping for 7,8,9 here
dic[' '] = '9'
rev_dic['9'] = ' '

def toBraille(s):
    return toBrailleGeneral(st,language[lang],dic)

def fromBraille(st):
    return fromBrailleGeneral(st,language[lang],rev_dic)

#example for testing
#fromBraille(map(convertToBinary,['1','6','1','9','1']))
#map(convertFromBinary,toBraille('My name is Slim Shady'))

