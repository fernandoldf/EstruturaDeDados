class Node:
    #criando nós
    def __init__(self, data) -> None:
        self.data = data
        self.next = self
        self.prev = self


class DCLL:
    #creates Double Circular Linked List
    def __init__(self) -> None:
        self.tail = None

    def addEnd(self, data) -> None:
        newNode = Node(data)
        if self.tail is None:
            self.tail = newNode
            return
        newNode.next = self.tail.next
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
    
    def addNodeatIndex(self, node: Node, index: int) -> None:
        if self.tail is None:
            self.addEnd(node)
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
        super().__init__()
        self.current = None
        
    def addMusic(self, title) -> None:
        self.addEnd(title)
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
playlist.addMusic("Celia")
playlist.playNext()
playlist.playNext()
playlist.playPrev()
playlist.printPlaylist()