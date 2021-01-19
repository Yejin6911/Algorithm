import sys

def push(a,x):
    a.append(x)

def pop(a):
    if len(a)==0:
        top = -1
    else:
        top = a[-1]
        del a[-1]
    return top

def size(a):
    return len(a)

def empty(a):
    if len(a)==0:
        return 1
    else:
        return 0

def top(a):
    if len(a)==0:
        return -1
    else:
        return a[-1]

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    a = []
    command = [sys.stdin.readline().rstrip() for x in range(n)]
    for c in command:
        if c.startswith('push'):
            push(a,c.split()[1])
        elif c == 'pop':
            print(pop(a))
        elif c == 'size':
            print(size(a))
        elif c == 'empty':
            print(empty(a))
        elif c == 'top':
            print(top(a))


