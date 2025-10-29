# Implement a hash table of size 10 and use the division method as a hash function 
# In case of collision use chaining. Implement the following op:
# 1. Insert(key): Insert key-value pairs into the hash table
# 2. Search(key): Search for the value associated with a given key
# 3. Delete(key): Delete a key-value pair from the hash table
# 4. Display the hash table
# 5. Exit
# Input Key Sequence = 31, 45, 53, 81, 22 , 17, 62, 11, 29, 65, 19
# hash function = key%10 
# Bucket size = 4


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class HashTable:
    def __init__(self, size=10, bucket_size=4):
        self.size = size
        self.bucket_size = bucket_size
        self.myhash = {i: None for i in range(size)}
    
    def hash_function(self, value):
        return value % self.size
    
    def insert(self, value):
        key = self.hash_function(value)
        head = self.myhash[key]

        count = 1 if head else 0
        curr = head
        while curr and curr.next:
            count += 1
            if curr.data == value:
                print(f"{value} already exists in bucket {key}")
                return
            curr = curr.next
        
        if curr and curr.data == value:
            print(f"{value} already exists in bucket {key}")
            return
        
        if count >= self.bucket_size:
            print(f"Bucket {key} full. Can't insert {value}.")
            return

        new_node = Node(value)
        if curr:
            curr.next = new_node
        else:
            self.myhash[key] = new_node
        print(f"{value} inserted in the bucket {key}.")
        
    def search(self, value):
        key = self.hash_function(value)
        curr = self.myhash[key]
        while curr:
            if curr.data == value:
                print(f"{value} found in bucket {key}.")
                return True
            curr = curr.next
        print(f"{value} not found in bucket {key}.")
        return False
    
    def deletion(self, value):
        key = self.hash_function(value)
        curr = self.myhash[key]
        prev = None
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.myhash[key] = curr.next
                print(f"{value} deleted from bucket {key}.")
                return True
            prev = curr
            curr = curr.next
        print(f"{value} not found in bucket {key}.")
        return False
    
    def display(self):
        print("\nHash Table contents:")
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            curr = self.myhash[i]
            while curr:
                print(curr.data, end=" -> ")
                curr = curr.next
            print("None")
        print()


def menu():
    print ("------------------------------")
    print("HASH TABLE MENU")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")


if __name__ == "__main__":
    ht = HashTable()

    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            val = int(input("Enter value to insert: "))
            ht.insert(val)

        elif choice == '2':
            val = int(input("Enter value to search: "))
            ht.search(val)

        elif choice == '3':
            val = int(input("Enter value to delete: "))
            ht.deletion(val)

        elif choice == '4':
            ht.display()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


