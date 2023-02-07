class Insert:
    """
        This structure serves to be able to add an element at the beginning of a list.
        We do this by passing all elements of the list to the right.
    """
    def __init__(self):
        self.array = []

    def insertNum(self, element):
        index = len(self.array)
        while index >= 0:
            """
                We 'append' an element so that we can pass the others to the right, 
                otherwise this 'append' will give an error that exceeded the number of elements.
            """
            self.array.append(0)
            self.array[index] = self.array[index - 1]
            index -= 1

        self.array[0] = element

    def item(self, value):
        return self.array[value]

    """
        These other structures are reused from the 'Stack' structure.
    """
    def push(self, value):
        self.array.append(value)

    def len(self):
        return len(self.array)

    def peek(self):
        return self.array[len(self.array) - 1]
