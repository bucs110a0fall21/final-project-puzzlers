import time


class Timer:
    def __init__(self):
        """
        when initialized, the timeloop is triggered
        args: self
        returns: none
        """
        self.timeLoop = True
        self.counting_string = ""

    def timer(self):
        """
        acts as a timer when initilized. Counts time in seconds and converts to minutes each time the time reaches 60 seconds
        args: self
        returns: none
        """
        sec = 0
        minu = 0
        while self.timeLoop == True:
            sec += 1
            time.sleep(1)
            if sec == 60:
                sec = 0
                minu += 1
            self.counting_string = "%s:%s" % (minu, sec)


