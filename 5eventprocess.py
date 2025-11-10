# Assignment 5

# Implement realtime event processing system using Queue System support following operations:

# 1. Add an event -> new event added to the event Queue
# 2. Process the next event -> process & remove the event that has been in the queue for long
# 3. Display panding events -> show all the events currently waiting
# 4. Cancle the events -> an event can be cancelled if not been process
#         1. event id
#         2. event name
#         3. timestamp


import time

class Event:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.timestamp = time.time()

    def __repr__(self):
        return f"Event(ID: {self.id}, Name: '{self.name}')"

class EventQueue:
    def __init__(self):
        self.events = []
        self.next_id = 1

    def add_event(self, name):
        event = Event(self.next_id, name)
        self.events.append(event)
        self.next_id += 1
        print(f"Event '{event.name}' added with ID {event.id}.")

    def process_next_event(self):
        if not self.events:
            print("Queue is empty. No event to process.")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
            return

        event_to_process = self.events.pop(0)
        processing_time = time.time() - event_to_process.timestamp
        print(f"Processing event: {event_to_process}")
        print(f"Time in queue: {processing_time:.2f} seconds.")

    def display_pending_events(self):
        if not self.events:
            print("Queue is empty. No pending events.")
        else:
            print("--- Pending Events ---")
            for event in self.events:
                print(event)

    def cancel_event(self, event_id_to_cancel):
        event_to_remove = None
        for event in self.events:
            if event.id == event_id_to_cancel:
                event_to_remove = event
                break
        
        if event_to_remove:
            self.events.remove(event_to_remove)
            print(f"Event {event_to_remove} has been cancelled.")
        else:
            print(f"Event with ID {event_id_to_cancel} not found in the queue.")

def main():
    event_queue = EventQueue()

    while True:
        print("\n--- Event Processing System ---")
        print("1. Add event")
        print("2. Process next event")
        print("3. Display pending events")
        print("4. Cancel an event")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            event_name = input("Enter the name of the new event: ")
            event_queue.add_event(event_name)
        elif choice == '2':
            event_queue.process_next_event()
        elif choice == '3':
            event_queue.display_pending_events()
        elif choice == '4':
            try:
                event_id = int(input("Enter event ID to cancel: "))
                event_queue.cancel_event(event_id)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()