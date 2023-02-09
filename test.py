# from treelib import Node, Tree
# tree = Tree()
# tree.create_node("Harry", "harry")  # root node
# tree.create_node("Jane", "jane", parent="harry")
# tree.create_node("Bill", "bill", parent="harry")
# tree.create_node("Diane", "diane", parent="jane")
# tree.create_node("Mary", "mary", parent="diane")
# tree.create_node("Mark", "mark", parent="jane")
# tree.show()


def solution():
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]
    answer = []

    #I. convert enroll and referral to tree structure
    from treelib import Node, Tree
    tree = Tree()
    tree.create_node("center", "center") # root node
    for i in range(len(enroll)):
    #if parent is '-' then parent is center
        if referral[i] == '-':
            tree.create_node(enroll[i], enroll[i], parent="center", data= { 'money': 0 })
        else:
            tree.create_node(enroll[i], enroll[i], parent=referral[i], data={ 'money': 0 })
    tree.show()

    #II. add money to each node
    for i in range(len(seller)):
        node = tree.get_node(seller[i])
        money = amount[i] * 100

    #III. reverse traverse the tree, transferring 10% of the money to the parent node
    node = tree.parent(enroll[len(enroll)-1]) #initialize node to the last node
    while node != None:
        money = node.data['money']
        transfer_sum = money // 10
        node.data['money'] = money - transfer_sum #deduct 10% of the money from current node
        node = tree.parent(node.identifier) #move to parent node
        node.data['money'] = node.data['money'] + transfer_sum #add 10% of the money to parent node

    #IV. get the money from each node
    for i in range(len(enroll)):
        node = tree.get_node(enroll[i])
        answer.append(node.data['money'])

    return answer
    
print(solution())
