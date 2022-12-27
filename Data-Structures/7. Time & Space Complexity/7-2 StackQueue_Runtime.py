#Stacks vs. Queues Runtime

#I. compare the runtime of retrieving the first value added to a queue Vs. the runtime of retrieving the first value added to a stack

from etc.stack import Stack
from etc.queue import Queue

N = 6

my_stack = Stack(N)
my_stack.push("Australia")
my_stack.push("India")
my_stack.push("Costa Rica")
my_stack.push("Peru")
my_stack.push("Ghana")
my_stack.push("Indonesia")

my_queue = Queue(N)
my_queue.enqueue("Australia")
my_queue.enqueue("India")
my_queue.enqueue("Costa Rica")
my_queue.enqueue("Peru")
my_queue.enqueue("Ghana")
my_queue.enqueue("Indonesia")

#Print the first values in the stack and queue
print("The top value in my stack is: {0}".format(my_stack.peek()))
print("The front value of my queue is: {0}".format(my_queue.peek()))

#Get First Value added to Queue
first_value_added_to_queue = my_queue.dequeue()
print("\nThe first value enqueued to the queue was {0}".format(first_value_added_to_queue))
queue_runtime = "1" #Checkpoint 3
print("The runtime of getting the front of the queue is O({0})".format(queue_runtime))

#Get First Value added to Stack
#Write Code Here for #Checkpoint 4
  #방법 1 :my_stack을 (n-1)번 pop하고, 마지막 pop한 값을 first_value_added_to_stack에 저장한다.
for i in range(5):
  my_stack.pop()
first_value_added_to_stack = my_stack.pop()
  #방법 2 : while을 사용하여 my_stack.is_empty()가 False일 때까지 pop하면서 값을 first_value_added_to_stack에 저장한다(update).
print("\nThe first value pushed onto the stack was {0}".format(first_value_added_to_stack))
stack_runtime = "N" #Checkpoint 5
print("The runtime of getting the bottom of the stack is O({0})".format(stack_runtime))