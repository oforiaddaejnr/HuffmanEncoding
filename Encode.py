from Huffman_Tree import Huffman_Tree

def encode(string):
    string.frequency()
    string.buildHuffmanForest()
    string.min_heapify()
    string.buildTree()
    string.encode()

def decode(binary):
    string.decode(binary)


if __name__ == '__main__':
  text = input("Input string you would like to encode: ")
  string = Huffman_Tree(text)
  encode(string)
  binary = str(input("Based on generated encodings input binary string you would like to decode: "))
  decode(binary)
