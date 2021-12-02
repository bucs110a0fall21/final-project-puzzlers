import time


class Timer:
    def __init__(self):
        self.timeLoop = True

    def timer(self):
        sec = 0
        min = 0
        while self.timeLoop == True:
            sec += 1
            time.sleep(1)
            if sec == 60:
                sec = 0
                min += 1


