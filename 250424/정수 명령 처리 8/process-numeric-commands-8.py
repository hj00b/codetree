N = int(input())
command = []
A = []
num = 0

for _ in range(N):
    line = input().split()
    command = line[0]
    if line[0] in ["push_front", "push_back"]:
        num = int(line[1])
    
    if command =="push_front":
        A = [num] + A
    elif command =="push_back":
        A.append(num)
    elif command =="pop_front":
        print(A.pop(0))
    elif command =="pop_back":
        print(A.pop(-1))
    elif command =="size":
        print(len(A))
    elif command =="empty":
        if A:
            print(0)
        else:
            print(1)
    elif command =="front":
        print(A[0])
    elif command =="back":
        print(A[-1])
# Please write your code here.
