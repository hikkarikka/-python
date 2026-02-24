import time

def decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"время выполнения {func.__name__} = {end - start:.8f} секунд")
        return result 
    return wrapper




@decorator
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [5, 2, 1, 9, 5, 6, 8]
print(insertion_sort(arr))