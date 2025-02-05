from DoublyLinkedList import DoublyLinkedList


class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for elem in list(num_str):
            self.data.add_last(elem)

    def __add__(self, other):
        self_cursor = self.data.trailer.prev
        other_cursor = other.data.trailer.prev
        sum_str = ""
        carry_over = 0

        for i in range(max(len(self.data),  len(other.data))):
            sum = 0

            if self_cursor.data is not None and other_cursor.data is not None:
                sum = str(int(self_cursor.data) + int(other_cursor.data) + int(carry_over))
                self_cursor = self_cursor.prev
                other_cursor = other_cursor.prev

            elif self_cursor.data is not None:  # add remaining nodes in self
                sum = str(int(self_cursor.data) + int(carry_over))
                self_cursor = self_cursor.prev

            elif other_cursor.data is not None:  # add remaining nodes in other
                sum = str(int(other_cursor.data) + int(carry_over))
                other_cursor = other_cursor.prev

            if len(sum) > 1:  # if sum is greater than or equal to 10
                carry_over = sum[0]
                sum_str = sum[1] + sum_str
            else:
                carry_over = 0

                if int(sum) != 0:
                    sum_str = sum + sum_str

        if int(carry_over) != 0:
            sum_str = carry_over + sum_str

        return Integer(sum_str)  # makes sum into DoublyLinkedList

    def __repr__(self):
        return "".join([str(item) for item in self.data])

    def __mul__(self, other):
        print(self.data, other.data)
        self_cursor = self.data.trailer.prev
        final_product = 0

        for i in range(len(self.data)):
            other_cursor = other.data.trailer.prev
            carry_over = 0
            tens_str = str(0) * i  # determines how many 0's go at end of solution

            for j in range(len(other.data)):
                sub_product = str((int(self_cursor.data)) * int(other_cursor.data) + int(carry_over))
                if len(sub_product) > 1:  # if sum is greater than or equal to 10
                    carry_over = sub_product[0]
                    tens_str = sub_product[1] + tens_str

                else:
                    carry_over = 0
                    tens_str = sub_product + tens_str

                other_cursor = other_cursor.prev

            self_cursor = self_cursor.prev

            if carry_over != 0:
                tens_str = carry_over + tens_str

            final_product += int(tens_str)

        return Integer(str(final_product))


