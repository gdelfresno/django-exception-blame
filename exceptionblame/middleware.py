import os
import sys
import traceback

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed

from git import Repo


class ExceptionBlameMiddleware(object):
    def __init__(self):
        if not settings.DEBUG or not settings.EXCEPTION_BLAME or \
                not settings.EXCEPTION_BLAME['REPO_DIR']:
            raise MiddlewareNotUsed()

    @staticmethod
    def process_exception(request, exception):
        exception_traceback = sys.exc_traceback

        stack = traceback.extract_tb(exception_traceback)

        repo_dir = settings.EXCEPTION_BLAME['REPO_DIR']
        repo = Repo(repo_dir)

        first_file_project = None
        for stack_file in reversed(stack):
            file_path = stack_file[0]

            if repo.git.ls_files(file_path, {'error-unmatch':True}):
                first_file_project = stack_file
                break

        if first_file_project:
            file_path = first_file_project[0]
            abs_linenumber = first_file_project[1]
            blame = repo.blame(None, file_path)

            # blame returns array with lists [commit, [lines]]
            blame_commit = [commit[0]
                            for commit in blame
                                for _ in commit[1]][abs_linenumber-1]


            author = blame_commit.author.name
            if author == 'Not Committed Yet':
                author = author + ', probably your modifications'
            else:
                author = '{} - {}'.format(author, blame_commit.author.email)

            request.META['BLAMED_DEVELOPER'] = author
