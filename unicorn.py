# Rules:
# The confusion:
'''
| Python 2:  | Python 3    | What?       | 
| <'str'>    | <'bytes'>   | bytes       | 
| <'unicode' | <'unicode'> | code-points | 
'''
# How to convert:
'''
<'str'> to <'unicode'> = <'str'>.encode('encodingName')
<'unicode'> to <'str'> = <'unicode'>.decode('encodingName')
'''
# To compare two strings, they have to be of the same type:
'''
<'str'> == <'str'>          :: b"abcd" == "abcd"
<'unicode'> == <'unicode'>  :: u"abcd" == 
'''

class _Unicorn():
    def __init__(self):
        pass

    def unicodeToBytes(self,inp):
        output = inp.encode('utf-8')
        return output

    def bytesToUnicode(self,inp):
        output = inp.decode('utf-8')
        return output

    def htmlToUnicode(self,inp):
        import HTMLParser
        if not type(inp) is unicode:
            inp = self.unicodeToBytes(inp)
        parser = HTMLParser.HTMLParser()
        output = parser.unescape(inp)
        return output

    def unicodeToHtmlCodes(self,inp):
        if not type(inp) is unicode:
            inp = self.bytesToUnicode(inp)
        #utfCode = ''.join([ '\\x%02x'% ord(c) for c in inp ])
        inp = inp.replace("'",b"&#39;")
        output = inp.encode('ascii', 'xmlcharrefreplace')
        return output

    # Helper function to get unicode numbers for special characters
    def getUnicodeInteger(self,inp):
        output = ''.join([ '\\x%02x'% ord(c) for c in inp ]) # preferred option: return ascii binary : \xf0\x9f\x92\xa9\x20 
        #output = self.bytesToUnicode(inp).encode('ascii','xmlcharrefreplace') # return html entity  : &#128169;
        return bytes(output)

    # CONVERTER FUNCTIONS
    def utfToBytes(self,inp):
        byt     = inp.decode("string-escape") # convert unicode integers
        uni     = self.bytesToUnicode(byt)
        resHtml = self.htmlToUnicode(uni)
        output  = self.unicodeToBytes(resHtml)
        return output

    # Good for writing content that goes into html fields on the web.
    def bytesToHtml(self,inp):
        htm = self.unicodeToHtmlCodes(inp)
        output = htm
        return output

# XXX TESTING

def compare():
    # How to compare your code strings with utf-8 text input:
    # Make sure that the two strings you want to compare are of the same type (<'unicode'> or <'str'> (where str == bytes))
    # Define your string with unicode integers and/or HTML-codes
    # See this page for reference: http://unicode-table.com/en/#0032
    # Or use the above getUnicodeInteger() function to get the unicode-integer of a special character
    byt = _unicorn.utfToBytes("Fynn&#39;s c\xc3\xb6de \xc3\xa5")
    print "looking for: ",byt,type(byt)

    # Do the same conversion for you input text and you should be good to go. No matter where the text comes from, as long as it's utf-8 all is well.
    strng = raw_input("Type something:\n")
    strng = _unicorn.utfToBytes(strng)
    print strng,type(strng)
    print strng==byt

def forWeb():
    # Convert to paste text into an html field
    inp = raw_input("Write Something:\n")
    print _unicorn.bytesToHtml(inp)

if __name__ == "__main__":
    import sys
    print sys.getdefaultencoding()
    _unicorn = _Unicorn() # for converting utf-8 stuff back and forth
    # compare()
    # forWeb()
    inp = raw_input("Type something:\'")
    _unicorn.getUnicodeInteger(inp)