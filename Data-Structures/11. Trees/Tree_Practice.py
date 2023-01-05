print("Once upon a time...")

class Treenode :
  def __init__(self, story_piece) :
    self.story_piece = story_piece
    self.choices = []

  def add_child(self, node) :
    self.choices.append(node)

  def traverse(self) :
    story_node = self
    print(story_node.story_piece)
    while story_node.choices != [] : #현재 노드에 자식 노드(선택지)가 있으면
      choice = input("Enter 1 or 2 to continue the story: ") #사용자에게 선택지를 입력받음
      if choice not in ["1", "2"] :
        print("Invalid choice. Try again.")
      else : #입력값이 1이나 2인 경우에만 실행
        chosen_index = int(choice)  
        chosen_index -= 1
        chosen_child = story_node.choices[chosen_index] #선택한 자식 노드를 chosen_child에 저장
        print(chosen_child.story_piece) #선택한 자식 노드의 내용을 출력
        story_node = chosen_child #선택한 자식 노드를 현재 노드로 변경

story_root = Treenode("""You are planning a date with your girlfriend. What would you choose as your night out?
1) A live music bar performing Jazz music
2) A cuddle session watching Avatar 2
""")
# print(story_root.story_piece)

choice_a = Treenode("""
You are now at a live Jazz Bar. Smooth Jazz music is playing while you are seated with your woman. What do you do?
1) Stare into her eyes and compliment her looks
2) Vibe with the music, doing a little shimmey
""")

choice_b = Treenode("""
You are now at a movie theare seated next to your girlfriend. As soon as the movie starts, you...
1) Flip the armrest up and move closer to her, putting your hand on her thighs
2) Focus on the movie. The plot is important you know!
""")

story_root.add_child(choice_a)
story_root.add_child(choice_b)
story_root.traverse()

