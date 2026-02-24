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
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
    return arr    

arr = [5, 2, 1, 9, 5, 6, 8]

print(bubble_sort(arr))