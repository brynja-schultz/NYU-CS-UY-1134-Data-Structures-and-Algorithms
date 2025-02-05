from DoublyLinkedList import DoublyLinkedList


def copy_linked_list(lnk_lst):
    copy_list = DoublyLinkedList()

    cursor = lnk_lst.header

    while cursor.next is not lnk_lst.trailer:
        copy_list.add_last(cursor.next.data)
        cursor = cursor.next

    return copy_list


def deep_copy_linked_list(lnk_lst):
    copy_list = DoublyLinkedList()

    cursor = lnk_lst.header.next

    while cursor is not lnk_lst.trailer:
        if type(cursor.data) != int:
            sub_copy = deep_copy_linked_list(cursor.data)
            copy_list.add_last(sub_copy)
        else:
            copy_list.add_last(cursor.data)

        cursor = cursor.next

    return copy_list
