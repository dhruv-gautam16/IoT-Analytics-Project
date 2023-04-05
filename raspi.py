import requests
import urllib3
import RPi.GPIO as GPIO
import time
http = urllib3.PoolManager()

channel = 21

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


if __name__ == '__main__':
    msg=requests.get("https://api.thingspeak.com/channels/2015574/fields/1.json?results=2")
    msg=msg.json()['feeds'][-1]['field1']
    print(msg)
    temp=int(msg)
    if temp==1:
        motor_on(channel)
    else:
        motor_off(channel)
    GPIO.cleanup()

    