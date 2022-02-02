class Node:
    def __init__(self, data):
        self.item = data    # 数据
        self.next = None    # 指针

    def __repr__(self):     # 把结点表示为一个字符串
        # 字符串格式化输出
        return "Node({})".format(self.item)


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> None:
        current = self.head
        # 遍历
        for _ in range(index):
            current = current.next
        return current

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise Exception('索引越界！')
        new_node = Node(data)
        if self.size == 0:    # 空链表
            self.head = new_node
            self.tail = new_node
        elif index == 0:        # 头部插
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:    # 尾部插
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def __repr__(self):
        curr = self.head
        str = ''
        while curr:
            str += f'{curr}-->'
            curr = curr.next
        return str + 'END'

    # def remove(self, index):
    #     temp = self.head
    #     if self.size == 0:
    #         raise Exception('空链表！')
    #
    #     if index < 0 or index > self.size -1:
    #         raise Exception('索引越界！')
    #     elif self.head == self.tail:    # 只有一个结点
    #         self.tail = None
    #         self.head = None
    #         self.size = 0
    #     else:
    #         prev = self.get(index - 1)
    #         prev.next = prev.next.next
    def remove(self, index):
        if index < 0 or index >= self.size - 1:
            raise Exception('索引越界！')
        elif self.size == 0:
            raise Exception('空链表！')
        elif index == 0:
            remove_node = self.head
            self.head = self.head.next
            remove_node.next = None
        elif index == self.size - 1:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = prev.next.next

    def delete(self,index):
        if index < 0 or index > self.size -1:
            raise Exception('超出索引！')
        elif self.size == 0:
            raise Exception('空链表！！')
        elif index == 0:
            remove = self.head
            self.head = remove.next
            remove.next = None
        elif index == self.size - 1 :
            prev = self.get(index - 1)
            remove = prev.next
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index -1)
            remove = prev.next
            prev.next = prev.next.next
        self.size -= 1
    def reverse(self)->None:
        pre = None
        temp = self.head
        while temp:
            next_node = temp.next
            temp.next = pre
            pre = temp
            temp = next_node
        self.head = pre


# l = LinkList()
# l.insert(0, 1)
# l.insert(1, 2)
# l.insert(2, 3)
# l.insert(3, 4)
# l.insert(4, 5)
#
# # result = l.get(0)
# # print(l)
# # print(result)
# print(l)
# l.remove(4)
# print(l)

if __name__ == '__main__':
    a = LinkList()
    a.insert(0,1)
    print(a)
    a.insert(1,2)
    print(a)
    a.insert(2, 3)
    print(a)
    a.insert(3, 4)
    print(a)
    a.delete(1)
    print(a)
    a.reverse()
    print(a)



