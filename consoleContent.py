import os

#contents = os.popen("git diff HEAD HEAD~1 --word-diff=plain").readlines()
contents = os.popen("git diff HEAD HEAD~1 --word-diff").readlines()

for line in contents:
    print(line.strip())