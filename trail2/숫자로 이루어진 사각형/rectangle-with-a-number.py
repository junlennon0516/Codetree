n = int(input())

# Please write your code here.
def square(N):
    i=1
    for _ in range(N):
        for k in range(N):
            print(i, end=" ")
            if i < 9:
                i=i+1
            else:
                i=1
        print("")

square(n)