import sys

def push_front(a,x):
    a.insert(0,x)

def push_back(a,x):
    a.append(x)

def pop_front(a):
    if len(a)==0:
        return -1
    else:
        return a.pop(0)

def pop_back(a):
    if len(a)==0:
        return -1
    else:
        return a.pop(-1)

def size(a):
    return len(a)

def empty(a):
    if len(a)==0:
        return 1
    else:
        return 0

def front(a):
    if len(a)==0:
        return -1
    else:
        return a[0]

def back(a):
    if len(a) == 0:
        return -1
    else:
        return a[-1]

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    a = []
    command = [sys.stdin.readline().rstrip() for x in range(n)]
    for c in command:
        if c.startswith('push_front'):
            push_front(a,c.split()[1])
        elif c.startswith('push_back'):
            push_back(a,c.split()[1])
        elif c == 'pop_front':
            print(pop_front(a))
        elif c == 'pop_back':
            print(pop_back(a))
        elif c == 'size':
            print(size(a))
        elif c == 'empty':
            print(empty(a))
        elif c == 'front':
            print(front(a))
        elif c == 'back':
            print(back(a))




