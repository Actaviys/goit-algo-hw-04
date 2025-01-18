
import random
import timeit


# Функція сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Функція сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr




def timsort(arr):
    """ 
    Функція сортування.
    `sorted` - вбудований метод python,
    використовує гібридний вбудований метод Timsort
    """
    return sorted(arr) 


# Функція генерації даних
def generate_data(size, case="random"):
    if case == "random":
        return [random.randint(0, 10000) for _ in range(size)]
    elif case == "sorted":
        return list(range(size))
    elif case == "reversed":
        return list(range(size, 0, -1))

# Емпіричне тестування
def test_sorting_algorithms():
    sizes = [1000, 5000, 10000]
    cases = ["random", "sorted", "reversed"]
    results = []

    for size in sizes:
        for case in cases:
            data = generate_data(size, case)

            time_insertion = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
            time_merge = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
            time_timsort = timeit.timeit(lambda: timsort(data.copy()), number=1) 

            results.append({
                "size": size,
                "case": case,
                "insertion_sort": time_insertion,
                "merge_sort": time_merge,
                "timsort": time_timsort,
            })

    return results

# Аналіз результатів
def analyze_results():
    results = test_sorting_algorithms()
    print(f"{'Size':<10}{'Case':<10}{'Insertion':<15}{'Merge':<15}{'Timsort':<15}")
    print("-" * 65)
    for result in results:
        print(f"{result['size']:<10}{result['case']:<10}{result['insertion_sort']:<15.6f}{result['merge_sort']:<15.6f}{result['timsort']:<15.6f}")


if __name__ == "__main__":
    analyze_results()