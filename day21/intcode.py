#!/usr/bin/env python3

import time
from termcolor import colored
import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', help="Verbose mode", action = 'store_true')
args = parser.parse_args()

init_data = [109,2050,21101,966,0,1,21101,13,0,0,1106,0,1378,21101,0,20,0,1106,0,1337,21101,0,27,0,1105,1,1279,1208,1,65,748,1005,748,73,1208,1,79,748,1005,748,110,1208,1,78,748,1005,748,132,1208,1,87,748,1005,748,169,1208,1,82,748,1005,748,239,21102,1,1041,1,21101,0,73,0,1106,0,1421,21101,0,78,1,21102,1041,1,2,21102,1,88,0,1106,0,1301,21102,68,1,1,21102,1041,1,2,21102,103,1,0,1105,1,1301,1102,1,1,750,1106,0,298,21101,0,82,1,21101,0,1041,2,21102,125,1,0,1106,0,1301,1102,2,1,750,1106,0,298,21101,79,0,1,21102,1,1041,2,21101,147,0,0,1106,0,1301,21101,84,0,1,21101,1041,0,2,21101,0,162,0,1105,1,1301,1101,3,0,750,1106,0,298,21101,0,65,1,21102,1,1041,2,21101,184,0,0,1106,0,1301,21102,1,76,1,21102,1,1041,2,21101,0,199,0,1106,0,1301,21102,75,1,1,21102,1041,1,2,21102,1,214,0,1105,1,1301,21102,221,1,0,1105,1,1337,21102,10,1,1,21102,1041,1,2,21101,236,0,0,1106,0,1301,1106,0,553,21101,0,85,1,21101,1041,0,2,21101,254,0,0,1105,1,1301,21101,0,78,1,21101,1041,0,2,21101,0,269,0,1105,1,1301,21102,276,1,0,1106,0,1337,21101,10,0,1,21102,1041,1,2,21102,291,1,0,1105,1,1301,1102,1,1,755,1106,0,553,21102,32,1,1,21102,1,1041,2,21102,1,313,0,1105,1,1301,21102,320,1,0,1105,1,1337,21101,0,327,0,1105,1,1279,2102,1,1,749,21101,0,65,2,21101,0,73,3,21102,1,346,0,1105,1,1889,1206,1,367,1007,749,69,748,1005,748,360,1102,1,1,756,1001,749,-64,751,1106,0,406,1008,749,74,748,1006,748,381,1101,0,-1,751,1106,0,406,1008,749,84,748,1006,748,395,1102,-2,1,751,1106,0,406,21102,1100,1,1,21101,0,406,0,1105,1,1421,21102,1,32,1,21102,1100,1,2,21102,1,421,0,1106,0,1301,21102,1,428,0,1106,0,1337,21102,435,1,0,1106,0,1279,1202,1,1,749,1008,749,74,748,1006,748,453,1101,-1,0,752,1105,1,478,1008,749,84,748,1006,748,467,1102,1,-2,752,1105,1,478,21101,1168,0,1,21101,0,478,0,1106,0,1421,21101,0,485,0,1105,1,1337,21101,0,10,1,21102,1,1168,2,21102,500,1,0,1105,1,1301,1007,920,15,748,1005,748,518,21101,0,1209,1,21102,1,518,0,1105,1,1421,1002,920,3,529,1001,529,921,529,101,0,750,0,1001,529,1,537,1002,751,1,0,1001,537,1,545,1001,752,0,0,1001,920,1,920,1106,0,13,1005,755,577,1006,756,570,21101,0,1100,1,21102,1,570,0,1105,1,1421,21102,1,987,1,1106,0,581,21102,1,1001,1,21102,1,588,0,1106,0,1378,1102,758,1,593,1001,0,0,753,1006,753,654,21001,753,0,1,21101,610,0,0,1105,1,667,21101,0,0,1,21101,621,0,0,1106,0,1463,1205,1,647,21101,0,1015,1,21101,635,0,0,1106,0,1378,21101,0,1,1,21102,646,1,0,1106,0,1463,99,1001,593,1,593,1105,1,592,1006,755,664,1101,0,0,755,1106,0,647,4,754,99,109,2,1101,726,0,757,21202,-1,1,1,21101,0,9,2,21101,0,697,3,21101,692,0,0,1106,0,1913,109,-2,2106,0,0,109,2,1002,757,1,706,2102,1,-1,0,1001,757,1,757,109,-2,2105,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,255,63,95,223,127,159,191,0,207,172,59,187,107,162,236,121,43,242,102,118,61,87,163,196,200,214,84,197,120,103,93,168,58,217,237,69,155,184,86,188,190,55,228,220,106,79,71,227,246,138,141,39,212,202,108,60,38,177,50,203,247,238,158,113,167,181,70,213,46,153,34,49,47,119,116,94,221,252,98,182,198,42,226,235,241,109,110,68,115,239,92,125,143,152,117,136,78,51,54,114,206,53,229,248,85,137,100,254,35,101,123,215,219,186,189,218,249,253,232,201,205,204,234,233,178,199,216,171,62,244,179,99,222,251,140,230,77,139,173,142,57,174,169,183,126,185,166,154,157,156,175,124,250,56,76,170,245,111,231,243,122,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,73,110,112,117,116,32,105,110,115,116,114,117,99,116,105,111,110,115,58,10,13,10,87,97,108,107,105,110,103,46,46,46,10,10,13,10,82,117,110,110,105,110,103,46,46,46,10,10,25,10,68,105,100,110,39,116,32,109,97,107,101,32,105,116,32,97,99,114,111,115,115,58,10,10,58,73,110,118,97,108,105,100,32,111,112,101,114,97,116,105,111,110,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,78,68,44,32,79,82,44,32,111,114,32,78,79,84,67,73,110,118,97,108,105,100,32,102,105,114,115,116,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,115,111,109,101,116,104,105,110,103,32,108,105,107,101,32,65,44,32,66,44,32,67,44,32,68,44,32,74,44,32,111,114,32,84,40,73,110,118,97,108,105,100,32,115,101,99,111,110,100,32,97,114,103,117,109,101,110,116,59,32,101,120,112,101,99,116,101,100,32,74,32,111,114,32,84,52,79,117,116,32,111,102,32,109,101,109,111,114,121,59,32,97,116,32,109,111,115,116,32,49,53,32,105,110,115,116,114,117,99,116,105,111,110,115,32,99,97,110,32,98,101,32,115,116,111,114,101,100,0,109,1,1005,1262,1270,3,1262,21002,1262,1,0,109,-1,2105,1,0,109,1,21101,1288,0,0,1106,0,1263,21001,1262,0,0,1101,0,0,1262,109,-1,2105,1,0,109,5,21102,1,1310,0,1106,0,1279,22101,0,1,-2,22208,-2,-4,-1,1205,-1,1332,21201,-3,0,1,21101,0,1332,0,1106,0,1421,109,-5,2105,1,0,109,2,21101,0,1346,0,1106,0,1263,21208,1,32,-1,1205,-1,1363,21208,1,9,-1,1205,-1,1363,1106,0,1373,21101,0,1370,0,1106,0,1279,1106,0,1339,109,-2,2105,1,0,109,5,2102,1,-4,1386,20102,1,0,-2,22101,1,-4,-4,21101,0,0,-3,22208,-3,-2,-1,1205,-1,1416,2201,-4,-3,1408,4,0,21201,-3,1,-3,1105,1,1396,109,-5,2106,0,0,109,2,104,10,22101,0,-1,1,21101,1436,0,0,1105,1,1378,104,10,99,109,-2,2105,1,0,109,3,20002,593,753,-1,22202,-1,-2,-1,201,-1,754,754,109,-3,2105,1,0,109,10,21101,0,5,-5,21102,1,1,-4,21101,0,0,-3,1206,-9,1555,21101,0,3,-6,21102,1,5,-7,22208,-7,-5,-8,1206,-8,1507,22208,-6,-4,-8,1206,-8,1507,104,64,1106,0,1529,1205,-6,1527,1201,-7,716,1515,21002,0,-11,-8,21201,-8,46,-8,204,-8,1105,1,1529,104,46,21201,-7,1,-7,21207,-7,22,-8,1205,-8,1488,104,10,21201,-6,-1,-6,21207,-6,0,-8,1206,-8,1484,104,10,21207,-4,1,-8,1206,-8,1569,21101,0,0,-9,1105,1,1689,21208,-5,21,-8,1206,-8,1583,21101,1,0,-9,1105,1,1689,1201,-5,716,1588,21002,0,1,-2,21208,-4,1,-1,22202,-2,-1,-1,1205,-2,1613,22101,0,-5,1,21101,1613,0,0,1106,0,1444,1206,-1,1634,21201,-5,0,1,21102,1,1627,0,1105,1,1694,1206,1,1634,21102,2,1,-3,22107,1,-4,-8,22201,-1,-8,-8,1206,-8,1649,21201,-5,1,-5,1206,-3,1663,21201,-3,-1,-3,21201,-4,1,-4,1106,0,1667,21201,-4,-1,-4,21208,-4,0,-1,1201,-5,716,1676,22002,0,-1,-1,1206,-1,1686,21101,0,1,-4,1105,1,1477,109,-10,2105,1,0,109,11,21102,0,1,-6,21101,0,0,-8,21101,0,0,-7,20208,-6,920,-9,1205,-9,1880,21202,-6,3,-9,1201,-9,921,1725,20101,0,0,-5,1001,1725,1,1733,20102,1,0,-4,21201,-4,0,1,21101,1,0,2,21101,9,0,3,21101,1754,0,0,1105,1,1889,1206,1,1772,2201,-10,-4,1766,1001,1766,716,1766,21001,0,0,-3,1106,0,1790,21208,-4,-1,-9,1206,-9,1786,22101,0,-8,-3,1106,0,1790,22102,1,-7,-3,1001,1733,1,1796,20101,0,0,-2,21208,-2,-1,-9,1206,-9,1812,21201,-8,0,-1,1106,0,1816,21201,-7,0,-1,21208,-5,1,-9,1205,-9,1837,21208,-5,2,-9,1205,-9,1844,21208,-3,0,-1,1105,1,1855,22202,-3,-1,-1,1106,0,1855,22201,-3,-1,-1,22107,0,-1,-1,1106,0,1855,21208,-2,-1,-9,1206,-9,1869,22102,1,-1,-8,1105,1,1873,22102,1,-1,-7,21201,-6,1,-6,1105,1,1708,21202,-8,1,-10,109,-11,2105,1,0,109,7,22207,-6,-5,-3,22207,-4,-6,-2,22201,-3,-2,-1,21208,-1,0,-6,109,-7,2106,0,0,0,109,5,2102,1,-2,1912,21207,-4,0,-1,1206,-1,1930,21102,0,1,-4,21202,-4,1,1,22102,1,-3,2,21101,0,1,3,21102,1949,1,0,1106,0,1954,109,-5,2106,0,0,109,6,21207,-4,1,-1,1206,-1,1977,22207,-5,-3,-1,1206,-1,1977,22101,0,-5,-5,1105,1,2045,21202,-5,1,1,21201,-4,-1,2,21202,-3,2,3,21101,1996,0,0,1106,0,1954,22102,1,1,-5,21102,1,1,-2,22207,-5,-3,-1,1206,-1,2015,21102,0,1,-2,22202,-3,-2,-3,22107,0,-4,-1,1206,-1,2037,22102,1,-2,1,21102,1,2037,0,105,1,1912,21202,-3,-1,-3,22201,-5,-3,-5,109,-6,2105,1,0]

moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
inverse_moves = {1: 2, 2: 1, 3: 4, 4:3}

opcode_names = {
        1: 'ADD',
        2: 'MULT',
        3: 'READ',
        4: 'WRITE',
        5: 'JMPEQ',
        6: 'JMPNEQ',
        7: 'LT',
        8: 'EQ',
        9: 'SET BASE',
        99: 'EXIT'
}

class Instruction:
    def __init__(self, program, insn):
        self.program = program 
        self.raw = insn
        self.modes = [0, 0, 0, 0]
        if insn >= 100:
            self.opcode = insn % 100
            modes = int(insn / 100)
            i = 0
            while modes > 0:
                self.modes[i] = modes % 10
                modes = int(modes / 10)
                i += 1
        else:
            self.opcode = insn

    def extend(self, index):
        while len(self.program.data) <= index:
            self.program.data.append(0)

    def get_arg(self, arg, mode_index):
        mode = self.modes[mode_index]
        index = None
        if mode == 0:
            index = self.program.data[arg]
        elif mode == 1:
            index = arg
        elif mode == 2:
            index = self.program.data[arg] + self.program.base
        else:
            assert False
        self.extend(index)
        if args.verbose:
            print('  getting at data[%d]=%d' % (index, self.program.data[index]))
        return self.program.data[index]

    def store(self, arg, mode_index, value):
        mode = self.modes[mode_index]
        index = None
        index = None
        if mode == 0:
            index = self.program.data[arg]
        elif mode == 1:
            assert False
        elif mode == 2:
            index = self.program.data[arg] + self.program.base
        else:
            assert False

        self.extend(index)
        self.program.data[index] = value
        if args.verbose:
            print('  storing at data[%d]=%d' % (index, value))
        return index

    def print(self):
        print('pc: %d, base: %d, raw: %d, opcode: %d (%s), modes: %s' % (self.program.pc, self.program.base, self.raw, self.opcode, opcode_names[self.opcode], str(self.modes)))

