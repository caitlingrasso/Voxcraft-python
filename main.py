from VoxcraftVXA import VXA
from VoxcraftVXD import VXD

vxa = VXA()
vxa.add_material(RGBA=(255,0,0))
vxa.write()

vxd = VXD()
vxd.set_history_tags()
vxd.write()