import multiprocessing
import time

class Process(multiprocessing.Process):
    def __init__(self, name, target, args):
        super().__init__()
        self.name = name
        self.target = target
        self.args = args

    def run(self):
        print(f'Starting {self.name}')
        self.target(*self.args)
        print(f'Exiting {self.name}')
              
if __name__ == '__main__':
    p = Process('p1', time.sleep, (5,))
    p.start()
    p.join()
    print('Done')
    p = Process('p2', time.sleep, (5,))
    p.start()
    p.join()
    print('Done')