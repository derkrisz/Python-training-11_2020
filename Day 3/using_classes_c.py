class Word:
    '''
    It's a good idea to comment classes with docstrings
    Explain the nature of the classe, use-cases, properties and methods
    Also explain any overrides
    So here, we override equality
    '''
    def __init__(self, text):
        self.text = text
       # here we will define the 'check equality' operator
    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

if __name__ == '__main__':
    w1 = Word('ho')
    w2 = Word('Ho')
    print(w1 == w2) # calls the __eq__ in w2
    print(w1.__eq__(w2))
    print(w1.__doc__)