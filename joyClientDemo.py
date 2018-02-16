import pygame
import requests
import time

pygame.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()
print  (controller.get_name())
print ("Buttons %4d" % (controller.get_numbuttons()))
print ("Hats %4d" % (controller.get_numhats()))

def joyFormat(value):
    value = (value * 100) + 100
    value = int(value)
    return value

while(1):
    joyKeys = ['LV', 'LH', 'RV', 'RH']
    butKeys = ['B1', 'B2', 'B3', 'B4']
    senValues = ['0','0','0','0']
    joyValues = [0,0,0,0] 
    butValues = [0,0,0,0] 
    senIndex = 0
    pygame.event.pump()
    for x in range (0, 4):
        joyValues[x] = controller.get_axis(x)
        joyValues[x] = joyFormat(joyValues[x])
    for x in range (0, 4):
        butValues[x] = controller.get_button(x)
    joyDict = dict(zip(joyKeys, joyValues))
    butDict = dict(zip(butKeys, butValues))
    print(joyDict)
    print(butDict)

    time.sleep(.1)

    payload = joyDict
    status = requests.get('http://10.1.41.10/drive/',params=payload)
    for x in range (0, len(status.text)):
            if status.text[x].isdigit():
               senValues[senIndex] += status.text[x]
            elif status.text[x] == ',':
                senIndex += 1
            elif status.text[x] == 'T':
                break

    for x in range (0, 4):
        print (senValues[x])
        senValues[x] = ""

controller.quit()
pygame.quit()
quit()



