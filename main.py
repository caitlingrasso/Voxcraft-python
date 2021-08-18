import numpy as np

from VoxcraftVXA import VXA
from VoxcraftVXD import VXD

# Generate a Base VXA file
vxa = VXA()

mat1 = vxa.add_material(RGBA=(255,0,255), E=5e4, RHO=1e4)
mat2 = vxa.add_material(RGBA=(255,0,0), E=1e8, RHO=1e4)

vxa.write("base.vxa")

# Create body random body array between 0 and maximum material ID
body = np.random.randint(0,mat2+1,size=(5,5,5))

vxd = VXD()
vxd.set_tags(RecordVoxel=1) 
vxd.set_data(body)
vxd.write("robot1.vxd")