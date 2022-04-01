from random import randint, random

from keyring import delete_password

class Array:
    def __init__(self,capacity, fill_value= None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
            
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item
        
    def RandomReplace(self, a , b):
        for i in range(len(self.items)):
            self.items[i] = randint(a, b)
    
    def __gettypeoflist__(self):
        self.strtype = True
        self.inttype = True
        for i in range(len(self.items)):
            if type(self.items[i]) == str:
                self.strtype = self.strtype and True
                print("strype True",self.strtype) 
            else:
                self.strtype = False
                print("strype False",self.strtype)
                break
                 
        for i in range(len(self.items)):
            if type(self.items[i]) == int:
                self.inttype = self.inttype and False
                print("intype True",self.inttype)
            else:
                self.inttype = False
                print("intype False",self.inttype)
                break
                
        if self.strtype:
            return type(self.items[0])
        elif self.inttype:
            return type(self.items[0])
        else:
            return "this is a multi-type array"
        
    def Sum(self):
        try:
            if self.strtype:
                self.sum = ""
                for i in self.items:
                    self.sum += i
                    return self.sum
            elif self.inttype:
                self.sum = 0
                for i in self.items:
                    self.sum += i
                    return self.sum
            else:
                raise ValueError("Only can Sum integers or strings")
        except ValueError as ve:
            return ve

class Grid:
    def __init__(self, rows, columns,fill_value = None):
        self.data = Array(rows)
        self.rows = rows
        self.columns = columns
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
            
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""
        
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "
                
            result += "\n"
        return str(result)
    
    def RandomReplace(self, a, b):
        for row in range(self.rows):
            for col in range(self.columns):
                self.data[row][col] = randint(a, b)

class Cube:
    def __init__(self,rows,columns,depth,fill_value = None):
        self.data = Array(rows)
        self.rows = rows
        self.columns = columns
        self.depth = depth
        for row in range(rows):
            self.data[row] = Array(columns)
            for col in range(columns):
                self.data[row][col] = Array(depth,fill_value)
                
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def get_depth(self):
        return len(self.data[0][0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        result = ""
        
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                for de in range(self.get_depth()):
                    result += str(self.data[row][col][de]) + " "
                
            result += "\n"
        return str(result)
    
    def RandomReplace(self, a, b):
        for row in range(self.rows):
            for col in range(self.columns):
                for de in range(self.depth):
                    self.data[row][col][de] = randint(a, b)

class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def append(self, data):
        node = Node(data)
        
        if self.head == None:
            self.head = node
        else:
            current = self.head
            
            while current.next:
                current = current.next
            
            current.next = node
        self.size +=1
        
    def size(self):
        return str(self.size)
    
    def iter(self):
        current = self.head
        
        while current:
            val = current.data
            current = current.next
            yield val
            
    def delete(self,data):
        current = self.head
        
        while current.next.data != data:
            if current.next == None:
                return False
            else:
                current = current.next
        deletednode = current.next
        current.next = deletednode.next
        self.size -=1
        
    def search(self,data):
        for node in self.iter():
            if data == node:
                return print(f"Data {data} found!")
                
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
        
