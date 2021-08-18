import numpy as np
from lxml import etree
import os

class VXD:

    def __init__(self, RecordVoxel=1, RecordLink=0, RecordFixedVoxels=1, RecordStepSize=100):
        root = etree.XML("<VXD></VXD>")
        self.tree = etree.ElementTree(root)

        self.set_history_tags()
    
    def set_history_tags(self):
        root = self.tree.getroot()

        history = etree.SubElement(root, "RecordHistory")
        history.set('replace', 'VXA.Simulator.RecordHistory')
        etree.SubElement(history, "RecordStepSize").text = str(RecordStepSize)
        etree.SubElement(history, "RecordVoxel").text = str(RecordVoxel)
        etree.SubElement(history, "RecordLink").text = str(RecordLink) 
        etree.SubElement(history, "RecordFixedVoxels").text = str(RecordFixedVoxels) 

    def set_data(self, data):
        #TODO: takes 3D np array and sets data by overwriting the VXA
        pass

    def write(self, filename='robot.vxd'):
        os.makedirs('data', exist_ok=True)
        
        with open('data/{}'.format(filename), 'w+') as f:
            f.write(etree.tostring(self.tree, encoding="unicode", pretty_print=True))    