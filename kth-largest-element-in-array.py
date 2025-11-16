# Intuition
# We need keep track of all the k largest elements and return the smallest from the k largest elements

# Approach
# Iterate through each element in the array. Push it to a minHeap, and after each push check if the size of the heap is greater than k, if greater than k pop from heap
# Popping from heap will remove the smallest element from the heap
# So every time we pop we can say that at this time, the k elements in the heap are greater than the popped element. 
# If we do this for all the elements, and the resulting heap will only contain k largest elements in the heap
# Hence return the smallest element from the k largest elements.

# Complexity
# Time complexity: O(nlog(k)), since we iterate through the whole n elements and when we iterate we either push or pop to heap, which can be maximum of size k, so log(k)
# Space complexity: O(k) since we save k elements in the heap that are extra elements.

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsHeap = []
        for num in nums:
            heapq.heappush(numsHeap, num)
            if len(numsHeap) > k:
                heapq.heappop(numsHeap)
            
        return heapq.heappop(numsHeap)