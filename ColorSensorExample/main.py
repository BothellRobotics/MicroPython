#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.robotics import DriveBase
import time

# Write your program here
brick.sound.beep()

motorA = Motor(Port.A)
motorD = Motor(Port.D)
robot = DriveBase(motorA, motorD, 56, 114)
cs = ColorSensor(Port.S4)

#drive speed at 450 mm per second with 0 deg per second turn rate
robot.drive(450, 0)
while cs.color() != Color.YELLOW:
     time.sleep(0.01)

robot.stop(Stop.BRAKE)
