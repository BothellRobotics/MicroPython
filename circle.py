#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

motorA = Motor(Port.A)
motorC = Motor(Port.C)
robot = DriveBase(motorA, motorC, 56, 114)
gs = GyroSensor(Port.S4)

def circle(rotations = 1, direction = -1, speedOut = 500, speedIn = 150):
    motorA.run(speedOut)
    motorC.run(speedIn)

    deg = (rotations * 360 * direction) - (20 * direction)

    gs.reset_angle(0)

    while gs.angle() >= deg:
        wait(50)
        print("Gyro Angle :", gs.angle())

        if gs.angle() <= deg:
            robot.stop(Stop.BRAKE)

    robot.stop(Stop.BRAKE)

circle()
  
