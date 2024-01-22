import numpy as np

from VoxcraftVXA import VXA
from VoxcraftVXD import VXD

np.random.seed(100)

# Generate a Base VXA file
# See here for list of vxa tags: https://gpuvoxels.readthedocs.io/en/docs/
vxa = VXA(EnableExpansion=1, VaryTempEnabled=1, TempAmplitude=20, TempPeriod=0.1, SimTime=5) # pass vxa tags in here

# Create a material
mat1 = vxa.add_material(RGBA=(255,0,255), E=5e4, RHO=1e4, CTE=0.01) # returns the material ID

# Write out the vxa to data/ directory
vxa.write("data/base.vxa")

# Create quadruped
body = np.zeros(shape=(6,6,5))
for z in range(body.shape[2]):
    if z<2:
        body[:2,:2,z]=mat1
        body[:2,4:,z]=mat1
        body[4:,0:2,z]=mat1
        body[4:,4:,z]=mat1
    else:
        body[:,:,z]=mat1

# Add phase offsets (same shape as body) of values between 0-1 (phase offset between actuations)

# Define neural network weights of size (5,1)
numInputs = 5
numOutputs = 1
weights = np.random.uniform(-1,1,numInputs*numOutputs) # TODO: ensure the weights are in the corrent range [-1,1]

# Generate a VXD file
vxd = VXD()
vxd.set_tags(RecordVoxel=1) # pass vxd tags in here to overwite vxa tags
vxd.set_data(body, controller_age=0, controller_weights=weights)
# Write out the vxd to data/
vxd.write("data/robot1.vxd")