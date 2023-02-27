# Queue Interaction

- **Enqueue**
    - adding to a queue
        - add to head of the queue
    - **Scenarios to consider**
        1. The queue is **empty**, so the node we’re adding is **both the head and tail** of the queue
        2. The queue has **at least one other node**, so the **added node becomes the new tail**
        3. The queue is **full**, so the node **will not get added** because we don’t want queue “overflow”
- **Dequeue**
    - **Scenarios to consider**
        1. The queue is **empty**, so we cannot remove or return any nodes lest we run into queue “underflow”
        2. The queue has one node, so when we remove it, the queue will be empty and we need to **reset** the queue’s `head` and `tail` to `None`
        3. The queue has more than one node, and we just remove the `head` node and reset the `head` to the following node