import numpy as np

# TODO: define constants

def AddMaterial(E=10000, RHO=1000, P=0.35, CTE=0, tempPhase=0, uStatic=1, uDynamic=0.8,
                      isSticky=0, isPaceMaker=0, paceMakerPeriod=1.0, hasCilia=0, isBreakable=0,
                      RGBA=None):
    if RGBA is None:
        RGBA = (np.random.randint(256), np.random.randint(256), np.random.randint(256), 255)

    # TODO: write material to VXA

def AddVoxel():
    pass

def WriteVXA():
    pass

def WriteVXD():
    # pass in params (materialID?)
    pass 

    # TODO: creates VXD to overwrite VXA params 