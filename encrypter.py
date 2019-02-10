#!/usr/bin/python
# Encrypter v1
# Author: Shawar Khan



# Importing Modules
import hashlib
import sys
import base64
import urllib


# Usage and User Input
usage = '''\nEncrypter v1
Author: Shawar Khan

Usage:

      --help,-h\tShows this help message
      -s\tString inputted for encoding


      python encrypter.py <option>
      python encrypter.py -s 'stringhere'

'''


# Arg Checks
try:
        if len(sys.argv) > 1:
                options = '-h --help -s'.split()
                for argname,argnum in zip(sys.argv,range(len(sys.argv))):
                        if '-h' in sys.argv or '--help' in sys.argv or '-s' in sys.argv:
                                if argname == '-h' or argname == '--help':
                                        print usage
                                        exit()
                                if argname == '-s':
                                        userinput = sys.argv[argnum+1]
                                else:
                                        pass
                        else:
                                print 'invalid options'
                                print usage
                                exit()
        else:
                raise IndexError
except(IndexError):
        print usage
        exit()

# Printing the Banner
def banner():
        print '\nEncrypter v1'
        print 'Author: Shawar Khan ( @shawarkhanethicalhacker )\n'
        print '\n'

"""num = sys.argv[1].split('-')

print '    Generating %s hashes:\n'%num[1]
for i in range(int(num[0])+1,int(num[1])+1):
        print hashlib.md5(str(i)).hexdigest()"""

# MD5 Function
def md5(string):
        return "[*] MD5     : %s"%hashlib.md5(str(string)).hexdigest()


# SHA1 Function
def sha1(string):
        return "[*] SHA1    : %s"%hashlib.sha1(str(string)).hexdigest()

# Base64 Function
def base64en(string):
        return "[*] Base64  : %s"%base64.b64encode(str(string))


# SHA224 Function
def sha224en(string):
        return "[*] SHA224  : %s"%hashlib.sha224(str(string)).hexdigest()


# SHA256 Function
def sha256en(string):
        return "[*] SHA256  : %s"%hashlib.sha256(str(string)).hexdigest()


# SHA384 Function
def sha384en(string):
        return "[*] SHA384  : %s"%hashlib.sha384(str(string)).hexdigest()


# SHA512 Function
def sha512en(string):
        return "[*] SHA512  : %s"%hashlib.sha512(str(string)).hexdigest()


# Urlencode Function
def custhexen(string,sign='\\x',end=''):
        encodedstring = string.encode('hex')
        final = []
        val1 = ''
        val2 = ''
        for i in encodedstring:
                if val1 == '':
                        val1 = i
                elif val1 != '' and val2 == '':
                        val2 = i
                if val1 != '' and val2 != '':
                        final.append(str(sign)+str(val1)+str(val2)+str(end))
                        val1 = ''
                        val2 = ''
        finalstring = ''.join(final)
        if sign == '%':
                return "[*] URL     : %s"%finalstring
        if sign == '&#x':
                return "[*] HTML    : %s"%finalstring
        else:
                return "[*] Hex \\x  : %s"%finalstring


# Hex Function
def hexen(string):
        return "[*] Hex     : %s"%string.encode('hex')


# ROT13 Function
def rot13en(string):
        return "[*] ROT13   : %s"%string.encode('rot13','strict')


# Program Start
try:
        banner()
        print '[*] Plain   : %s'%userinput
        print md5(userinput)
        print sha1(userinput)
        print base64en(userinput)
        print custhexen(userinput,'%')
        print custhexen(userinput)
        print hexen(userinput)
        print custhexen(userinput,'&#x',';')
        print rot13en(userinput)
        print sha224en(userinput)
        print sha256en(userinput)
        print sha384en(userinput)
        print sha512en(userinput)
        print '\n'
except(Exception,KeyboardInterrupt), Err:
        exit()
