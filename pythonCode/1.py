import pybullet as sim
import time


pc = sim.connect(sim.GUI)
sim.setGravity(0, 0, -9.8)

path = "path to your URDF file"

armID = sim.loadURDF(path, basePosition=[0, 0, 0], useFixedBase=True)

while pc != 0:
  sim.stepSimulation()
  time.sleep(0.01)
