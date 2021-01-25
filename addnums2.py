
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def getElems(l1: ListNode):
    if l1.next is None:
        return str(l1.val)

    return getElems(l1.next) + str(l1.val)


def cleanExcess(p1, p2, carry, base):
    pass


def addnums(l1: ListNode, l2: ListNode) -> ListNode:
    base, carry = 10, 0
    while p1 is not None and p2 is not None:
        addition = p1.val + p2.val + carry
        carry = sum // base
        p1.val = sum % base

        # update
        p1 = p1.next
        p2 = p2.next


    cleanExcess(p1, p2, carry, base)



if __name__ == '__main__':

    print('Starting program........')
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    print(getElems(l1))

    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(getElems(l2))


    addition = addTwoNumbers(l1, l2)
    print(getElems(addition))

    print('\nEnd of Program.')
