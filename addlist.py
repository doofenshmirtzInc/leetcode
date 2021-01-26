# while both lists are not empty
    # p3.next = ListNode()
    # p3 = p3.next
    # sum current elems
    # if (sum + carry) < 10
        # new list elem = sum + carry
    # else
        # new list elem = (sum + carry) % 10
        # carry = 1

    # update statements (move pointers)
    # p1 = p1.next
    # p2 = p2.next


    # if l1 not empty:
        # p3.next = Link
        # while carry = 1
            #





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def addcommon(l1: ListNode, l2: ListNode) -> ListNode:
    # set up pointers
    p1, p2 = (l1, l2)
    l3, p3 = (ListNode(),)* 2
    carry = 0

    while p1 is not None and p2 is not None:
        if p3 is not l3:
            p3.next = ListNode()
            p3 = p3.next

        add = p1.val + p2.val + carry
        if add < 10:
            p3.val = add
        else:
            p3.val = add % 10
            carry = 1


        # updates
        p1, p2 = (p1.next, p2.next)
        print('val of l3: ', l3.val)

    return l3









def addtail(l1: ListNode, l2: ListNode) -> ListNode:
    pass

def solve(l1: ListNode, l2: ListNode) -> ListNode:
    pass


if __name__ == '__main__':

    l1 = ListNode(1, ListNode(2, ListNode(3, None)))
    l2 = ListNode(4, ListNode(5, ListNode(6, None)))

    common = addcommon(l1, l2)

    while common is not None:
        print('value of a common node: ', common.val)
        common = common.next
