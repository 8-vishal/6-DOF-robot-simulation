import pybullet as sim
import time
import math


pc = sim.connect(sim.GUI)
sim.setGravity(0, 0, -9.8)
sim.setRealTimeSimulation(True, pc)

path = "path to your URDF file"

armID = sim.loadURDF(path, basePosition=[0, 0, 0], useFixedBase=True)
joints = sim.getNumJoints(armID)
print(joints)

sim.setJointMotorControlArray(armID, range(6), sim.POSITION_CONTROL, [0] * 6)
time.sleep(1)
sim.setJointMotorControl2(armID, 1, sim.POSITION_CONTROL, 120*math.pi/180)
time.sleep(1)
