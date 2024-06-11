# "informal"/quick implementation just to check if I made this machine correctly on paper

n1 = 120
n2 = 45

b1 = format(n1, '#010b')[2:]
b2 = format(n2, '#010b')[2:]

print(b1, b2)

transition_table = {
    'q0': { '00': ('q0', 0), '01': ('q1', 1), '10': ('q0', 1), '11': ('q0', 0), },
    'q1': { '00': ('q1', 1), '01': ('q1', 0), '10': ('q0', 0), '11': ('q1', 1), }
} 

state = 'q0'
generated_output = ''
for l1, l2 in zip(reversed(b1), reversed(b2)):
    state, output = transition_table[state][l1+l2]
    generated_output += str(output)

print(int(''.join(list(reversed(generated_output))), 2))
