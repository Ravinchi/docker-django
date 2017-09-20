# import uwsgi
# from uwsgidecorators import filemon

# @filemon('/webapp')
# def file_chaged(num)
#     uwsgi.reload()

import uwsgi
from uwsgidecorators import timer
from django.utils import autoreload

@timer(3)
def change_code_gracefull_reload(sig):
    if autoreload.code_changed():
        uwsgi.reload()