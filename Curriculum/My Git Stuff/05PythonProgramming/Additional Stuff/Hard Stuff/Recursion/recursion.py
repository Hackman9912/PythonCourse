'''
https://github.com/CyberTrainingUSAF/05-Python-Programming/blob/master/03_Flow_Control/08_recursion.md

a funciton that calls itself and will call itself until the exit condition is met

Depth of the recursion is the number of times a function calls itself

Base case is the problem can be solved now and the function solves it and returns

Recursive Case

If the problem cannot be solved now, then the function reduces it to smaller similar problems and calls itself to solve the smaller problem.

'''


def forever_recursion():
    annoying_message(int(input('How many times do you want to do it? ')))

def annoying_message(count):
    if count > 0:
        print(count, 'Nudge Nudge, Wink Wink, Say No More Say No More')
        annoying_message(count - 1)

forever_recursion()