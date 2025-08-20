class Node:
    #criando nós
    def __init__(self, data) -> None:
        self.data = data
        self.next = self  #every node created point to itself in the next and prev attributes
        self.prev = self


class DCLL:
    #creates Double Circular Linked List
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
    
    def moveNodeToIndex(self, node: Node, index: int) -> None:
        #TODO
        pass
    
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
playlist.invertedList()
playlist.printPlaylist()