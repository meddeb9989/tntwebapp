import xml.etree.ElementTree as ET
import json

from xml.etree.ElementTree import Element, SubElement, Comment
from xml.dom import minidom

class XMLPARSE(object):
    """docstring for XMLPARSE"""
    def __init__(self, **kwargs):
        super(XMLPARSE, self).__init__(**kwargs)

    def parse(self, xmlfile):
        et = ET.parse(xmlfile)
        root = et.getroot()
        #print root.tag
        #for child in root:
            #print "tag : " + child.tag + "\n" + "attributes : \n"
        #    data=str(child.attrib).strip("'<>() ").replace('\'', '\"')
        #    attrib = json.loads(data)
            #for attr in attrib:
                #print attr + " : VALUE : " + attrib[attr]
        job_attributes = []
        SUB_FOLDER_attributes = []
        SMART_FOLDER_attributes = []

        job= open('job.xml',"w")
        sub= open('sub.xml',"w")
        smart= open('smart.xml',"w")
        
        for rank in root.iter('JOB'):
            for attr in rank.attrib:
                if attr not in job_attributes:
                    job_attributes.append(attr)
                    et = attr + "=None\n"
                    job.write(et)

        for rank in root.iter('SUB_FOLDER'):
            for attr in rank.attrib:
                if attr not in SUB_FOLDER_attributes:
                    SUB_FOLDER_attributes.append(attr)
                    et = attr + "=None\n"
                    sub.write(et)

        for rank in root.iter('SMART_FOLDER'):
            for attr in rank.attrib:
                if attr not in SMART_FOLDER_attributes:
                    SMART_FOLDER_attributes.append(attr)
                    et = attr + "=None\n"
                    smart.write(et)

        smart.close()
        sub.close()
        job.close()

        print str(len(job_attributes)) + " JOB ATTRIBUTES : \n"
        print str(len(SUB_FOLDER_attributes)) + " SUB_FOLDER ATTRIBUTES : \n"
        print str(len(SMART_FOLDER_attributes)) + " SMART_FOLDER ATTRIBUTES : \n"

        print "Different JOB ATTRIBUTES : \n"
        for attr in job_attributes:
            if attr not in SUB_FOLDER_attributes:
                if attr not in SMART_FOLDER_attributes:
                    print attr + "\n"

        print "Different SUB_FOLDER ATTRIBUTES : \n"
        for attr in SUB_FOLDER_attributes:
            if attr not in job_attributes:
                if attr not in SMART_FOLDER_attributes:
                    print attr + "\n"

        print "Different SMART_FOLDER ATTRIBUTES : \n"
        for attr in SMART_FOLDER_attributes:
            if attr not in job_attributes:
                if attr not in SUB_FOLDER_attributes:
                    print attr + "\n"
        
        i=0
        print "Same ATTRIBUTES : \n"
        for attr in SUB_FOLDER_attributes:
            if attr in (job_attributes and SMART_FOLDER_attributes):
                i = i+1
                print attr + "\n"
        print "TOTAL : " + str(i)
        #et.write('output.xml')

    def create(slef):
    	DEFTABLE = ET.Element('DEFTABLE')
    	comment = Comment('Generated for ATOS DEV TEAM')
        DEFTABLE.append(comment)
    	DEFTABLE.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
        DEFTABLE.attrib["xsi:noNamespaceSchemaLocation"] = "Folder.xsd"

        SMART_FOLDER = ET.SubElement(DEFTABLE, 'SMART_FOLDER')
        SMART_FOLDER.attrib["JOBISN"] = "AAAAAA"
        SMART_FOLDER.attrib["APPLICATION"] = "AAAAAA"
        SMART_FOLDER.attrib["SUB_APPLICATION"] = "AAAAAA"
        SMART_FOLDER.attrib["JOBNAME"] = "AAAAAA"
        SMART_FOLDER.attrib["JOB"] = "AAAAAA"
        
        SUB_FOLDER_1 = ET.SubElement(SMART_FOLDER, 'SUB_FOLDER')
        SUB_FOLDER_1.attrib["JOBISN"] = "AAAAAA"
        SUB_FOLDER_1.attrib["APPLICATION"] = "AAAAAA"
        SUB_FOLDER_1.attrib["SUB_APPLICATION"] = "AAAAAA"
        SUB_FOLDER_1.attrib["JOBNAME"] = "AAAAAA"
        SUB_FOLDER_1.attrib["JOB"] = "AAAAAA"

        JOB_1 = ET.SubElement(SUB_FOLDER_1, 'JOB')
        JOB_1.attrib["JOBISN"] = "AAAAAA"
        JOB_1.attrib["APPLICATION"] = "AAAAAA"
        JOB_1.attrib["SUB_APPLICATION"] = "AAAAAA"
        JOB_1.attrib["JOBNAME"] = "AAAAAA"
        JOB_1.attrib["JOB"] = "AAAAAA"

        JOB_2 = ET.Element('JOB')
        JOB_2.attrib["JOBISN"] = "AAAAAA"
        JOB_2.attrib["APPLICATION"] = "AAAAAA"
        JOB_2.attrib["SUB_APPLICATION"] = "AAAAAA"
        JOB_2.attrib["JOBNAME"] = "AAAAAA"
        JOB_2.attrib["JOB"] = "AAAAAA"
        
        SUB_FOLDER_1.insert(1, JOB_2)

        et = minidom.parseString(ET.tostring(DEFTABLE, encoding="us-ascii", method="xml")).toprettyxml(indent="   ")
        XML_File= open('output.xml',"w")
        XML_File.write(et)
        XML_File.close()

        top = Element('top')

        comment = Comment('Generated for PyMOTW')
        top.append(comment)

        child = SubElement(top, 'child')
        child.text = 'This child contains text.'

        child_with_tail = SubElement(top, 'child_with_tail')
        child_with_tail.text = 'This child has regular text.'
        child_with_tail.tail = 'And "tail" text.'

        child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
        child_with_entity_ref.text = 'This & that'
        
        all = minidom.parseString(ET.tostring(top)).toprettyxml(indent="   ")
        print all

if __name__ == '__main__':
    xmlparse = XMLPARSE()
    xmlparse.parse("ZXXX00Q01_smart.xml")
    #xmlparse.create()
