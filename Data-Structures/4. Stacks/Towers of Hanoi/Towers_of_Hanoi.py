from stacks import Stack

#creating 3 stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks += [left_stack, middle_stack, right_stack]
# print(stacks)

#setting up the Game for towers of Hanoi using stacks
if __name__ == "__main__":
    num_disks = int(input("How many disks do you want to play with?\n"))
    while num_disks < 3:
        num_disks = int(input("Enter a number greater than or equal to 3\n")) #input validation
    for disk in range(num_disks, 0, -1):
        left_stack.push(disk)
    num_optimal_moves = 2 ** num_disks - 1  #formula for optimal moves
    print("The fastest you can solve this game is in {0} moves".format(num_optimal_moves))

  #Get User Input
    def get_input():  
      choices = [stack.get_name()[0] for stack in stacks] #L, M, R로 이루어진 리스트를 반환
      print(choices)
      while True :
        for i in range(len(stacks)):
          name = stacks[i].get_name()
          letter = choices[i]
          print("Enter {0} for {1}".format(letter, name))
        user_input = input("")
        if user_input in choices: #L, M, R 중 하나를 입력하면
          for i in range(len(stacks)):   #stacks 리스트에서 L, M, R을 찾아서 해당하는 stack을 반환
            if user_input == choices[i]:  #choices 리스트에서 입력한 값과 같은 인덱스를 가진 스택을 반환 
              return stacks[i] 
  #Play the Game
    num_user_moves = 0
    while right_stack.get_size() != num_disks:  #right_stack에 num_disks만큼의 디스크가 쌓일 때까지 게임을 계속 진행
      print("\n\n\n...Current Stacks...")
      for stack in stacks:
        stack.print_items()
      while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        if from_stack.is_empty():
          print("\n\nInvalid Move. Try Again")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
          disk = from_stack.pop()
          to_stack.push(disk)
          num_user_moves += 1
          break
        else:
          print("\n\nInvalid Move. Try Again")


