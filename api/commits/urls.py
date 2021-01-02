"""Commits' urls."""

# Django
from django.urls import path

# Views
from .views import (
    ListBranches,
    BranchDetail,
    CommitDetail,
)

urlpatterns = [
    
    path(
        'branches/',
        ListBranches.as_view(),
        name='branches',
    ),

    path(
        'branches/<str:branch_name>/',
        BranchDetail.as_view(),
        name='branch',
    ),

    path(
        'commits/<str:commit_id>/',
        CommitDetail.as_view(),
        name='commit',
    ),

]
