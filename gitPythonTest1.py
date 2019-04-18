from git import Repo
import git
import os

repo = Repo(os.path.join(os.getcwd(), ".git"))
print("************************************")
hcommit = repo.head.commit
print(hcommit.diff())
print(hcommit.diff('HEAD^'))
#print(hcommit.stats.total)
print(hcommit.stats.files)
# repo iter_commit
for r in repo.iter_commits():
    print(r)

# repo index iter_blob
for r in repo.index.iter_blobs():
    print(r)


print("************************************")

