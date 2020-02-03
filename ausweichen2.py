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
    sonic = Sonic()
    STEP_POWER, STEP_STEER= 10, 0.25
    power, steer = 0, 0.0
    running = True
    checkdistance = False
    wait = True
    objectsafe = 0
    

    print('calibrating...')
    bot.calibrate()

    while running:
        inp = readkey()
        if inp == 's':
            checkdistance = True        
            while checkdistance:
                distance = sonic.getDistance()
                print(distance)
                if distance[0] < 50 or distance[1] < 50: 
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
                    bot.drive_power(30)
                    ##if distance[0] < 50 or distance[1] > 50:
                        ##wait = true
                    ##while wait:
                        ##distance = sonic.getDistance()
                        ##print('move object out of the way')
                        ##if distance[0] > 50 or distance[1] > 50:
                            ##wait = false
        inp = readkey()            
        if inp == key.SPACE:
            print('stop...')
            bot.stop_all()
            running = False

if __name__ == '__main__':
    main()
