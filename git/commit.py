import os


def commit():
    count = 0
    while True:
        os.system('git commit --allow-empty --allow-empty-message -m test')
        count ++
        print(str(count) + ':commits')


new = True
if not new:
    try:
        commit()
    except KeyboardInterrupt:
        os.system("git push origin master --force")
if new:
    os.system('git init')
    repository = input("Repository URL: ")
    os.system(f'git remote add origin {repository}')
    try:
        commit()
    except KeyboardInterrupt:
        os.system("git push origin master --force")
