from microbit import *
import utime

while True:
    pin8.write_digital(0)
    display.scroll("GO")

    pin8.write_digital(1)
    t0 = utime.ticks_us()

    for i in range(102):
        u = pin0.read_analog()
        if u > .63 * 1023:
            t1 = utime.ticks_us()
            break
        else:
            t1 = t0

    tau = utime.ticks_diff(t1, t0)
    if tau == 0:
        display.scroll("0")
    else:
        display.show(tau)
    pin8.write_digital(0)
    sleep(2000)