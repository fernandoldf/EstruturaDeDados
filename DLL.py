class Node:
    #criando nós
    def __init__(self, data) -> None:
        self.data = data
        self.next = self  #every node created point to itself in the next and prev attributes
        self.prev = self


class DCLL:
    #creates Doubly Circular Linked List
    def __init__(self) -> None:
        self.tail = None

    def appendLL(self, data) -> None:
        newNode = Node(data)
        if self.tail is None:  #testing case of no node
            self.tail = newNode
            return
        newNode.next = self.tail.next
        newNode.prev = self.tail
        self.tail.next.prev = newNode
        self.tail.next = newNode
        self.tail = newNode
        return
    
    def moveNodeToIndex(self, data: str, index: int) -> None:
        if index < 0:
            print("Index must be a positive Integer.")
            return
        if self.tail is None:
            print("The list is empty")
            return

        # Find the node and its current index
        current = self.tail.next
        desired_node = None
        current_index = 0
        length = 0
        while True:
            if current.data == data and desired_node is None:
                desired_node = current
                desired_node_index = current_index
            current = current.next
            current_index += 1
            length += 1
            if current == self.tail.next:
                break

        if desired_node is None:
            print(f"Node with data '{data}' not found.")
            return

        if index >= length:
            print("Index out of range.")
            return

        if index == desired_node_index:
            print("Node is already at the desired index.")
            return

        #remove desired_node
        desired_node.prev.next = desired_node.next
        desired_node.next.prev = desired_node.prev
        if desired_node == self.tail:
            self.tail = desired_node.prev

        #insert at new index
        current = self.tail.next
        for _ in range(index):
            current = current.next

        desired_node.prev = current.prev
        desired_node.next = current
        current.prev.next = desired_node
        current.prev = desired_node

        #update tail if inserted at the end
        if index == length - 1:
            self.tail = desired_node


    def invertedList(self) -> None:
        if self.tail is None or self.tail.next == self.tail:  #testing no node or one node
            return
        new_tail = self.tail.next  #storing the new tail address
        support_node = self.tail
        while(True):
            support_node.prev, support_node.next = support_node.next, support_node.prev
            support_node = support_node.next
            if support_node == self.tail:  #will break loop when it goes back to the tail
                break
        self.tail = new_tail #pointing to the new tail preveously stored
        return


    def printCDLL(self, highlight = None) -> None:
        if self.tail is None:
            print("Linked List is empty.")
            return
        current_node = self.tail.next
        text = "PlayList: "
        while current_node != self.tail:
            text += str(current_node.data) + " -> "
            current_node = current_node.next
        text += str(self.tail.data)
        if highlight is not None:
            text = text.replace(highlight, "{"+highlight+"}") 
        print(text)


class PlayList(DCLL):
    
    def __init__(self) -> None:
        super().__init__()    #constructor using hierarchy
        self.current = None   #attribute to keep record of the current music playing
        
    def addMusic(self, title) -> None:
        self.appendLL(title)
        if self.current is None:
            self.current = self.tail.next
        return
    
    def playNext(self) -> None:
        self.current = self.current.next
        return
    
    def playPrev(self) -> None:
        self.current = self.current.prev
        return
    
    def printPlaylist(self) -> None:
        self.printCDLL(self.current.data)
        return


playlist = PlayList()
playlist.addMusic("Numb")
playlist.addMusic("Crawling")
playlist.addMusic("In The End")
playlist.addMusic("Somewhere I Belong")
playlist.addMusic("Faint")
playlist.addMusic("What I've Done")
playlist.invertedList()
playlist.invertedList()
playlist.moveNodeToIndex("What I've Done", 4)
playlist.printPlaylist()