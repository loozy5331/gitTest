import os

#contents = os.popen("git diff HEAD~1 HEAD --word-diff=plain").readlines()
contents = os.popen("git diff HEAD~1 HEAD --word-diff=plain").readlines()

for line in contents:
    print(line.strip())