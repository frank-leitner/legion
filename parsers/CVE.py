#!/usr/bin/python

import sys
import xml.dom.minidom

class CVE:
    name = ''
    product = ''
    version = ''
    url = ''
    source = ''
    severity = ''
    exploitId = ''
    exploit = ''
    exploitUrl = ''

    def __init__(self, cveData):
        self.name = cveData['id']
        self.product = cveData['product']
        self.version = cveData['version']
        self.url = cveData['url']
        self.source = cveData['source']
        self.severity = cveData['severity']
        self.exploitId = cveData['exploitId']
        self.exploit = cveData['exploit']
        self.exploitUrl = cveData['exploitUrl']
