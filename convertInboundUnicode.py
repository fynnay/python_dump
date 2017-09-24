'''
Assume the document is in ASCII encoding.

- Always .decode('CorrectCodecHere') stuff right after it goes into your program
- Always .encode('CorrectCodecHere') stuff before it goes out of your program (especially when writing to files)
'''
# Encode all output, also stuff that just is displayed on screen\
# Decode all input, even if it's not read from a file but input directly:
uinp = raw_input( u"Write something: ".encode('utf-8') ).decode('utf-8')

tmpFilePath = '/Users/fynn/Desktop/test.txt'
tempfile = open(tmpFilePath,'w')
tempText = u"somethingsomething %s"%uinp
# Encode output before writing to file:
tempfile.write( tempText.encode('utf-8') )