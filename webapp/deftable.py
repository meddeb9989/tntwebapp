import xml.etree.ElementTree as ET
from xml.dom import minidom
from smart_folder import SMARTFOLDER
from myobjects import MyObjects

class DEFTABLE(object):
    """docstring for DEFTABLE"""

    myobjects = None

    def __init__(self, **kwargs):
        self.myobjects = MyObjects()

    def create(self):
        self.menu()
        DEFTABLE = ET.Element('DEFTABLE')
        DEFTABLE.attrib["xmlns:xsi"]="http://www.w3.org/2001/XMLSchema-instance" 
        DEFTABLE.attrib["xsi:noNamespaceSchemaLocation"]="Folder.xsd"
        DEFTABLE.append(self.create_smart_folder())
        return DEFTABLE

    def menu(self):
        print "1 - Ajouter une Application \n"
        print "2 - Modifier une Application \n"
        choix = input()
        if choix == 1:
            application = raw_input("Donner le nom de l'application : ")
            self.myobjects.set_app(application)
        elif choix == 2:
            if self.myobjects.get_app() != None:
    
    def create_smart_folder(self):
        smart_el = SMARTFOLDER(myobjects=self.myobjects)
        smart_el.APPLICATION=self.myobjects.get_app()
        smart_el.JOBISN=self.myobjects.get_jobisn()
        self.myobjects.jobisn_plus()
        smart_el.SUB_APPLICATION="APP-"+self.myobjects.get_app()
        smart_el.CREATED_BY="jn07099s" 
        smart_el.TASKTYPE="SMART Table" 
        smart_el.CREATION_USER="JN07099S" 
        smart_el.VERSION_HOST="ZE0MW04A" 
        smart_el.PARENT_FOLDER=self.myobjects.get_app()
        smart_el.DATACENTER="QUAERD08" 
        smart_el.VERSION="800" 
        smart_el.PLATFORM="UNIX" 
        smart_el.FOLDER_NAME=self.myobjects.get_app()
        smart_el.MODIFIED="False" 

        return smart_el.create()

if __name__ == '__main__':
    deftable = DEFTABLE()
    et = minidom.parseString(ET.tostring(deftable.create(), encoding="utf-8", method="xml")).toprettyxml(indent="   ")
    XML_File= open('output.xml',"w")
    XML_File.write(et)
    XML_File.close()
