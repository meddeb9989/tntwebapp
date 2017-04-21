import xml.etree.ElementTree as ET
from xml.dom import minidom
from sub_folder import SUBFOLDER
from myobjects import MyObjects


class SMARTFOLDER(object):
    """docstring for SMARTFOLDER"""

    myobjects = None

    def __init__(self, **kwargs):

        if "myobjects" in kwargs:
            self.myobjects = kwargs["myobjects"]

        DAYS_AND_OR=None
        INTERVAL=None
        SHIFT=None
        VERSION_OPCODE=None
        CREATED_BY=None
        SYSDB=None
        APPLICATION=None
        APPL_TYPE=None
        RETRO=None
        USE_INSTREAM_JCL=None
        APR=None
        PARENT_FOLDER=None
        DEC=None
        OCT=None
        MAXDAYS=None
        MAXRUNS=None
        MAXWAIT=None
        LAST_UPLOAD=None
        AUTOARCH=None
        SUB_APPLICATION=None
        REAL_FOLDER_ID=None
        JUN=None
        MODIFIED=None
        JUL=None
        VERSION_HOST=None
        PLATFORM=None
        CRITICAL=None
        MAXRERUN=None
        TASKTYPE=None
        IND_CYCLIC=None
        FEB=None
        AUG=None
        CONFIRM=None
        IS_CURRENT_VERSION=None
        CREATION_USER=None
        CREATION_TIME=None
        CREATION_DATE=None
        JAN=None
        VERSION=None
        FOLDER_NAME=None
        JOBS_IN_GROUP=None
        JOBISN=None
        DATACENTER=None
        ADJUST_COND=None
        MAR=None
        USED_BY_CODE=None
        CYCLIC=None
        MAY=None
        SEP=None
        DAYS=None
        JOBNAME=None
        VERSION_SERIAL=None
        CYCLIC_TOLERANCE=None
        NOV=None
        TYPE=None
        CYCLIC_TYPE=None

    def create(self):
        SMART_FOLDER = ET.Element('SMART_FOLDER')
        for attr in self.__dict__:
            if self.__dict__[attr] is not None:
                if not isinstance(self.__dict__[attr], MyObjects):
                    SMART_FOLDER.attrib[attr] = self.__dict__[attr]
        sub_el = SUBFOLDER(myobjects=self.myobjects)
        sub_el.APPLICATION=self.myobjects.get_app()
        sub_el.JOBISN=self.myobjects.get_jobisn()
        self.myobjects.jobisn_plus()
        sub_el.SUB_APPLICATION="APP-"+self.myobjects.get_app()
        SUB_tag = sub_el.create()
        SMART_FOLDER.append(SUB_tag)
        return SMART_FOLDER

if __name__ == '__main__':
    smart = SMARTFOLDER()
    smart.APPLICATION="ZAAAP01"
    smart.JOBISN="1"
    smart.SUB_APPLICATION="ZAAAP01"
    print minidom.parseString(ET.tostring(smart.create(), encoding="us-ascii", method="xml")).toprettyxml(indent="   ")