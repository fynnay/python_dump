import sys
import subprocess

# Run command
cmd = "ls /Users/fynn/Desktop"
exe = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# Wait for it to finish
exe.wait()

# Read output
output = exe.communicate()
# Split each line into new item in list
stdoutList = output[0].split("\n")
stdErrList = output[1].split("\n")

# OUTPUT
for i in stdoutList:
    print i
    if i == "dein mudda":
        print "------ WEEEE! -----"

# ERRORS
for i in stdErrList:
    print i
    if i == "dein mudda":
        print "------ WEEEE! -----"
