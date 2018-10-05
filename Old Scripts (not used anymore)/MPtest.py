#import multiprocessing
#import TerminalGameUsbDetector
#import TerminalGameLauncher

#if __name__ == "__main__":
#    TransferValue = multiprocessing.Value('i',0)

#    p1 = multiprocessing.process(target=TerminalGameLauncher.TitleScreen, args=(TransferValue))
#    p2 = multiprocessing.process(target=TerminalGameUsbDetector.UsbMonitor, args=(TransferValue))

#    p1.start()
#    p2.start()

#    p1.join()
#    p2.join()

#    print(TransferValue)

import threading,time,random,queue
import TerminalGameUsbDetector, TerminalGameLauncher

def test1():
    while True:
        print("a")

def test2():
    #for i in range(5):
    #    print("b")
    while True:
        print("b")

def handle_script_a(q):
    TerminalGameLauncher.TitleScreen(q)

def handle_script_b(q):
    TerminalGameUsbDetector.UsbMonitor(q)

if __name__ == "__main__":
    q = queue.Queue()
    q.put(1)
    Tgame = threading.Thread(target=handle_script_a,args=(q,))
    Tdetector = threading.Thread(target=handle_script_b,args=(q,))
    Tdetector.daemon = True
    Tdetector.start()
    Tgame.start()
    Tgame.join()
    Tdetector.join()