class Program:
    def __init__(self, data, input):
        self.data = data.copy()
        self.pc = 0
        self.base = 0
        self.last_modified = -1
        self.input = input
        self.mycode = input
        self.output = ''
        self.exit = False

    def print_data(self):
        for i, v in enumerate(self.data):
            if i == self.pc:
                print(colored('PC:', 'blue'), end = '')
            if i == self.last_modified:
                print(colored(v, 'red'), end = '')
            else:
                print(v, end = '')
            print(',', end = '')
        print()

    def process_one_instruction(self):
        self.last_modified = -1
        insn = Instruction(self, self.data[self.pc])
        if args.verbose:
            insn.print()
        if insn.opcode == 1:
            # ADD 
            r = insn.store(self.pc + 3, 2, insn.get_arg(self.pc + 1, 0) + insn.get_arg(self.pc + 2, 1))
            self.pc += 4
            self.last_modified = r
        elif insn.opcode == 2:
            # MULT
            r = insn.store(self.pc + 3, 2, insn.get_arg(self.pc + 1, 0) * insn.get_arg(self.pc + 2, 1))
            self.pc += 4
            self.last_modified = r
        elif insn.opcode == 3:
            # READ
            # print('Setting input to: %d' % self.last_input)
            input = ord(self.input[0])
            self.input = self.input[1:]
            r = insn.store(self.pc + 1, 0, input)
            self.pc += 2
            self.last_modified = r
        elif insn.opcode == 4:
            # WRITE
            output = insn.get_arg(self.pc + 1, 0)
            if output > 1000:
                print(output)
                print(self.mycode)
                exit(0)
            self.output += chr(output)
            if args.verbose:
                print(colored('Output: %d' % output, 'red'))
            self.pc += 2
        elif insn.opcode == 5 or insn.opcode == 6:
            # EQ/NEQ
            cmp = insn.get_arg(self.pc + 1, 0)
            if insn.opcode == 6:
                cmp = not cmp
            if cmp:
                self.pc = insn.get_arg(self.pc + 2, 1)
            else:
                self.pc += 3
        elif insn.opcode == 7:
            # LT
            r = int(insn.get_arg(self.pc + 1, 0) < insn.get_arg(self.pc + 2, 1))
            r = insn.store(self.pc + 3, 2, r)
            self.pc += 4
            self.last_modified = r
        elif insn.opcode == 8:
            # EQ
            r = int(insn.get_arg(self.pc + 1, 0) == insn.get_arg(self.pc + 2, 1))
            r = insn.store(self.pc + 3, 2, r)
            self.pc += 4
            self.last_modified = r
        elif insn.opcode == 9:
            # SET BASE
            self.base += insn.get_arg(self.pc + 1, 0)
            self.pc += 2
        elif insn.opcode == 99:
            # print('Exit')
            self.exit = True
        else:
            print('Unknown opcode: %d' % insn.opcode)
            assert False

    def run(self):
        step = 0
        #self.print_data()
        self.last_output = None
        counter = 1
        while True:
            step += 1
            if args.verbose:
                print('Step %d:' % step)
            r = self.process_one_instruction()
            if args.verbose:
                self.print_data()
            if self.exit:
                return

