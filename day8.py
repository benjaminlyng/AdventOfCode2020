import copy
with open('day8.txt', 'r') as day8:
    commands = day8.read().splitlines()

commands = {i: list(command.split()) for i, command in enumerate(commands)}

def run_commands(commandlist):
    EOF = len(commandlist)
    executed = set()
    acc = 0
    i = 0

    while i not in executed:
        executed.add(i)
        cmd = commandlist[i][0]
        val = int(commandlist[i][1])
        if  cmd == 'nop':
            i +=1
        elif cmd == 'acc':
            acc += val
            i +=1
        elif cmd == 'jmp':
            i += val
        if i == EOF:
            return acc, True  
    return acc, False

acc, completed = run_commands(commands)
print(f"Part 1 - {acc=}")

## Part 2:
done = False
i=-1

while not done:
    i +=1
    attempt = copy.deepcopy(commands)
    cmd = attempt[i][0]
    if cmd == 'jmp':
        attempt[i][0] = 'nop'
    elif cmd == 'nop':
        attempt[i][0] = 'jmp'
    else:
        continue
    
    acc, done = run_commands(attempt)
    


print(f"Part 2 - {acc=}")