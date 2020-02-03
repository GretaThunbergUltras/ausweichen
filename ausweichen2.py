def main():
    import sys
    import time
    import ctypes
    import cv2 as cv

    from botlib.bot import Bot
    from readchar import readkey, key
    from ultra import Sonic

    sonic=Sonic()
    bot = Bot()
    __init__()
    STEP_POWER, STEP_STEER= 10, 0.25
    power, steer = 0, 0.0
    running = True
    objectsafe = 0

    print('calibrating...')
    bot.calibrate()

    while running:
        objects = bot.detectObject("../classifer/cascade.xml")
        inp = readkey()
        distance = sonic.getDistance()

        ret, frame = bot.getCap().read()
        if distance[1] < 30 or distance[2] < 30: 
            if len(objects) or objectsafe == 1:
                print('object detected...')
                bot.drive_power(0)
                time.sleep(0.5)
                bot.drive_steer(1.)
                bot.drive_power(60)
                time.sleep(0.4)
                bot.drive_power(0)
                bot.drive_steer(-1.0)
                bot.drive_power(60)
                time.sleep(1.4)
                bot.drive_power(0)
                bot.drive_steer(1.0)
                bot.drive_power(60)
                time.sleep(0.4)
                bot.drive_steer(0)
                time.sleep(1)
                bot.drive_power(0)
            else:
                bot.drive_power(0)
                print('no other bot detected...')
                print('waiting for free path...')
                    if distance[1] > 50  or distance[2] > 50:
                        bot.drive_power(80)
                    else:
                        print('move object out of the way...')
        
        if inp == 'o':
            if objectsafe == 0:
                objectsafe = 1
            else:
                objectsafe = 0
                    
        if inp == key.SPACE:
            print('stop...')
            bot.stop_all()
            running = False

if __name__ == '__main__':
    main()