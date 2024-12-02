#15.1

import multiprocessing
import random
import time
from datetime import datetime

def task():
    #gets the random time between 0 and 1
    ran_time = random.uniform(0,1)
    time.sleep(ran_time)

    #prints the processes and times into the terminal
    print(f"Process {multiprocessing.current_process().name}: Current time is {datetime.now().strftime('%H:%M:%S')}")


if __name__ == "__main__":
    processes = []

    #runs the 3 processes
    for i in range(3):
        process = multiprocessing.Process(target=task, name=f"Process-{i+1}")
        processes.append(process)
        process.start()

    #ensures all processes are completed before ending
    for process in processes:
        process.join()