#!/usr/bin/env python
# coding: utf-8
#Developer: Devesh Waingankar
#Iterating over XML file

import os
import re
from collections import Counter
import xml.etree.ElementTree as ET

tree = ET.parse('/apps/python/data/InCommon-metadata.xml')
root = tree.getroot()
del_cmd = '''rm -rf /apps/python/data/xml_data.xlsx'''
#os.system(del_cmd)


csvfile = "/apps/python/data/xml_analysis_ready.csv"

name_list = []
print(name_list)
unique_name_count = {}
for child_node in range(2,len(root.getchildren())):
        saml_list = []
        new_rows = " "
        req_friendly_name = " "
        req_name = " "
        saml_all = " "
        names_all = " "
        rows_to_write = " "
        name_list = []
        spsso_check = root[child_node][1]
        row_to_write = " "
        if re.search(r'\}(.*)',spsso_check.tag).group(1) == "SPSSODescriptor": #checks for SPSSODescriptor
            entity_id = root[child_node].attrib['entityID'] #returns entity ID
            try:
                for elem in root[child_node][1].iter():
                    if re.search(r'\}(.*)',elem.tag).group(1) == "RequestedAttribute":
                        req_friendly_name = elem.attrib['FriendlyName']
                        name_list.append(req_friendly_name)

            except Exception as e:
                pass

for each in name_list:
    print(each)

flag=0
with open(csvfile, "a") as fp:
    for child_node in range(2,len(root.getchildren())):
        saml_list = []
        new_rows = " "
        req_friendly_name = " "
        req_name = " "
        saml_all = " "
        names_all = " "
        rows_to_write = " "
        name_list = []
        spsso_check = root[child_node][1]
        row_to_write = " "
        if re.search(r'\}(.*)',spsso_check.tag).group(1) == "SPSSODescriptor": #checks for SPSSODescriptor
            entity_id = root[child_node].attrib['entityID'] #returns entity ID
            try:
######################################################################################################
                for elem in root[child_node][1].iter():
                    if re.search(r'\}(.*)',elem.tag).group(1) == "RequestedAttribute":
                        req_friendly_name = elem.attrib['FriendlyName']
                        name_list.append(req_friendly_name)
            except Exception as e:
                pass

            for each in name_list:
                names_all = names_all + "," + each

            row_to_write = entity_id + names_all
            fp.write(row_to_write +"\n")
        else:
            pass
