#!/usr/bin/env python

import sys
import urllib2
import xmltodict

def main(user, t1=None, t2=None):
    xml_file = "http://www.openstreetmap.org/api/0.6/changesets?display_name={}".format(user)
    if t1:
        xml_file += "&time={}".format(t1)
    if t2:
        xml_file += ",{}".format(t2)
    
    changesets = parse_changesets(xml_file)
    print('Number of changesets: {}'.format(len(changesets)))

    nedits = 0
    for changeset in changesets:
        nedits += parse_changeset(changeset)
    print('Number of changes: {}'.format(nedits))
    
    return 0

def parse_changesets(xml_file):
    changesets = []

    data = parse_xml(xml_file)
    for item in data['osm']['changeset']:
        changesets.append(item['@id'])
    
    return changesets

def parse_changeset(changeset):
    xml_file = "http://www.openstreetmap.org/api/0.6/changeset/{}/download".format(changeset)

    data = parse_xml(xml_file)
    
    nedits = 0
    for item in ('create', 'modify', 'delete'):
        if item not in data['osmChange'].keys():
            continue
        for subitem in data['osmChange'][item]:
            nedits += 1
    
    return nedits
    
def parse_xml(xml_file):
    try:
        fd = urllib2.urlopen(xml_file)
    except urllib2.URLError as e:
        sys.exit(e)
        
    obj = xmltodict.parse(fd.read())
    fd.close()
    
    return obj

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("User not defined")
    user = sys.argv[1]
    t1 = t2 = None
    if len(sys.argv) > 2:
        t1 = sys.argv[2]
    if len(sys.argv) > 3:
        t2 = sys.argv[3]

    sys.exit(main(user, t1, t2))
