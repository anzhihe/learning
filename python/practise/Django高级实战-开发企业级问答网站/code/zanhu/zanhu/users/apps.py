#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = '__Jack__'

from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'zanhu.users'
    verbose_name = '用户'

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        try:
            import users.signals  # noqa F401

        except ImportError:
            pass
