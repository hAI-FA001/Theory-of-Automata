from functools import reduce
import re

tape = 'B'*20 + "B 10110 B 10001 B".replace(' ', '') + 'B'*20

state_table = {
    ('q0', '0'): ('0', 'r', 'q0'),
    ('q0', '1'): ('1', 'r', 'q0'),
    ('q0', 'B'): ('B', 'r', 'q1'),
    
    ('q1', '0'): ('0', 'r', 'q1'),
    ('q1', '1'): ('1', 'r', 'q1'),
    ('q1', 'B'): ('B', 'l', 'q2'),
    
    ('q2', '0'): ('1', 'l', 'q2'),
    ('q2', '1'): ('0', 'l', 'q3'),
    ('q2', 'B'): ('B', 'r', 'q5'),
    
    ('q3', '0'): ('0', 'l', 'q3'),
    ('q3', '1'): ('1', 'l', 'q3'),
    ('q3', 'B'): ('B', 'l', 'q4'), 
    
    ('q4', '0'): ('1', 'l', 'q4'),
    ('q4', '1'): ('0', 'r', 'q0'),
    ('q4', 'B'): ('B', 'r', 'q0'),
    
    ('q5', '0'): ('B', 'r', 'q5'),
    ('q5', '1'): ('B', 'r', 'q5'),
    ('q5', 'B'): ('B', 'l/r', 'q6'),
    
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
