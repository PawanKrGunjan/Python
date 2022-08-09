import datetime
def time_delta(t1, t2):
    Format = "%a %d %b %Y %H:%M:%S %z"
    T1 = datetime.datetime.strptime(str(t1), Format)
    T2 = datetime.datetime.strptime(str(t2), Format)
    delta = T2-T1
    return int(abs(delta.total_seconds()))

if __name__ == '__main__':
<<<<<<< HEAD
    print("Input format : Sun 10 May 2015 13:54:36 -0700")
    t1 = input()
    t2 = input()
    print(time_delta(t1, t2))
=======
    n = int(input())
    for t_itr in range(n):
        t1 = input()
        t2 = input()
        print(time_delta(t1, t2))
>>>>>>> ddc3205baf481bfbbcf6e90e7b6dc8cf69e93fcd
