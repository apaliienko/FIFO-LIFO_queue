from random import random
from math import log, pow

typeofqueue = -1            # -1 = LIFO, 0 = FIFO
actualtime = 10             # actual time(0-10) of completing tasks
count, maxcount = 1, 10000  # count of tasks
intensity = 0.9             # intensity of task's appearance
service = 1.0               # service time of one task


def tnext():
    # arrival time of new task
    tnext = -log(random()) / intensity
    return tnext


if typeofqueue == 0:
    lettertype = 'F'
else:
    typeofqueue = -1
    lettertype = 'L'

print("----------{}IFO---------".format(lettertype))
timeinsystem, queue = [], []
tin, t = 0.0, 0.0
queue.append(tin)

while count <= maxcount:
    if len(queue) > 0:
        tin = queue.pop(typeofqueue)
        count += 1
        tend = t + tin + service
    tnex = tin + tnext()
    queue.append(tnex)
    if tend > tnex:
        t = tend - tnex
    else:
        t = 0.0
    timeinsystem.append(tend - tin)

average = sum(timeinsystem) / len(timeinsystem)
print("Average time in system -", average)

dispersion = sum([pow(tasktime - average, 2) for tasktime in timeinsystem]) / len(timeinsystem)
print("Dispersion of average time -", dispersion)

count_actual = len([actual for actual in timeinsystem if actual <= actualtime])
print("Relevance indicator - {}/{}".format(count_actual, maxcount))
