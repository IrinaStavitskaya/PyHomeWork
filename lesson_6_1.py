from itertools import cycle
import time


class TrafficLight:
    __color = {7: 'red', 2: 'yellow', 5: 'green'}

    def running(self):
        c = 0
        for t, col in cycle(TrafficLight.__color.items()):
            if c > 10:
                break
            print(col)
            time.sleep(t)
            c += 1


a = TrafficLight()
a.running()
