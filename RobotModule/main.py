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

left = Motor(Port.A)
right = Motor(Port.D)

robot = DriveBase(left, right, 56, 114)

#Go forward for three seconds
#speed 500 mm/s - forward speed
#steering 0 deg/s - Turn rate of the robot
#time 2000 ms - duration
robot.drive_time(500, 0, 1000)
#Stop.COAST - Resistance is low
robot.stop(stop_type = Stop.COAST)
wait(1000)

robot.drive_time(500, 0, 1000)
#Stop.BRAKE - Resistance is medium
robot.stop(stop_type = Stop.BRAKE)
wait(1000)

robot.drive_time(500, 0, 1000)
#Stop.HOLD - Resistance is high
robot.stop(stop_type = Stop.HOLD)
wait(1000)