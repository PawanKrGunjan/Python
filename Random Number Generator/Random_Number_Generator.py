from time import time

def randomNumber(Min, Max, N):
    def time_random():
        return time() - float(str(time()).split('.')[0])

    def gen_random_range(min, max):
        return int(time_random() * (max - min) + min)
    x=[]
    y=[]
    for i in range(N):
        for j in range(N**5):
            time_random()
        x.append(i)
        y.append(gen_random_range(min,max))
    return f"x :{x} \ny:{y}"

min = int(input("Enter the first number:"))
max= int(input("Enter the second number:"))
N = int(input("Random number required: "))
print(randomNumber(min, max, N))
