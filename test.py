class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



p1 = None
l1 = p1

for i in range(5):
    if p1 is None:
        p1 = ListNode()
    else:
        p1.next = ListNode(i)
        p1 = p1.next




p2 = l1
while p2 is not None:
    print('the value of the node is: ', p2.val)
    p2 = p2.next



if l1 is None:
    print('not working')
