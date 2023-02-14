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
            self.array.append("a")
            self.array[index] = self.array[index - 1]
            index -= 1
            
            """
                We eliminate the element that we 'append' because otherwise there would be a
                difference in size and we would have this unwanted element at the end of the array.
            """
            if "a" in self.array:
                self.array.pop()
            else:
                continue

        self.array[0] = element

    def deleteNum(self):
        """
            This server function to remove an item from the first position in array.
        """
        index = len(self.array)
        num = 0
        while num < (index - 1):
            self.array[num] = self.array[num + 1]
            num += 1

        self.array.pop()

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
