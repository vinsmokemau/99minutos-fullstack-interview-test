from git import Repo


repo = Repo('.')

branches = repo.heads
for branch in branches:
    print(f'Branch: {branch.name}\n')

commits = repo.iter_commits('develop')
previous_commit = ''
for commit in commits:
    print(f'Id: {commit}')
    files = repo.git.show('--name-only', '--pretty=', f'{commit}')
    no_files = len(files.split('\n'))
    print(f'Number of files changed: {no_files}')
    print(f'Author: {commit.author.name}')
    print(f'Mail: {commit.author.email}')
    print(f'Message: {commit.message}')
    print(f'Timestamp: {commit.authored_date}\n')

commit = repo.commit(f'{commit}')
print(f'Id: {commit}')
files = repo.git.show('--name-only', '--pretty=', f'{commit}')
no_files = len(files.split('\n'))
print(f'Number of files changed: {no_files}')
print(f'Author: {commit.author.name}')
print(f'Mail: {commit.author.email}')
print(f'Message: {commit.message}')
print(f'Timestamp: {commit.authored_date}\n')
