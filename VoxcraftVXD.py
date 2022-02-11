import numpy as np
from lxml import etree
import os

class VXD:

    def __init__(self):
        root = etree.XML("<VXD></VXD>")
        self.tree = etree.ElementTree(root)
    
    def set_tags(self, RecordVoxel=1, RecordLink=0, RecordFixedVoxels=1, RecordStepSize=100):
        root = self.tree.getroot()

        history = etree.SubElement(root, "RecordHistory")
        history.set('replace', 'VXA.Simulator.RecordHistory')
        etree.SubElement(history, "RecordStepSize").text = str(RecordStepSize) #Capture image every 100 time steps
        etree.SubElement(history, "RecordVoxel").text = str(RecordVoxel) # Add voxels to the visualization
        etree.SubElement(history, "RecordLink").text = str(RecordLink) # Add links to the visualization
        etree.SubElement(history, "RecordFixedVoxels").text = str(RecordFixedVoxels) 

    def set_data(self, data):
        root = self.tree.getroot()

        X_Voxels, Y_Voxels, Z_Voxels  = data.shape
        body_flatten = np.zeros((X_Voxels*Y_Voxels, Z_Voxels),dtype=np.int8)
        for i in range(Z_Voxels):
            body_flatten[:,i] = data[:,:,i].flatten()
        
        structure = etree.SubElement(root, "Structure")
        structure.set('replace', 'VXA.VXC.Structure')
        structure.set('Compression', 'ASCII_READABLE')

        etree.SubElement(structure, "X_Voxels").text = str(X_Voxels)
        etree.SubElement(structure, "Y_Voxels").text = str(Y_Voxels)
        etree.SubElement(structure, "Z_Voxels").text = str(Z_Voxels)

        # set body data
        data_tag = etree.SubElement(structure, "Data")
        for i in range(Z_Voxels):
            string = "".join([f"{c}" for c in body_flatten[:,i]])
            etree.SubElement(data_tag, "Layer").text = etree.CDATA(string)

    def write(self, filename='robot.vxd'):
        with open(filename, 'w+') as f:
            f.write(etree.tostring(self.tree, encoding="unicode", pretty_print=True))    