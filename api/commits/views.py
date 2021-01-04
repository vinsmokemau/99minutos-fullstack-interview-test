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
                {'name': branch.name}
            )
        
        return Response(data)


class BranchDetail(APIView):

    def get(self, request, branch_name):
        """Return a list of all commits in the branch."""
        data = []
        commits = repo.iter_commits(branch_name)
        for commit in commits:
            
            data.append(
                {
                    'id': str(commit),
                    'author': commit.author.name,
                    'message': commit.message,
                    'timestamp': commit.authored_date,
                }
            )

        return Response(data)


class CommitDetail(APIView):

    def get(self, request, commit_id):
        """Return the data of a commit."""
        commit = repo.commit(commit_id)
        files = repo.git.show('--name-only', '--pretty=', f'{commit}')
        no_files = len(files.split('\n'))
        
        data = {
            'id': str(commit),
            'files': no_files,
            'author': commit.author.name,
            'mail': commit.author.email,
            'message': commit.message,
            'timestamp': commit.authored_date,
        }

        return Response(data)
