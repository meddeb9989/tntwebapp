#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'meddebmohamedfakher'


class MyObjects():
    application = None
    jobs = {}
    sub_folders = {}
    JOBISN = 1

    def set_app(self, app):
        self.application = app
    
    def set_jobs(self, job):
        self.jobs.append(job)

    def set_subs(self, sub):
        self.sub_folders.append(sub)

    def jobisn_plus(self):
        self.JOBISN = self.JOBISN + 1

    def get_app(self):
        return self.application

    def get_jobs(self):
        return self.jobs

    def get_subs(self):
        return self.sub_folders

    def get_jobisn(self):
        return str(self.JOBISN)
