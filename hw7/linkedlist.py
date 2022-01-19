class LinkedList:
    """
    This class is the one you should be modifying!
    Don't change the name of the class or any of the methods.

    Implement those methods that current raise a NotImplementedError
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_to_list(self, node):
        """
        This method should add at the beginning of the linked list.
        if root has a value:
            next of new node = root
            
        root = new node
        """
        
        if self.__root:
            node.set_next(self.__root)
            
        self.__root = node
        #raise NotImplementedError()
        
    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        '''
        marker = root
        while marker:
            if marker'sname == name:
                return marker
            marker = next item of marker
            
        raise LookupError("Name {} was not found in the linked list.".format(name))
        '''
        marker = self.__root
        while marker:
            if marker.name == name:
                print(True)
                return marker
            marker = marker.get_next()
        print(False)
        return marker
        #raise LookupError(f"Name {name} was not found in the linked list.")
        
    def removeNode(self, value):

        prev = None
        curr = self.__root
        
        while curr:
            if curr.name == value:
                if prev:
                    prev.set_next(curr.get_next())
                else:
                    self.__root = curr.get_next()
                return True
                    
            prev = curr
            curr = curr.get_next()
            
        return False
        
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print ("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)

        new_node.__next = prev_node.__next

        prev_node.__next = new_node