all_inputs = []
functions = [lambda x, y: x & y, lambda x, y: x | y, lambda x, y: not x]

def gen_all_inputs(n, inputs, result):
    if n == 0:
        result.append(inputs.copy())
    else:
        if len(inputs) == 0 or len(inputs) == 1:
            inputs.append(False)
            gen_all_inputs(n - 1, inputs, result)
            inputs.pop()
        else:
            for i in [False, True]:
                inputs.append(i)
                gen_all_inputs(n - 1, inputs, result)
                inputs.pop()

gen_all_inputs(11, [], all_inputs)
print(all_inputs)

def get_value(insns, registers):
    registers = list(registers)
    for insn in insns:
        op1 = insn[1]
        op2 = insn[2]
        opcode = insn[0]
        fn = functions[opcode]
        assert op2 <= 1
        registers[op2] = fn(registers[op1], registers[op2])
    return registers[0]

def get_all_results(insns):
    r = []
    for i in all_inputs:
        r.append(get_value(insns, i))
    return r

def tocode(insns):
    code = ''
    opcodes = ['AND', 'OR', 'NOT']
    registers = 'JTABCDEFGHI'
    for i in insns:
        code += '%s %s %s\n' % (opcodes[i[0]], registers[i[1]], registers[i[2]])
    return code + 'WALK\n'

