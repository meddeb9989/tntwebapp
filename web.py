#!/usr/bin/env python
# -*- coding: utf-8 -*-
from webapp import app

if __name__ == '__main__':
    app.debug = True
    app.run()