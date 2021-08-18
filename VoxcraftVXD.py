import numpy as np
from lxml import etree
import os

class VXD:

    def __init__(self):
        root = etree.XML("<VXD></VXD>")
        self.tree = etree.ElementTree(root)

    def write(self, filename='robot.vxd'):
        os.makedirs('data', exist_ok=True)
        
        with open('data/{}'.format(filename), 'w+') as f:
            f.write(etree.tostring(self.tree, encoding="unicode", pretty_print=True))    