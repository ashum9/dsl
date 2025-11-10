def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    customer_ids = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 30000, 40000, 50000, 100000]
    key = int(input("Enter Customer ID to search: "))

    print("\nUsing Linear Search:")
    pos = linear_search(customer_ids, key)
    if pos != -1:
        print(f"Customer ID found at position {pos+1}")
    else:
        print("Customer ID not found")

    print("\nUsing Binary Search:")
    pos = binary_search(customer_ids, key)
    if pos != -1:
        print(f"Customer ID found at position {pos+1}")
    else:
        print("Customer ID not found")

if __name__ == "__main__":
    main()