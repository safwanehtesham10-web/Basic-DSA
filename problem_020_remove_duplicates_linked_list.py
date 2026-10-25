class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

def delete_duplicates(root):
    iterator = root
    while iterator and iterator.next:
        if iterator.val == iterator.next.val:
            iterator.next = iterator.next.next
        else:
            iterator = iterator.next
    return root

head_node = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
delete_duplicates(head_node)

temp = head_node
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
