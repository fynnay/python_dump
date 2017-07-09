#======================================================
# CreateSymlinks.py
# Run this file via the terminal with arguments:
# $ python CreateSymlinks.py <input-folder/file> <output-folder>
#======================================================

import os
import sys

def createHardlink(sFile,dFile):
    print "Creating Link: %s -> %s"%(sFile,dFile)
    cmd = ""
    return

def main(sPath,dPath):
    # Cancel if destination doesn't exist
    if not os.path.exists(dPath):
        print "Destination doesn't exist."
        return
    if os.path.isfile(dPath):
        print "Destination can't be a file."
        return
    # Cancel if source and destination are or have same parent-folder
    if sPath == dPath or os.path.dirname(sPath) == dPath:
        print "Destination has to differ from source."
        return
    # Cancel if source doesn't exist
    if not os.path.exists(sPath):
        print "Source doesn't exist."
        return
    # Check if the source is a file
    if os.path.isfile(sPath):
        fileName     = os.path.basename(sPath)
        destFilePath = os.path.join(dPath,fileName)
        createHardlink(sPath,destFilePath)
    else:
        for root, dirs, files in os.walk(sPath):
            print root
#__INIT__
# Cancel if not enough arguments passed
if not len(sys.argv) == 3:
    print "Not enough arguments passed."
else:
    # sys.argv[0] = $path
    # sys.argv[1] = source
    # sys.argv[2] = destination
    main(sys.argv[1],sys.argv[2])