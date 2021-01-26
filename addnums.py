class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def getElems(l1: ListNode):
    if l1.next is None:
        return str(l1.val)

    return getElems(l1.next) + str(l1.val)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode()
    p1, p2, p3 = (l1, l2, l3)

    while p1 is not None and p2 is not None:
        p3.next = ListNode()
        addition = p3.val + p1.val + p2.val
        carry = addition // 10
        p3.val = addition % 10

        # update pointers
        p1 = p1.next
        p2 = p2.next
        p3 = p3.next

    if p1 is not None:
        while p1 is not None:
            addition = p3.val + p1.val
            p3.val = addition % 10
            p3.next = ListNode(val = addition//10)

            p1 = p1.next
            p3 = p3.next


    if p2 is not None:
        while p2 is not None:
            addition = p3.val + p2.val
            p3.val = addition % 10
            p3.next = ListNode(val = addition//10)

            p2 = p2.next
            p3 = p3.next


    return l3


if __name__ == '__main__':

    print('Starting program........')
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    print(getElems(l1))

    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(getElems(l2))


    addition = addTwoNumbers(l1, l2)
    print(getElems(addition))

    print('\nEnd of Program.')








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
