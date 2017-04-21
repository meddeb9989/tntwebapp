import xml.etree.ElementTree as ET
from xml.dom import minidom
from myobjects import MyObjects

class JOB(object):
    """docstring for JOB"""

    myobjects = None

    def __init__(self, **kwargs):

        if "myobjects" in kwargs:
            self.myobjects = kwargs["myobjects"]

        self.DAYS_AND_OR=None
        self.SHIFT=None
        self.NODEID=None
        self.CREATED_BY=None
        self.SYSDB=None
        self.APPLICATION=None
        self.APPL_TYPE=None
        self.RETRO=None
        self.USE_INSTREAM_JCL=None
        self.MEMNAME=None
        self.PARENT_FOLDER=None
        self.DEC=None
        self.OCT=None
        self.MAXDAYS=None
        self.TIMEFROM=None
        self.MAXWAIT=None
        self.SEP=None
        self.RUN_AS=None
        self.AUTOARCH=None
        self.SUB_APPLICATION=None
        self.INTERVAL=None
        self.JUN=None
        self.JUL=None
        self.VERSION_HOST=None
        self.CMDLINE=None
        self.CRITICAL=None
        self.MAXRERUN=None
        self.TASKTYPE=None
        self.IND_CYCLIC=None
        self.FEB=None
        self.AUG=None
        self.CONFIRM=None
        self.IS_CURRENT_VERSION=None
        self.CREATION_USER=None
        self.CREATION_TIME=None
        self.SHIFTNUM=None
        self.CREATION_DATE=None
        self.JAN=None
        self.MAXRUNS=None
        self.JOBISN=None
        self.RULE_BASED_CALENDAR_RELATIONSHIP=None
        self.MULTY_AGENT=None
        self.MAR=None
        self.APR=None
        self.DESCRIPTION=None
        self.CYCLIC=None
        self.MAY=None
        self.VERSION_OPCODE=None
        self.WEEKDAYS=None
        self.TIMETO=None
        self.JOBNAME=None
        self.VERSION_SERIAL=None
        self.CYCLIC_TOLERANCE=None
        self.NOV=None
        self.CYCLIC_TYPE=None
        self.CHANGE_USERID=None
        self.CONFCAL=None
        self.CHANGE_TIME=None
        self.CHANGE_DATE=None
        self.DAYS=None

    def create(self):
        JOB = ET.Element('JOB')
        for attr in self.__dict__:
            if self.__dict__[attr] is not None:
                if not isinstance(self.__dict__[attr], MyObjects):
                    JOB.attrib[attr] = self.__dict__[attr]
        return JOB

if __name__ == '__main__':
    job = JOB()
    job.PARENT_FOLDER="ZAAAP01"
    job.JOBISN="1"
    job.JOBNAME="ZAAAP01"
    print minidom.parseString(ET.tostring(job.create(), encoding="us-ascii", method="xml")).toprettyxml(indent="   ")

    