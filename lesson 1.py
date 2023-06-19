'''
def strcounter(string):
    for symbol in string:
        counter = 0
        for syb_symbol in string:
            if symbol == syb_symbol:
                counter += 1
        print(symbol, counter)
strcounter('aaabbbcccdddeee')
'''

'''
def strcounter(string):
    for symbol in set(string):
        counter = 0
        for syb_symbol in string:
            if symbol == syb_symbol:
                counter += 1
        print(symbol, counter)


strcounter('aaabbbcccdddeee')
'''
'''
def strcounter(string):
    syms_counter = {}
    for symbol in string:
        syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
    print(syms_counter)
strcounter('aaabbbcccdddeee')
'''
word = input('Введите слово для проверки: ')

if word == word[::-1]:
    print(True)
else:
    print(False)
