from abc import ABC, abstractmethod
import time

class Sort(ABC):

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _sort(self):
        pass

    def get_items(self):
        return self._items

    def _time(self):
        start_time = time.time()
        self._sort()
        end_time = time.time()
        return end_time - start_time

class BubbleSort(Sort):

    def _sort(self):
        for j in range(len(self._items)):
            for i in range(len(self._items) - 1):
                if self._items[i] > self._items[i + 1]:
                    self._items[i], self._items[i + 1] = self._items[i + 1], self._items[i]

class MergeSort(Sort):

    def _sort(self):
        if len(self._items) > 1:
            mid = len(self._items) // 2
            left_half = self._items[:mid]
            right_half = self._items[mid:]

            left_half_sorter = MergeSort(left_half)
            right_half_sorter = MergeSort(right_half)

            left_half_sorter._sort()
            right_half_sorter._sort()

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    self._items[k] = left_half[i]
                    i += 1
                else:
                    self._items[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                self._items[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                self._items[k] = right_half[j]
                j += 1
                k += 1

def main():
    a = int(input("Enter the size of the list:"))
    print("Enter the list:")
    b = []
    for i in range(a):
        b.append(int(input()))
    
    bubble_sorter = BubbleSort(b.copy())
    bubble_time = bubble_sorter._time()
    print(f"Bubble Sort took {bubble_time} seconds to sort the list.")
    print("Sorted List (Bubble Sort):", bubble_sorter.get_items())

    merge_sorter = MergeSort(b.copy())
    merge_time = merge_sorter._time()
    print(f"Merge Sort took {merge_time} seconds to sort the list.")
    print("Sorted List (Merge Sort):", merge_sorter.get_items())

if __name__ == "__main__":
    main()
