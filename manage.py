# -*- coding: utf-8 -*-
# @Time    : 2017/5/23 14:33
# @Author  : wrd
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base_web.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
