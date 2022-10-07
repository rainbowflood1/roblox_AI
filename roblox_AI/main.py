import random
import mouse
import time
#import subprocess
#import main

#subprocess.call("arrows.vbs", shell=True)

while True:
    x = random.randint(-1920,1920)
    print(x)

    y = random.randint(-1080,1080)
    print(y)

    d = random.randint(0,5)
    print(d)

    mouse.move(x, y, absolute=False, duration=d)

    mouse.click('right')

    time.sleep(d)