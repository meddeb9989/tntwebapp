import xml.etree.ElementTree as ET
from xml.dom import minidom
from job import JOB
from myobjects import MyObjects


class SUBFOLDER(object):
    """docstring for SUBFOLDER"""

    myobjects = None


    def __init__(self, **kwargs):

        if "myobjects" in kwargs:
            self.myobjects = kwargs["myobjects"]

        DAYS_AND_OR=None
        IND_CYCLIC=None
        CREATED_BY=None
        SYSDB=None
        APPLICATION=None
        APPL_TYPE=None
        RETRO=None
        USE_INSTREAM_JCL=None
        PARENT_FOLDER=None
        DEC=None
        OCT=None
        MAXDAYS=None
        MAXRUNS=None
        MAXWAIT=None
        VERSION_OPCODE=None
        CHANGE_USERID=None
        AUTOARCH=None
        SUB_APPLICATION=None
        INTERVAL=None
        JUN=None
        JUL=None
        VERSION_HOST=None
        CRITICAL=None
        MAXRERUN=None
        TASKTYPE=None
        FEB=None
        AUG=None
        CONFIRM=None
        IS_CURRENT_VERSION=None
        CREATION_USER=None
        CREATION_TIME=None
        CREATION_DATE=None
        JAN=None
        ADJUST_COND=None
        CHANGE_TIME=None
        JOBISN=None
        MAR=None
        APR=None
        DESCRIPTION=None
        CYCLIC=None
        MAY=None
        SEP=None
        DAYS=None
        JOBNAME=None
        VERSION_SERIAL=None
        CHANGE_DATE=None
        CYCLIC_TOLERANCE=None
        NOV=None
        CYCLIC_TYPE=None

    def create(self):
        SUB_FOLDER = ET.Element('SUB_FOLDER')
        for attr in self.__dict__:
            if self.__dict__[attr] is not None:
                if not isinstance(self.__dict__[attr], MyObjects):
                    SUB_FOLDER.attrib[attr] = self.__dict__[attr]
        job_el = JOB(myobjects=self.myobjects)
        self.JOBNAME = raw_input("Donner le GROUP : ")
        job_el.PARENT_FOLDER=self.myobjects.get_app()+"/"+self.JOBNAME
        job_el.JOBISN=self.myobjects.get_jobisn()
        self.myobjects.jobisn_plus()
        jobname = raw_input("Donner le JOB : ")
        job_el.JOBNAME=self.JOBNAME+jobname
        JOB_tag = job_el.create()
        SUB_FOLDER.append(JOB_tag)
        return SUB_FOLDER

if __name__ == '__main__':
    sub = SUBFOLDER()
    sub.APPLICATION="ZAAAP01"
    sub.JOBISN="1"
    sub.SUB_APPLICATION="ZAAAP01"
    print minidom.parseString(ET.tostring(sub.create(), encoding="us-ascii", method="xml")).toprettyxml(indent="   ")