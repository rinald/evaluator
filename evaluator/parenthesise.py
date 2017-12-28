priority = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
    '^': 2
}

class Operation:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

        self.grouped = False

    def __str__(self):
        return '({}{}{})'.format(self.left, self.operator, self.right)

    def __repr__(self):
        return self.__str__()

class Lexer:
    def __init__(self, expression):
        self.expression = expression
        self.cursor_position = 0
        self.read_position = 0
        self.current_character = expression[0]

    def read_character(self):
        self.read_position += 1

        if self.read_position <= (len(self.expression) - 1):
            self.current_character = self.expression[self.read_position]
        else:
            self.current_character = ''

    def get_integer(self):
        while self.current_character.isdigit():
            self.read_character()
        integer = self.expression[self.cursor_position:self.read_position]
        self.cursor_position = self.read_position

        return integer

    def get_operator(self):
        operator = self.current_character
        self.read_character()
        self.cursor_position = self.read_position

        return operator

    def get_next(self):
        if self.current_character == '':
            return None

        if self.current_character.isdigit():
            next = self.get_integer()
        else:
            next = self.get_operator()

        return next

def get_previous(operations, current):
    if current == 0:
        return None

    while current > 0:
        if operations[current-1].grouped:
            current -= 1
        else:
            break
    if current == 0:
        return None
    else:
        return current-1

def get_next(operations, current):
    if current == (len(operations) - 1):
        return None
    
    while current < (len(operations) - 1):
        if operations[current+1].grouped:
            current += 1
        else:
            break
    if current == (len(operations) - 1):
        return None
    else:
        return current+1

def parenthesise(expression):
    current = 0
    current_priority = 0
    next_priority = 0
    operands = []
    operators = []
    operations = []

    # Initialise operations
    lexer = Lexer(expression)

    while True:
        token = lexer.get_next()

        if token is None:
            break

        if token.isnumeric():
            operands.append(token)
        else:
            operators.append(token)

    for i in range(len(operators)):
        operations.append(Operation(operands[i], operators[i], operands[i+1]))

    while not (get_previous(operations, current) == None and get_next(operations, current) == None):
        current_priority = priority[operations[current].operator]
        if get_next(operations, current) != None:
            next_priority = priority[operations[get_next(operations, current)].operator]
        else:
            next_priority = 0

        if current_priority >= next_priority:
            operations[current].grouped = True
            if get_previous(operations, current) != None:
                operations[get_previous(operations, current)].right = str(operations[current])
            if get_next(operations, current) != None:
                operations[get_next(operations, current)].left = str(operations[current])
            current = get_next(operations, -1)
        else:
            current = get_next(operations, current)

    return str(operations[current])

if __name__ == '__main__':
    expression = '1+2+3'
    parenthesise(expression)

