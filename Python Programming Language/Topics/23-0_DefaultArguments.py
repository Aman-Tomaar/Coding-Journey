import time


def count(end, start=0, step=1):
    for i in range(start, end + 1, step):
        print(i)
        time.sleep(1)
    print("Done!")


count(2)
