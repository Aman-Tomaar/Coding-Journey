# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                 Good for I/O bound tasks like reading files or fetching data from APIs
#                 threading.Thread(target=my_function, args=(if any arguments required and use this as a tuple so if only one argument use , after it))

import threading as th
import time


def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")


def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail(place):
    time.sleep(4)
    print(f"You get the mail from {place}")


chore1 = th.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = th.Thread(target=take_out_trash)
chore2.start()

chore3 = th.Thread(
    target=get_mail, args=("MailBox",)
)  # Need to use the , if only one element in tuple
chore3.start()

chore1.join()  # if we dont use .join() it will not wait until all these are over and print the nxt code before it
chore2.join()
chore3.join()

print("All Chores are Complete!!")
