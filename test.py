from DataStructures import Array, Grid,Cube,Node,SinglyLinkedList

matrix = Cube(3,3,8)
print(matrix)
for row in range(matrix.get_height()):
    for col in range(matrix.get_width()):
        for de in range(matrix.get_depth()):
            matrix[row][col][de] = row*col*de

matrix.RandomReplace(11,99)
print(matrix)

words = SinglyLinkedList()
words.append("egg")
words.append("ham")
words.append("spam")
words.search("spam")
print (words.size)
words.delete("ham")
print (words.size)
words.clear()
print(words.size)