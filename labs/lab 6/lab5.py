import array
import random
class ArrayStack:
    def __init__(self, capacity):
        self.stack = array.array('i', [0] * capacity)
        self.top = -1
        self.capacity = capacity

    def push(self, item):
        """Task1: Implement Push and Pop. You can use is empty and is full to prevent error by raising and Exception. Don't forget to handle top"""
        if self.top < self.capacity - 1:
            self.top += 1
            self.stack[self.top] = item
        else:
            raise Exception("Stack is full")

    def pop(self):
        if self.top >= 0:
            item = self.stack[self.top]
            self.top -= 1
            return item
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1

def reverse_stack(stack):
    temp_stack = ArrayStack(stack.capacity)
    while not stack.is_empty():
        temp_stack.push(stack.pop())
    return temp_stack

def process_card_stack(cardStack):
    """Task3: This function accepts a stack of unqiue cards ranging from 1-13
    -The goal is create a solution stack where the cards are in order with 1 at the bottom and 13 at the top.
    -You pop the card stack 1 at a time
    see if you can place it on the solution stack. 
    -If you can't push it onto the discard
    -If you run out of cards, reverse discard and start again
    -continue until its sorted.
    -Check for Errors, None input, typererror, size"""
    if cardStack == None:
        raise TypeError
    if isinstance(cardStack, ArrayStack) == False:
        raise TypeError
    if cardStack.capacity != 13:
        raise ValueError

    solutionStack = ArrayStack(13)
    discardStack = ArrayStack(13)

    while cardStack.is_empty() == False:
        # pop out the first element
        tmp = cardStack.peek()
        cardStack.pop()
 
        # while temporary stack is not
        # empty and top of stack is
        # lesser than temp
        while solutionStack.is_empty() == False and int(solutionStack.peek()) < int(tmp):
            # pop from temporary stack and
            # push it to the input stack
            cardStack.push(solutionStack.peek())
            solutionStack.pop()
 
        # push temp in temporary of stack
        solutionStack.push(tmp)
         
    return reverse_stack(solutionStack)

# Example usage


cards = [3, 6, 4, 1, 2, 5, 9, 8, 7, 10, 13, 12, 11]
random.shuffle(cards)
cardStack = ArrayStack(13)
for card in cards:  # Example card stack
    cardStack.push(card)
# Process and print the solution stack
result = process_card_stack(cardStack)
while not result.is_empty():
    print(result.pop(), end=' ')

