#!/usr/bin/env python
# coding: utf-8
# Developer: Devesh Waingankar
# In[7]:


import os
import pandas as pd
from lxml import etree


# In[8]:

#Read in a CSV to be converted into XML
data = pd.read_csv('''/apps/python/data/modo/Modo.csv''', encoding = "ISO-8859-1")


f = open('/apps/python/data/modo/ModoOutput.xml', 'wb')
root = etree.Element('recipients')
for index,row in data.iterrows():

    recipient = etree.Element('recipient')
    root.append(recipient)
    recipient.set('id', row['RECIPIENT_ID'])

    name = etree.Element('name')
    name.text = row['NAME']
    recipient.append(name)

    email = etree.Element('email')
    email.text = row['EMAIL_ADDR']
    recipient.append(email)

    attributes = etree.Element('attributes')
    recipient.append(attributes)

    string_attributes_id = etree.Element('stringAttribute')
    attributes.append(string_attributes_id)
    string_attributes_id.set('id', 'identifier')

    value_id = etree.Element('value')
    value_id.text = row['FSUID']
    string_attributes_id.append(value_id)


    string_attributes_emplid = etree.Element('stringAttribute')
    string_attributes_emplid.set('id', 'emplid')
    attributes.append(string_attributes_emplid)

    value_emplid = etree.Element('value')
    value_emplid.text = str(row['EMPLID'])
    string_attributes_emplid.append(value_emplid)

    array_attrib_group = etree.Element('arrayAttribute')
    array_attrib_group.set('id', 'groups')
    attributes.append(array_attrib_group)

    groups = row['GROUP'].split('|')
    for each in range(0,len(groups)):
        value_group = etree.Element('value')
        value_group.text = groups[each]
        array_attrib_group.append(value_group)

    array_attrib_affl = etree.Element('arrayAttribute')
    array_attrib_affl.set('id', 'affiliations')
    attributes.append(array_attrib_affl)

    affl_count = row['AFFILIATION'].split('|')
    for each in range(0,len(affl_count)):
        value_affl = etree.Element('value')
        value_affl.text = affl_count[each]
        array_attrib_affl.append(value_affl)

s = etree.tostring(root,pretty_print=True, encoding="us-ascii")
f.write(s)
f.close()
