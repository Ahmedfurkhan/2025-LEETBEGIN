import heapq

class NumberContainers:

    def __init__(self):
        self.index_to_number = {}
        self.number_to_heap = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number and self.index_to_number[index] == number:
            return
        self.index_to_number[index] = number
        if number not in self.number_to_heap:
            self.number_to_heap[number] = []
        heapq.heappush(self.number_to_heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.number_to_heap:
            return -1
        heap = self.number_to_heap[number]
        while heap and self.index_to_number.get(heap[0], None) != number:
            heapq.heappop(heap)
        return heap[0] if heap else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)