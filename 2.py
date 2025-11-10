def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    salaries = [30000.5, 50000.2, 20000.7, 70000.9, 60000.4, 40000.8]
    print("Original Salaries:", salaries)

    sorted_selection = selection_sort(salaries.copy())
    print("\nSalaries sorted using Selection Sort:", sorted_selection)

    sorted_bubble = bubble_sort(salaries.copy())
    print("\nSalaries sorted using Bubble Sort:", sorted_bubble)

if __name__ == "__main__":
    main()