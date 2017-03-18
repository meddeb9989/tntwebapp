#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from sqlalchemy import create_engine

_appdir = os.path.abspath(os.path.dirname(__file__))
_basedir = _appdir.rstrip("src\sos\web")
_basedir = _appdir.rstrip("src/sos/web")

DEBUG = True

APPLICATION_ROOT = _appdir

ADMINS = frozenset(['meddeb9989@hotmail.fr'])
SECRET_KEY = 'think_u_can_guess_it_?_well_think_again'

DATABASE_FILE = 'sos/db/app.sqlite'
JSON_FILE = 'sos/json'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir,  "sos" ,"db", "app.sqlite")


DB_File = SQLALCHEMY_DATABASE_URI
engine = create_engine(DB_File)



STATIC_ASSETS_FOLDER = os.path.join(_appdir, "static", "assets")
STATIC_IMAGES_FOLDER = os.path.join(_appdir, "static", "media", "images")
IMAGES_FILE_PATH = os.path.join(_appdir, "static", "media", "images")
CAMPAIGN_IMAGE_PATH = os.path.join(_appdir, "static", "media", "images")
STATIC_THUMBNAILS_FOLDER = os.path.join(_appdir, "static", "media", "thumbnails")
JSON_PATH = os.path.join(_basedir, "sos", "json")

DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}
