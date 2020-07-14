from pprint import pprint
import operator
class Huffman_Tree:
    #TODO: Find a way for the program to build the tree and encode it using the functions you have created #like josephus
    class __Huffman_node:

        def __init__(self,value,key=None):
            self.value = value
            self.key = key
            self.rightChild = None #2i+2
            self.leftChild = None #2i+1

    def __init__(self, string):
        self.__string = string
        self.__array = []
        self.__back = -1 #change to modular maybe??
        self.__heap = []
        self.__code = {}

    def frequency(self):
        letters = {l: 0 for l in " abcdefghijklmnopqrstuvwxyz"}  # assign every character to 0 from the start
        new = self.__string.lower()
        for char in new:  # building frequency
            letters[char] += 1  # add one to char if they are in string
        for key in letters:
            if letters[key] != 0:
                self.__array.append((key, letters[key]))
        self.__heap = [None] * len(self.__array)
        # print("array")
        # self.print_array()
        return self.__array

    def buildHuffmanForest(self):
        for i in range(len(self.__array)):
            self.__array[i] = self.__Huffman_node(self.__array[i][0],self.__array[i][1])
        #print("Huffman",self.array)
        return self.__array

    def __parent(self,current):
        return (current - 1)//2

    def min_heapify(self):
        for i in range (len(self.__array)):
            index = i
            # print()
            # print("i",i)
            self.__heap[i] = self.__array[i]
            self.__back+=1
            while (index != 0):
                if (self.__heap[self.__parent(index)].key > self.__heap[index].key):
                    # print()
                    # print("index", index)
                    # print("got in")
                    new_parent = self.__heap[index]
                    move_OldParent = self.__heap[self.__parent(index)]
                    self.__heap[self.__parent(index)] = new_parent
                    self.__heap[index] = move_OldParent
                    # print("inde sub", index)
                    # print()
                    # print("process")
                    #self.print_tree()
                index = index - 1
        return self.__heap

    def buildTree(self):#find a way to get rid of cells not being used to save space??
        while self.__back != 0:
            t1 = self.__heap[0]
            # print()
            # print("last element", self.__heap[self.__back-1].value)
            self.__heap[0] = self.__heap[self.__back]
            self.__heap[self.__back] = None
            self.__back-=1
            # print("before minheap")
            # self.print_tree()
            # print()
            self.__heap = self.__siftDown()
            # self.print_tree()
            # print()
            t2 = self.__heap[0]
            self.__heap[0] = self.__heap[self.__back]
            self.__heap[self.__back] = None
            self.__back-=1
            self.__heap = self.__siftDown()
            # self.print_tree()
            # print()
            new_tree = self.__Huffman_node(None,(t1.key + t2.key))
            new_tree.leftChild = t1
            new_tree.rightChild = t2
            #print("back", self.__back)
            self.__back += 1
            self.__heap[self.__back] = new_tree

            #correct tree after inserting to the back of tree
            for i in range(self.__back + 1):
                index = i
                while (index != 0):
                    if (self.__heap[self.__parent(index)].key > self.__heap[index].key):
                        new_parent = self.__heap[index]
                        move_OldParent = self.__heap[self.__parent(index)]
                        self.__heap[self.__parent(index)] = new_parent
                        self.__heap[index] = move_OldParent
                    index = index - 1

        #self.print_tree()
        return self.__heap

    def __siftDown(self):
        for i in range(self.__back):
            # self.print_tree()
            # print()
            root = i
            left = (2 * i) + 1
            right = (2 * i) + 2

            if (left < len(self.__heap) and self.__heap[left] != None):
                if self.__heap[i].key > self.__heap[left].key:
                    root = left

            if (right < len(self.__heap) and self.__heap[right] != None):
                if root == left and self.__heap[root].key > self.__heap[right].key:
                    root = right
                elif root != left and self.__heap[i].key > self.__heap[right].key:
                    root = right


            if root != i:
                new_parent = self.__heap[root]
                old_parent = self.__heap[i]
                self.__heap[root] = old_parent
                self.__heap[i] = new_parent
        # self.print_tree()
        return self.__heap

    def encode(self):
        vals = ""
        root = self.__recursive_encode(self.__heap[0],vals)
        return pprint(sorted(self.__code.items(), key=operator.itemgetter(1), reverse=True))

    def __recursive_encode(self,root,vals):
        #tree is self.heap[0]
        #variable to build string as you go
        #you could go all the way to the end of the tree
        #when you return code, reverse it
        if root.value == None:
            self.__recursive_encode(root.leftChild,vals = vals + "0")
            self.__recursive_encode(root.rightChild, vals = vals + "1")
        #root.__code = vals

        elif root.value != None:
            self.__code[str(root.value)] = vals
        vals = vals[:-1]
        return vals

    def decode(self, binary):
        val = ""
        decode = ""
        for num in binary:
            val+=(num)
            for key in self.__code:
                if self.__code[key] == val:
                    decode += key
                    val = ""
        print(decode)

    # def print_array(self):
    #     print(self.__array, end=" ")
    #
    # def print_tree(self):
    #     for i in range(self.__back):
    #         print(self.__heap[i].value,"->", self.__heap[i].key, end=" ")


# if __name__ == '__main__':
#input into string
#make huffman
    # string = input("Give string: ")
    # a = Huffman_Tree(string)
    # a.frequency()
    # a.buildHuffmanForest()
    # a.buildHeap()
    # a.print_array()
    # print()
    # print()
    # a.print_tree()
    # print()
    # print()
    # a.buildTree()
    # # a.print_tree()
    # # print()
    # a.encode()
