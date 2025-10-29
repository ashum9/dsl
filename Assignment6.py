# A Callcenter recives incoming calls, each call has assigned unique 
# customer id. The calls are answered in order they received . Your task is 
# to simulate the call queue using queue data structure(implement queue using linked list)
# 1. addCall(customer ID , callTime): Add a call to the queue with customer ID and call Time
# 2. answerCall(): Answer the call and remove the first call from queue 
# 3. viewQueue(): View all the calls currently in the queue 
# 4. isQueueEmpty(): Check for the queue is empty
    

import time

class Node:
    def __init__(self, customer_id, call_time):
        self.customer_id = customer_id
        self.call_time = call_time
        self.next = None

class ClassQueue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.customerCounter = 1

    def addCall(self, customer_id=None, call_time=None):
        if customer_id is None:
            customer_id = self.customerCounter
            self.customerCounter += 1
        if call_time is None:
            call_time = time.strftime("%H:%M:%S", time.localtime())

        new_node = Node(customer_id, call_time)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Call added: Customer ID={customer_id}, Time={call_time}")

    def answerCall(self):
        if self.front is None:
            print("No calls to answer. Queue is empty.")
            return

        answered_call = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None

        print(f"Call answered:\nCustomer ID: {answered_call.customer_id}\nCall Time: {answered_call.call_time}")

    def viewQueue(self):
        if self.front is None:
            print("Queue is empty.")
            return

        print("Current Call Queue:")
        temp = self.front
        while temp:
            print(f"Customer ID: {temp.customer_id}, Call Time: {temp.call_time}")
            temp = temp.next

    def isQueueEmpty(self):
        return self.front is None


if __name__ == "__main__":
    c = ClassQueue()

    print("Welcome to the Call Center")
    while True:
        option = input(
            "Enter the number of the operation you want to perform:\n"
            "1. Add Call\n"
            "2. Answer Call\n"
            "3. View Queue\n"
            "4. Is Queue Empty\n"
            "5. Exit\n"
            "Enter option: "
        )
        try:
            option = int(option)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if option == 1:
            c.addCall()
        elif option == 2:
            c.answerCall()
        elif option == 3:
            c.viewQueue()
        elif option == 4:
            print("Is queue empty?", c.isQueueEmpty())
        elif option == 5:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 5.")
