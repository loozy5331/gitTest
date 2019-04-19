import os
import re
"""
 HEAD~1(바로 전 내용)에서 HEAD(현재)의 차이점을 단어 별로 출력
<예시 내용>
1. new text!
2. new text add word!
3. new text word!
4. new text add word! {+new contents!+} 
5. new
text!
6. hello world!
"""

#contents = os.popen("git diff HEAD~1 HEAD --word-diff=plain").readlines()
#contents = [content.strip() for content in contents] # remove /n

class GitLog:
    def __init__(self, fileName):
        self.fileName = fileName
        self.messageList = list()

    def makeMessageList(self):
        logs = os.popen("git log").readlines()
        logs = [log.strip() for log in logs] # remove \n

        for i, line in enumerate(logs):
            if(i == 4 or (i - 4) % 6 == 0):
                self.messageList.append(line)
                print("line {}: {}".format(i, line))

    def displayChange(self):
        for i, message in enumerate(self.messageList):
            contents = os.popen("git diff --word-diff=plain HEAD~{i} HEAD {fileName}".format(i=i, fileName=self.fileName)).readlines()
            contents = [content.strip() for content in contents]
            print("commit number {}  : ".format(i))
            print("message: {}".format(message))
            for content in contents:
                print(content)
            print("\n")

if __name__ == "__main__":
    gitlog = GitLog("hello.txt")
    gitlog.makeMessageList()
    gitlog.displayChange()

#add_pattern = re.compile("{\+(.*)\+}")
#sub_pattern = re.compile("\[-(.*)-\]")

# for i, content in enumerate(contents):
#     if(re.search(add_pattern, content)):
#         start, end = re.search(add_pattern, content).span()
#         print(content[start:end])
    
    
