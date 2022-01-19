name = "Jose"
matric = "1234"
year = 2

print("=============== NODE ELEMS ========")
node = Node(name, matric, year)
node.print_details()
linked_list = LinkedList()

print("=============== LIST ELEMS ========")
linked_list.add_to_list(node)
linked_list.print_list()

print("=============== LIST: GET_ROOT ========")
root = linked_list.get_root()
root.print_details()

print("=============== LIST: FIND. Att 1 ========")
root = linked_list.find("Test")

print("=============== LIST: FIND. Att 2 ========")
root = linked_list.find("Jose")

print("=============== REMOVE EL ========")
linked_list.removeNode("Jose")
linked_list.print_list()

print("=============== INSERT EL(ERROR CASE) ========")
linked_list.insertAfter(linked_list.get_root(), 8)