# Intuition
# We know the heads of all the k lists are the minimum values, if we identify the min and keep using this min to create a new Linked List, we will get the resultant linked list with all nodes in sorted order.

# Approach
# Iterate through each head in the array push all heads in the minHeap.
# Pop from heap will give the smallest element, use it to add to the resultant list.
# If the popped element had an next element, push that to the heap.
# Do this till the heap is empty and we will get all nodes in the resultant list.

# Complexity
# Time Complexity: O(n*k*log(k)). Where n is the maximum length among k linked lists
# Space Complexity: O(k) since we will be storing at most each node from the k lists
class HeapNode:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        # Define comparison based on ListNode's value
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        heapStore = []
        for listHead in lists:
            if listHead is not None:
                heapq.heappush(heapStore, HeapNode(listHead))
        curr = dummyNode
        while len(heapStore) > 0:
            minNode = heapq.heappop(heapStore).node
            curr.next = minNode
            curr = curr.next
            if minNode.next:
                heapq.heappush(heapStore, HeapNode(minNode.next))
            
        return dummyNode.next