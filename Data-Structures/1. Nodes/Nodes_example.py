#node 클래스 생성
class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self._link_node = link_node

    @property
    def link_node(self):
        return self._link_node

    @link_node.getter
    def link_node(self):
        return self._link_node

    @link_node.setter
    def link_node(self, link):
        self._link_node = link

    def value(self):
        return self.value
        
# Instantiate Nodes
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

#test
print('yacko value : ', yacko.value)

# setting link node
dot.link_node = wacko # dot -> wacko link 생성
yacko.link_node = dot # yacko -> dot link 생성
# yacko -> dot -> wacko 형태로 링크 생성. wacko는 null pointer

#test
print('yacko link : ', yacko.link_node)


#get value using link nodes
dot_value = yacko.link_node.value
wacko_value = dot.link_node.value

#test
print("dot : " , dot_value)
print("wacko : " , wacko_value)