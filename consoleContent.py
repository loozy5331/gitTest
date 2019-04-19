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
messageList = list()

contents = os.popen("git diff HEAD~1 HEAD~2 --word-diff=plain").readlines()
contents = [content.strip() for content in contents]
logs = os.popen("git log").readlines()
logs = [log.strip() for log in logs]

# for i, line in enumerate(logs):
#     if(i == 4 or (i - 4) % 6 == 0):
#         messageList.append(line)
#         print("line {}: {}".format(i, line))

add_pattern = re.compile("{\+(.*)\+}")
sub_pattern = re.compile("\[-(.*)-\]")

for i, content in enumerate(contents):
    contentWordList = content.split(" ")
    for j, content in enumerate(contentWordList):
        if(re.search(add_pattern, content)):
            print("({}, {}) {}".format(i, j, content))
        #print(re.findall(sub_pattern, content))
    
    
