def clamp(vmin,v,vmax):
    return max(vmin,min(v,vmax))

def main():
    import sys
    import time 

    from botlib.bot import Bot
    from readchar import readkey, key

    bot = Bot()
    STEP_POWER, STEP_STEER= 10, 0.25
    power, steer = 0, 0.0
    running = True

    print('calibrating...')
    bot.calibrate()

    while running:
        inp = readkey()
        if inp == 's':
            print('driving forward...')
            bot.drive_power(80)
        if inp == 'd':
            print('simulate other car...')
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
        if inp == key.SPACE:
            print('stop...')
            bot.stop_all()
            running = False

if __name__ == '__main__':
    main()
