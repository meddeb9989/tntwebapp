#!/usr/bin/env python
# -*- coding: utf-8 -*-
from webapp import app
import os

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run()
