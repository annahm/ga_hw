# CHAL #2:  str.maketrans(), ascii table character translation, ord(), chr()
# ocr.html
import sys

#s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def trans(s):
    a = ""
    for i in range(0,len(s)):
        o = ord(s[i])
        if o in range(97,121):
            a = a + chr(o+2)
        elif o in range(121,123):
            a = a + chr(o+2-26)
        else:
            a = a + s[i]
    print s + "\n"
    print a

def main(argv):
    if (len(argv) < 2):
        print "Usage: python 2.py <string to map>"
        exit(0)
    trans(argv[1])
  
if __name__ == "__main__":
    main(sys.argv)
