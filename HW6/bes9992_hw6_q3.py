from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.list = DoublyLinkedList()

        for elem in list(orig_str):
            if self.list.is_empty():  # adds first instance in list
                self.list.add_last((elem, 1))

            elif elem == self.list.trailer.prev.data[0]:  # if elem is already in list
                self.list.trailer.prev.data = (elem, self.list.trailer.prev.data[1]+1)

            else:  # if list is not empty & elem is a new character
                self.list.add_last((elem, 1))

    def __add__(self, other):
        sum_of_lists = DoublyLinkedList()
        self_cursor = self.list.header.next

        while self_cursor is not self.list.trailer:
            sum_of_lists.add_last(self_cursor.data)
            self_cursor = self_cursor.next

        other_cursor = other.list.header.next

        while other_cursor is not other.list.trailer:
            if other_cursor.data[0] == sum_of_lists.trailer.prev.data[0]:
                sum_of_lists.trailer.prev.data = (other_cursor.data[0], sum_of_lists.trailer.prev.data[1]+1)

            else:
                sum_of_lists.add_last(other_cursor.data)

            other_cursor = other_cursor.next

        compact_str_sum = CompactString("")
        compact_str_sum.list = sum_of_lists

        return compact_str_sum

    def __lt__(self, other):
        self_cursor = self.list.header.next
        other_cursor = other.list.header.next

        while self_cursor is not self.list.trailer or other_cursor is not other.list.trailer:  # while one has nodes left
            if self_cursor is self.list.trailer:  # if self is done
                return True

            if other_cursor is other.list.trailer:  # if other is done
                return False

            if self_cursor.data[0] == other_cursor.data[0]:  # if same elem
                if self_cursor.data[1] == other_cursor.data[1]:  # if same frequency
                    self_cursor = self_cursor.next
                    other_cursor = other_cursor.next

                elif self_cursor.data[1] < other_cursor.data[1]:  # if other has more occurrences
                    if self_cursor.next is self.list.trailer:
                        return True

                    else:
                        return ord(self_cursor.next.data[0]) < ord(other_cursor.data[0])  # return comparison of next self and other

                else:  # if self has more occurrences
                    if other_cursor.next is other.list.trailer:
                        return False

                    else:
                        return ord(self_cursor.data[0]) < ord(other_cursor.next.data[0])  # return comparison of self and next other

            else:  # if not same elem
                return ord(self_cursor.data[0]) < ord(other_cursor.data[0])

        return False

    def __le__(self, other):
        self_cursor = self.list.header.next
        other_cursor = other.list.header.next

        while self_cursor is not self.list.trailer or other_cursor is not other.list.trailer:  # while one has nodes left
            if self_cursor is self.list.trailer:  # if self is done
                return True

            if other_cursor is other.list.trailer:  # if other is done
                return False

            if self_cursor.data[0] == other_cursor.data[0]:  # if same elem
                if self_cursor.data[1] == other_cursor.data[1]:  # if same frequency
                    self_cursor = self_cursor.next
                    other_cursor = other_cursor.next

                elif self_cursor.data[1] < other_cursor.data[1]:  # if other has more occurrences
                    if self_cursor.next is self.list.trailer:
                        return True

                    else:
                        return ord(self_cursor.next.data[0]) < ord(other_cursor.data[0])  # return comparison of next self and other

                else:  # if self has more occurrences
                    if other_cursor.next is other.list.trailer:
                        return False

                    else:
                        return ord(self_cursor.data[0]) < ord(other_cursor.next.data[0])  # return comparison of self and next other

            else:  # if not same elem
                return ord(self_cursor.data[0]) < ord(other_cursor.data[0])

        return True

    def __gt__(self, other):
        return not(self <= other)

    def __ge__(self, other):
        return not(self < other)

    def __repr__(self):
        return str(self.list)

