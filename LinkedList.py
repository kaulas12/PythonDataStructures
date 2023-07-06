class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def __str__(self):
    temp_node = self.head
    result = ''
    while temp_node is not None:
      result += str(temp_node.value)
      if temp_node.next is not None:
        result += "->"
      temp_node = temp_node.next
    return result

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node

  def prepend(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1

  def insert(self, index, value):
    new_node = Node(value)
    if index < 0 or index > self.length:
      return False
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    elif index == 0:
      new_node.next = self.head
      self.head = new_node
    else:
      temp_node = self.head
      for _ in range(index - 1):
        temp_node = temp_node.next
      new_node.next = temp_node.next
      temp_node.next = new_node
    self.length += 1
    return True
  def traverse(self):
    current = self.head
    while current is not None:
      print(current.value)
      current = current.next
  def get(self,index):
    if index == -1:
      return self.tail
    elif index< -1 or index >= self.length:
      return None
    current = self.head
    for _ in range(index):
      current = current.next
    return current
  def set_value(self,index,value):
    temp = self.get(index)
    if temp:
      temp.value = value
      return True
    return False
    
  def pop_first(self):
    if self.length == 0:
        return None
    popped_node = self.head
    if self.length == 1:
        self.head = None
        self.tail = None
    else:
        self.head = self.head.next
        popped_node.next = None
    self.length -= 1
    return popped_node

  def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node
    

  


new_linked_list = LinkedList()
new_linked_list.insert(0, 0)
print(new_linked_list)
new_linked_list.append(20)
new_linked_list.append(200)
new_linked_list.append(201)
print(new_linked_list)
new_linked_list.prepend(12)
print(new_linked_list)
new_linked_list.insert(0, 2)
print(new_linked_list)
new_linked_list.traverse()
print(new_linked_list.get(2))
print(new_linked_list.set_value(2,2))
print(new_linked_list.pop_first())
