from collections import deque
queue = deque(["Ali","zahra","dania","rana"])
queue.append("NewBaby")
queue.append("New")
s=queue.popleft()
print(s)