from threading import Thread
counter = 0
rounds = 100000

class Counter(Thread):

    def run(self):
        global counter
        global rounds
        for i in range(rounds):
            counter += 1

if __name__ == '__main__':

    for i in range(2):
        th = Counter()
        th.start()
        th.join()

    print(counter)













