import time

class Timer:    

    def __init__(self, label):
        self.label = label

    def __enter__(self):
        print '{}...'.format(self.label)
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        print '{} time: {} s'.format(self.label, round(self.interval, 3))
