"""Commits' Views."""

# GitPython
from git import Repo

# Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Get the current repository
repo = Repo('..')


class ListBranches(APIView):

    def get(self, request):
        """Return a list of all branches."""
        data = []
        branches = repo.heads
        for branch in branches:
            data.append(
                {'Name': branch.name}
            )
        
        return Response(data)


class BranchDetail(APIView):

    def get(self, request, branch_name):
        """Return a list of all commits in the branch."""
        data = []
        commits = repo.iter_commits(branch_name)
        for commit in commits:
            files = repo.git.show('--name-only', '--pretty=', f'{commit}')
            no_files = len(files.split('\n'))
            
            data.append(
                {
                    'Id': str(commit),
                    'Files': no_files,
                    'Author': commit.author.name,
                    'Mail': commit.author.email,
                    'Message': commit.message,
                    'Timestamp': commit.authored_date,
                }
            )

        return Response(data)
