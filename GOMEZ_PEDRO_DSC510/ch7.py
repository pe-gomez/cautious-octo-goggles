'''
fhand = open('mbox.txt')

print(fhand)  # <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>
inp = fhand.read()
print(len(inp))
print(inp[: 20])


fhand = open('mbox.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)



fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # Skip 'uninteresting lines'
    if not line.startswith('From:'):
        continue
    # Process our 'interesting' line
    print(line)


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)
'''

# class Error is derived from super class Exception
class Error(Exception):
    # Error is derived class for Exception, but
    # Base class for exceptions in this module
    pass


class TransitionError(Error):

    # Raised when an operation attempts a state
    # transition that's not allowed.
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex

        # Error message thrown is saved in msg
        self.msg = msg


try:
    raise (TransitionError(2,1 , "Not Allowed"))

# Value of Exception is stored in error
except TransitionError as error:
    print('Exception occured: ', error.msg)