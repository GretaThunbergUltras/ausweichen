def main():
    import sys
    import time
    import ctypes
    import pigpio
    ##import cv2 as cv

    from botlib.bot import Bot
    from readchar import readkey, key
    from ultra import Sonic

    bot = Bot()
    STEP_POWER, STEP_STEER= 10, 0.25
    power, steer = 0, 0.0
    running = True
    checkdistance = False
    objectsafe = 0

    print('calibrating...')
    bot.calibrate()

    while running:
        inp = readkey()
        if inp = 's':
            checkdistance = True        
            while checkdistance:
                if distance[0] < 30 or distance[1] < 30: 
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
                    while distance[0] < 50 or distance[1] 50:
                        print('move object out of the way')
                    bot.drive_power(50)
                if key = 't':
                    checkdistance=False
                    
        if inp == key.SPACE:
            print('stop...')
            bot.stop_all()
            running = False

if __name__ == '__main__':
    main()