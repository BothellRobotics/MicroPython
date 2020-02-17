#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor

# Write your program here
brick.sound.beep()
gs = GyroSensor(Port.S3)
motorA = Motor(Port.A)
motorD = Motor(Port.D)
robot = DriveBase(motorA, motorD, 56, 114)

#Go forward for one seconds
#speed 500 mm/s - forward speed
#steering 0 deg/s - Turn rate of the robot
#time 1000 ms - duration
robot.drive_time(500, 0, 1000)
robot.stop(Stop.BRAKE)
wait(500)

#Reset Gyro Sensor angle  to zero
gs.reset_angle(0)

print("Gyro Angle :", gs.angle())

#Run motor A at 30 degrees per second
motorA.run(300)
motorD.run(-300)

#wait(5000)

while gs.angle() <= 80:
    wait(50)
    
robot.stop(Stop.BRAKE)

print("Gyro Angle :", gs.angle())
