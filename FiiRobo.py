#! /usr/bin/env python

import time
import Adafruit_PCA9685

def m_deg(deg):
    pulse = int((650-150)*deg/180+150)
    return pulse

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

RightHand = 0
RightLeg = 1
LeftHand = 2
LeftLeg = 3

pwm.set_pwm(RightHand, 0, m_deg(90))
pwm.set_pwm(RightLeg, 0, m_deg(90))
pwm.set_pwm(LeftHand, 0, m_deg(90))
pwm.set_pwm(LeftLeg, 0, m_deg(90))
time.sleep(1)

while True:
    pwm.set_pwm(RightHand, 0, m_deg(110))
    pwm.set_pwm(LeftHand, 0, m_deg(60))
    pwm.set_pwm(RightLeg, 0, m_deg(110))
    pwm.set_pwm(LeftLeg, 0, m_deg(60))
    time.sleep(0.1)
    
    pwm.set_pwm(RightHand, 0, m_deg(60))
    pwm.set_pwm(LeftHand, 0, m_deg(110))
    pwm.set_pwm(RightLeg, 0, m_deg(60))
    pwm.set_pwm(LeftLeg, 0, m_deg(110))
    time.sleep(0.1)
