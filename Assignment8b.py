# Implementation of Linear probing hashing scheme
# Write a menu driven program for below op
# 1. insert (key)
# 2. Search (key)
# 3. Delete (key)
# 4. Display table 
# 5. Exit

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  
    
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key):
        index = self.hash_function(key)
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"{key} already exists at index {index}.")
                return
            index = (index + 1) % self.size
            if index == start_index:  
                print("Hash table is full. Can't insert more keys.")
                return
        
        self.table[index] = key
        print(f"{key} inserted at index {index}.")
    
    def search(self, key):
        index = self.hash_function(key)
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"{key} found at index {index}.")
                return True
            index = (index + 1) % self.size
            if index == start_index:
                break
        
        print(f"{key} not found.")
        return False
    
    def deletion(self, key):
        index = self.hash_function(key)
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"{key} deleted from index {index}.")
                self.table[index] = None
                self._rehash_from(index)
                return True
            index = (index + 1) % self.size
            if index == start_index:
                break
        
        print(f"{key} not found.")
        return False
    
    def _rehash_from(self, empty_index):
        index = (empty_index + 1) % self.size
        
        while self.table[index] is not None:
            key_to_rehash = self.table[index]
            self.table[index] = None
            self.insert(key_to_rehash)
            index = (index + 1) % self.size
    
    def display(self):
        print("\nHash Table contents:")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")
        print()


def menu():
    print("------------------------------")
    print("HASH TABLE MENU (Linear Probing)")
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
