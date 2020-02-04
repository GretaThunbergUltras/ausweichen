def main():
    ##import Library
    import sys
    import time
    import ctypes
    import pigpio

    ##create new instance for bot, readchar and ultra
    from botlib.bot import Bot
    from readchar import readkey, key
    from ultra import Sonic

    bot = Bot()
    sonic = Sonic()
    
    ##set parameter for while loops
    running = True
    checkdistance = False
    
    ##calibrate bot
    print('calibrating...')
    bot.calibrate()
    
    ##while loop for main programm
    while running:
        inp = readkey()
        if inp == 's':
            checkdistance = True        
            while checkdistance:
                distance = sonic.getDistance()
                ##if any distance < 50 start avoid sequence 
                if distance[0] < 50 or distance[1] < 50:
                    #avoid to the rigth side
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
                ##if not obstacle in the way drive forward
                else:
                    bot.drive_power(30)
        inp = readkey()
        ##if Space is spressed stop the while loop and stop all movement
        if inp == key.SPACE:
            print('stop...')
            bot.stop_all()
            running = False

if __name__ == '__main__':
    main()
