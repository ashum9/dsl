class Node:
    def __init__(self, customer_id, call_time):
        self.customer_id = customer_id
        self.call_time = call_time
        self.next = None

class CallCenterQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def add_call(self, customer_id, call_time):
        new_node = Node(customer_id, call_time)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Call from Customer {customer_id} added (Duration: {call_time} mins)")

    def process_call(self):
        if not self.front:
            print("No calls in queue.")
            return
        print(f"Processing call from Customer {self.front.customer_id} (Duration: {self.front.call_time} mins)")
        self.front = self.front.next
        if not self.front:
            self.rear = None

    def display_calls(self):
        if not self.front:
            print("No pending calls.")
            return
        current = self.front
        print("\nPending Calls:")
        while current:
            print(f"Customer ID: {current.customer_id}, Call Time: {current.call_time} mins")
            current = current.next

def main():
    queue = CallCenterQueue()
    while True:
        print("\n1. Add Call")
        print("2. Process Call")
        print("3. Display Calls")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_id = input("Enter Customer ID: ")
            call_time = int(input("Enter Call Time (in minutes): "))
            queue.add_call(customer_id, call_time)
        elif choice == '2':
            queue.process_call()
        elif choice == '3':
            queue.display_calls()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
