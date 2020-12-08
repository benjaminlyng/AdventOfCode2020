
with open('day8.txt', 'r') as day8:
    commands = day8.read().splitlines()

commands = {i: tuple(command.split()) for i, command in enumerate(commands)}
EOF = len(commands)
executed = set()
acc = 0
i = 0

while i not in executed and i<=EOF:
    executed.add(i)
    cmd = commands[i][0]
    val = int(commands[i][1])
    if  cmd == 'nop':
        i +=1
    elif cmd == 'acc':
        acc += val
        i +=1
    elif cmd == 'jmp':
        i += val
    
print(f"Part 1 - {acc=}")