from DoublyLinkedList import DoublyLinkedList


def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):

    def merge_sublists(cursor1, cursor2, output, list1, list2):
        if cursor1 is list1.trailer and cursor2 is list2.trailer:  # if both lists are done
            return output

        else:
            if cursor1 is not list1.trailer and cursor2 is not list2.trailer:  # both lists aren't done --> check data
                if cursor1.data < cursor2.data:
                    output.add_last(cursor1.data)
                    return merge_sublists(cursor1.next, cursor2, output, list1, list2)

                else:
                    output.add_last(cursor2.data)
                    return merge_sublists(cursor1, cursor2.next, output, list1, list2)

            else:  # if one list is done
                if cursor1 is list1.trailer:  # if only list1 is done --> add rest of list2
                    output.add_last(cursor2.data)
                    return merge_sublists(cursor1, cursor2.next, output, list1, list2)

                else:  # if only list2 is done --> add rest of list1
                    output.add_last(cursor1.data)
                    return merge_sublists(cursor1.next, cursor2, output, list1, list2)

    merged_list = DoublyLinkedList()
    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next, merged_list, srt_lnk_lst1, srt_lnk_lst2)  # returns merged lists

