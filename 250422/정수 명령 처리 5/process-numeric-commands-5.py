N = int(input())

li = []
command = None
num = 0

for _ in range(N):
    line = input().split()
    command = line[0]
    if line[0] == "push_back" or line[0] == "get":
        num = int(line[1])
    if command == "push_back":
        li.append(num)
    elif command == "pop_back":
        li.pop()
    elif command == "size":
        print(len(li))
    elif command == "get":
        print(li[num-1])
# Please write your code here.