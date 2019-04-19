import os
import re

class GitControl:
    def initGit(self):
        initMessage = os.popen("git init")
        print(initMessage)

    def addGit(self):
        addMessage = os.popen("git add *")
        print(addMessage)
    
    def commitGit(self, message):
        commitMessage = os.popen("git commit -m \"{message}\"".format(message=message))
        print(commitMessage)


class GitLog:
    """
        파일 이름을 통해 초기화 후
        makeMessageList()를 통해 message들을 뽑아내고
        displayChange()를 통해 현재 내용과 어떤 것이 다른지 확인 가능
        diffContents(pivotNum, targetNum): pivotNum을 기준으로 targetNum의 내용과 어떻게 다른지 확인. 메시지는 targetNum의 것을 사용

    """
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

    def diffContents(self, pivotNum, targetNum):
        if(targetNum >= len(self.messageList)):
            print("targetNum is out of range!")
            return
        contents = os.popen("git diff --word-diff=plain HEAD~{targetNum} HEAD~{pivotNum} {fileName}".format(targetNum=targetNum, 
                                                                                                            pivotNum=pivotNum, 
                                                                                                            fileName=self.fileName))
        contents = [content.strip() for content in contents] # remove \n
        print("======================================================")
        print("commit number {targetNum}".format(targetNum=targetNum))
        print("message: {message}".format(message=self.messageList[targetNum - 1]))
        for content in contents:
            print(content)


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
    #gitlog = GitLog("hello.txt")
    #gitlog.makeMessageList()
    #gitlog.displayChange()
    #gitlog.diffContents(0, 10)
    gitcontrol = GitControl()
    gitcontrol.initGit()
    gitcontrol.addGit()
    gitcontrol.commitGit("git control test for new class")

#add_pattern = re.compile("{\+(.*)\+}")
#sub_pattern = re.compile("\[-(.*)-\]")

# for i, content in enumerate(contents):
#     if(re.search(add_pattern, content)):
#         start, end = re.search(add_pattern, content).span()
#         print(content[start:end])
    
    
