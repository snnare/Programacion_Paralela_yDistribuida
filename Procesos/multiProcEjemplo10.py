#

import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("proceso %s ----> %s" % (name, datetime.fromtimestamp(now)))


def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("proceso %s ----> %s" % (name, datetime.fromtimestamp(now)))


if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='p1-TEST WITH BARRIER', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p2-TEST WITH BARRIER', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p3-TEST WITHOUT BARRIER', target=test_without_barrier).start()
    Process(name='p4-TEST WITHOUT BARRIER', target=test_without_barrier).start()