all_instructions = []
for opcode in range(3):
    for op1 in range(6+5-5):
        for op2 in range(2):
            if opcode != 2 and op1 == op2:
                continue
            all_instructions.append((opcode, op1, op2))
print(all_instructions)
print(len(all_instructions))

def testall(n, selection, known):
    if n == 0:
        code = [all_instructions[i] for i in selection]
        r = get_all_results(code)
        r = tuple(r)
        if not r in known:
            print('New %d: %s' % (len(known), str(r)))
            known.add(r)
            source = tocode(code)
            print(source)
            program = Program(init_data, source)
            program.run()
            print(program.output)
            assert "Didn't" in program.output
    else:
        for i in range(len(all_instructions)):
            selection.append(i)
            testall(n - 1, selection, known)
            selection.pop()

def toregisters(s):
    assert len(s) == 4
    return tuple([False, False] + [x == '#' for x in s])

asserts = [(toregisters('###.'), False),
        (toregisters('.###'), True),
        (toregisters('...#'), True),
        (toregisters('#..#'), True),
        (toregisters('##..'), False),
        ]

def verify_code(code):
    for a in asserts:
        if get_value(code, a[0]) != a[1]:
            return False
    return True

#####...#########
#####.###########
#####..#.########

import random
random.seed(0)
def test_random(n, known, holes, c):
    if c % 100 == 0:
        print(c)
    code = [random.choice(all_instructions) for _ in range(n)]
    if not verify_code(code):
        return
    r = get_all_results(code)
    r = tuple(r)
    if not r in known:
        known.add(r)
        source = tocode(code)
        program = Program(init_data, source)
        program.run()
        end = program.output.strip().split('\n')[-1]
        end = end.replace('@', '.')
        if not end in holes:
            print(end)
            holes.add(end)
            print('New %d: %s' % (len(known), str()))
        assert "Didn't" in program.output

known = set()
holes = set()
c = 0
while True:
    c += 1
    test_random(4, known, holes, c)

code = '''OR H T
OR D J
AND T J
NOT I T
OR T J
RUN
'''

program = Program(init_data, code)
program.run()
print(program.output)

# code = [(1, 2, 0), (1, 3, 1), (0, 1, 0)]
# print(get_all_results(code))
exit(0)


insns = ['AND', 'OR', 'NOT']
inputs = ['ABCDJT', 'JT']
all_instructions = []
for insn in insns:
    for op1 in inputs[0]:
        for op2 in inputs[1]:
            all_instructions.append('%s %s %s' % (insn, op1, op2))

print(all_instructions)
print(len(all_instructions))


program = Program(init_data, 'OR B J\nWALK\n')
program.run()
print(program.output)

exit(0)

def generate_random_program(n):
    output = []
    for i in range(n):
        output.append(random.choice(all_instructions))
    return '\n'.join(output) + '\nWALK\n'

maximum = 0
for i in range(5000):
    code = generate_random_program(6)
    program = Program(init_data, code)
    program.run()
    result = not 'Didn' in program.output
    assert not result
    ats = len([x for x in program.output if x == '@'])
    print('Len: %d' % (ats))
    print(program.output)
    if ats > maximum:
        maximum = ats
        print(code)
        print(program.output)
