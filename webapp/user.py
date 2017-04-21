#!/usr/bin/env python
# -*- coding: utf-8 -*-

class User():

    login = None
    password = None
    id=None

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

		