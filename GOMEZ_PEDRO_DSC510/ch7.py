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

'''
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)

