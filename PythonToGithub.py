#Username and password no longer exist, so we must login with the ~token~ generated on Github


from github import Github
g = Github("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")

repo = g.get_user().get_repo("DataLogger")
all_files = []
contents = repo.get_contents("")
while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        file = file_content
        all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))

with open('AllTempLogs.csv', 'r') as file:
    content = file.read()

# Upload to github
# git_prefix = 'folder1/'
# git_file = git_prefix + 'file.txt'
git_file = 'AllTempLogs.csv'
if git_file in all_files:
    contents = repo.get_contents(git_file)
    repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
    print(git_file + ' UPDATED')
else:
    repo.create_file(git_file, "committing files", content, branch="master")
    print(git_file + ' CREATED')