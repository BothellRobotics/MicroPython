#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
motorA = Motor(Port.A)
motorC = Motor(Port.C)
robot = DriveBase(motorA, motorC, 56, 114)
gs = GyroSensor(Port.S4)
x = 0

while x < 4 :
    
    robot.drive_time(500, 0, 2000)

    motorA.run(250)
    motorC.run(-250)

    gs.reset_angle(0)

    while gs.angle() >= -75:
        wait(50)
        print("Gyro Angle :", gs.angle())

        
        if gs.angle() <= -75:
            robot.stop(Stop.BRAKE)
            
    robot.stop(Stop.BRAKE)

    x = x+1

brick.sound.beep()
