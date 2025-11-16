"""
PROBLEM: Implement Queue from Scratch (Circular Queue)
======================================================

A Queue is a linear data structure that follows the First-In-First-Out (FIFO) principle.
The first element inserted is the first one to be removed.

This implementation uses a Circular Queue approach to efficiently utilize array space.

Key Operations:
1. EnQueue(val) - Add element to rear of queue
2. DeQueue() - Remove element from front of queue
3. isEmpty() - Check if queue is empty
4. isFull() - Check if queue is full
5. queue_front() - View front element
6. queue_rear() - View rear element

APPROACH & REASONING:
====================
We use a Circular Queue (Ring Buffer) implementation because:
1. Efficient space utilization - reuses empty spots after dequeue
2. Fixed capacity prevents unbounded growth
3. O(1) enqueue and dequeue operations
4. Uses modulo arithmetic to wrap around array indices

In a regular queue, after many enqueue/dequeue operations, front moves forward
and space at the beginning is wasted. Circular queue solves this by wrapping
the rear pointer back to the beginning when it reaches the end.

FLOWCHART:
=========

EnQueue Operation:
┌──────────────┐
│    START     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Is Full?    │
└───┬──────┬───┘
    │      │
   Yes    No
    │      │
    ▼      ▼
┌────────┐ ┌─────────────────┐
│ Print  │ │ rear=(rear+1)   │
│ Error  │ │  % capacity     │
│ Return │ │                 │
└────────┘ └────────┬────────┘
                    │
                    ▼
           ┌─────────────────┐
           │ queue[rear]=val │
           └────────┬────────┘
                    │
                    ▼
           ┌─────────────────┐
           │   size += 1     │
           └────────┬────────┘
                    │
                    ▼
              ┌─────────┐
              │   END   │
              └─────────┘

DeQueue Operation:
┌──────────────┐
│    START     │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Is Empty?   │
└───┬──────┬───┘
    │      │
   Yes    No
    │      │
    ▼      ▼
┌────────┐ ┌─────────────────┐
│ Print  │ │ front=(front+1) │
│ Error  │ │  % capacity     │
│ Return │ │                 │
└────────┘ └────────┬────────┘
                    │
                    ▼
           ┌─────────────────┐
           │   size -= 1     │
           └────────┬────────┘
                    │
                    ▼
              ┌─────────┐
              │   END   │
              └─────────┘

Circular Array Visualization:
     front
       ↓
[10][20][30][ ][ ]
            ↑
          rear

After wrapping:
       front
         ↓
[40][ ][30][20][10]
 ↑
rear (wrapped around)

TIME COMPLEXITY:
===============
- EnQueue(): O(1) - Direct array access with index calculation
- DeQueue(): O(1) - Direct array access with index calculation
- isEmpty(): O(1) - Simple size check
- isFull(): O(1) - Simple size check
- queue_front(): O(1) - Direct array access
- queue_rear(): O(1) - Direct array access

SPACE COMPLEXITY: O(n) where n is the capacity of the queue
"""

class Queue:
    def __init__(self, capacity) -> None:
        """
        Initialize a circular queue with fixed capacity.

        Args:
            capacity: Maximum number of elements the queue can hold

        Instance variables:
        - front: Index of the front element (where we dequeue from)
        - rear: Index of the rear element (where we enqueue to)
        - size: Current number of elements in queue
        - capacity: Maximum capacity of queue
        - queue: Fixed-size array to store elements
        """
        self.front = self.size = 0
        # rear starts at capacity-1 because EnQueue increments it first
        self.rear = capacity - 1
        self.capacity = capacity
        # Initialize array with None values
        self.queue = [None] * capacity

    def isEmpty(self):
        """
        Check if the queue is empty.

        Returns:
            True if queue has no elements, False otherwise
        """
        return self.size == 0

    def isFull(self):
        """
        Check if the queue is full.

        Returns:
            True if queue is at maximum capacity, False otherwise
        """
        return self.size == self.capacity

    def EnQueue(self, val):
        """
        Add an element to the rear of the queue.

        Args:
            val: The value to be added to the queue

        The rear pointer moves circularly using modulo arithmetic.
        If rear is at the last index, it wraps to index 0.
        """
        if self.isFull():
            print("Queue is Full")
            return

        # Move rear pointer circularly
        # Example: if capacity=5 and rear=4, (4+1)%5=0 (wraps to start)
        self.rear = (self.rear + 1) % self.capacity

        # Insert the element at the new rear position
        self.queue[self.rear] = val

        # Increment the size counter
        self.size += 1
        print(f"Insert {val} into the queue")

    def DeQueue(self):
        """
        Remove and return the element from the front of the queue.

        The front pointer moves circularly using modulo arithmetic.
        If front is at the last index, it wraps to index 0.

        Returns:
            The element at the front of the queue
        """
        if self.isEmpty():
            print("Queue is Empty")
            return

        # Print the element being removed
        print(f"Removed {self.queue[self.front]}")

        # Move front pointer circularly
        # Example: if capacity=5 and front=4, (4+1)%5=0 (wraps to start)
        self.front = (self.front + 1) % self.capacity

        # Decrement the size counter
        self.size -= 1

    def queue_front(self):
        """
        Display the element at the front of the queue without removing it.

        This is useful for peeking at the next element to be dequeued.
        """
        if not self.isEmpty():
            print(f"Element at front {self.queue[self.front]}")
        else:
            print("Queue is Empty")

    def queue_rear(self):
        """
        Display the element at the rear of the queue.

        This is useful for seeing the most recently added element.
        """
        if not self.isEmpty():
            print(f"Element at end {self.queue[self.rear]}")
        else:
            print("Queue is Empty")


# EXAMPLE USAGE AND TEST CASES
if __name__ == "__main__":
    # Create a queue with capacity 30
    queue = Queue(30)

    print("Testing Queue Operations:")

    # Enqueue elements
    queue.EnQueue(10)  # Insert 10 into the queue
    queue.EnQueue(20)  # Insert 20 into the queue
    queue.EnQueue(30)  # Insert 30 into the queue
    queue.EnQueue(40)  # Insert 40 into the queue

    # Dequeue one element
    queue.DeQueue()  # Removed 10

    # View front and rear
    queue.queue_front()  # Element at front 20
    queue.queue_rear()   # Element at end 40

    print(f"\nQueue size: {queue.size}")  # 3
    print(f"Is empty: {queue.isEmpty()}")  # False
    print(f"Is full: {queue.isFull()}")    # False
