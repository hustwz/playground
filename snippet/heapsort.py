def MAX_Heapify(heap, start, end):
    l = 2 * start + 1
    while l <= end:
        if l + 1 <= end and heap[l] < heap[l+1]:
            l += 1
        if heap[start] > heap[l]:
            return
        else:
            heap[start], heap[l] = heap[l], heap[start]
            start = l
            l = 2 * start + 1

def Build_Max_Heap(heap):
    for i in range(len(heap)/2-1, -1, -1):
        MAX_Heapify(heap, i, len(heap)-1)

def heap_sort(heap):
    Build_Max_Heap(heap)
    for i in range(len(heap)-1, 0, -1):
        heap[0], heap[i] = heap[i], heap[0]
        MAX_Heapify(heap, 0, i-1)
