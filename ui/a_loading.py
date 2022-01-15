import itertools
import threading
import time
import sys



class load:

    def loading(self):
        done = False

        def eza_reza():
            for eza in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rMemperoses data ' + eza)
                sys.stdout.flush()
                time.sleep(0.1)

        t = threading.Thread(target=eza_reza)
        t.start()

        time.sleep(3)
        done = True
