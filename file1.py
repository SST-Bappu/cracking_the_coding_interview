from collections import deque

tasks = [['t1',8],['t2',4],['t3',9]]

def round_robin_scheduler(tasks):
    queue = deque(tasks)
    completed = []
    t = 0
    quantum = 3
    while queue:
        task, time = queue.popleft()
        t+=quantum if (time-quantum)>0 else time
        time-=quantum
        if time>0:
            queue.append([task, time])
        else:
            completed.append([task, t])

    return completed


def generator_imp(tasks):
    for task in tasks:
        yield task


caller = generator_imp(tasks)

for call in caller:
    print(call)
    
    