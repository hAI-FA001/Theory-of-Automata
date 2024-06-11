from functools import reduce
import re

tape = 'B'*20 + "B 1111 1111 1111 1111 B".replace(' ', '') + 'B'*20

state_table = {
    ('q0', '1'): ('1', 'r', 'q0'),
    ('q0', 'B'): ('B', 'l', 'q1'),
    
    ('q1', '1'): ('x', 'r', 'q2'),
    ('q1', 'B'): ('B', 'r', 'q5'),
    
    ('q2', '0'): ('0', 'r', 'q2'),
    ('q2', '1'): ('1', 'r', 'q2'),
    ('q2', 'B'): ('B', 'l', 'q3'),
    
    ('q3', '0'): ('1', 'l', 'q4'),
    ('q3', '1'): ('0', 'l', 'q3'),
    ('q3', 'x'): ('1', 'l', 'q1'),
    
    ('q4', '0'): ('0', 'l', 'q4'),
    ('q4', '1'): ('1', 'l', 'q4'),
    ('q4', 'x'): ('0', 'l', 'q1'),
    ('q4', 'B'): ('B', 'r', 'q5'),
    
    ('q5', '0'): ('B', 'r', 'q5'),
    ('q5', '1'): ('1', 'l/r', 'q6'),
    
    ('q6', ''): ('', '', '')
}

halt = False
cur_pos = re.search('[01]', tape).start()
tape = list(tape)
state = 'q0'
while not halt:
    cur_input = tape[cur_pos]
    write, move, state = state_table[(state, cur_input)]
    
    tape[cur_pos] = write
    
    if move == 'r': cur_pos += 1
    elif move == 'l': cur_pos -= 1
    elif move == 'l/r': halt = True


print(reduce(lambda aggregate, item: aggregate + item, tape, '').replace('B', ''))
