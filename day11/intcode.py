#!/usr/bin/env python3

from termcolor import colored
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', help="Verbose mode", action = 'store_true')
args = parser.parse_args()

init_data = [3,8,1005,8,326,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,28,2,1104,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,55,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,77,2,103,7,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,102,1006,0,76,1,6,5,10,1,1107,3,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,135,1,1002,8,10,2,1101,3,10,1006,0,97,1,101,0,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,172,1006,0,77,1006,0,11,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,201,1006,0,95,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,226,2,3,16,10,1,6,4,10,1006,0,23,1006,0,96,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,261,1,3,6,10,2,1006,3,10,1006,0,78,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,295,1006,0,89,1,108,12,10,2,103,11,10,101,1,9,9,1007,9,1057,10,1005,10,15,99,109,648,104,0,104,1,21102,1,838365918100,1,21102,343,1,0,1106,0,447,21102,387365315476,1,1,21102,354,1,0,1106,0,447,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,179318254811,1,21102,401,1,0,1106,0,447,21102,1,97911876839,1,21101,0,412,0,1106,0,447,3,10,104,0,104,0,3,10,104,0,104,0,21101,838345577320,0,1,21101,435,0,0,1106,0,447,21102,1,838337188628,1,21101,0,446,0,1105,1,447,99,109,2,21202,-1,1,1,21101,40,0,2,21102,478,1,3,21101,0,468,0,1106,0,511,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,473,474,489,4,0,1001,473,1,473,108,4,473,10,1006,10,505,1102,1,0,473,109,-2,2106,0,0,0,109,4,2102,1,-1,510,1207,-3,0,10,1006,10,528,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21101,1,0,3,21102,1,547,0,1106,0,552,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,575,2207,-4,-2,10,1006,10,575,22102,1,-4,-4,1105,1,643,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,594,0,1105,1,552,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,613,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,635,22102,1,-1,1,21101,635,0,0,106,0,510,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

orientations = [[0, 1], [1, 0], [0, -1], [-1, 0]]

class Robot:
    def __init__(self):
        self.position = [0, 0]
        self.orientation = 0

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
    def __init__(self, data):
        self.data = data.copy()
        self.pc = 0
        self.base = 0
        self.output_values = []
        self.last_modified = -1
        self.exit = False
        self.white = set()
        self.painted = set()
        self.robot = Robot()

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
            input_value = 1 if tuple(self.robot.position) in self.white else 0
            print('Setting input to: %d' % input_value)
            r = insn.store(self.pc + 1, 0, input_value)
            self.pc += 2
            self.last_modified = r
        elif insn.opcode == 4:
            # WRITE
            output = insn.get_arg(self.pc + 1, 0)
            if args.verbose:
                print(colored('Output: %d' % output, 'red'))
            self.output_values.append(output)
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
            print('Exit')
            self.exit = True
        else:
            print('Unknown opcode: %d' % insn.opcode)
            assert False

    def run(self):
        step = 0
        self.print_data()
        self.last_output = None
        self.white.add((0, 0))
        counter = 1
        while True:
            step += 1
            if args.verbose:
                print('Step %d:' % step)
            r = self.process_one_instruction()
            if args.verbose:
                self.print_data()
            if len(self.output_values) == 2:
                self.painted.add(tuple(self.robot.position))
                t = tuple(self.robot.position)
                if self.output_values[0] == 1:
                    self.white.add(t)
                elif t in self.white:
                    self.white.remove(t)
                # print('white: %s' % str(sorted(list(self.white))))

                turn = self.output_values[1]
                if turn == 0:
                    self.robot.orientation = (self.robot.orientation + 3) % 4
                else:
                    self.robot.orientation = (self.robot.orientation + 1) % 4
                print('Robot #%d at %s, orientation: %d, color: %d' % (counter, str(self.robot.position), self.robot.orientation, self.output_values[0]))
                print()
                counter += 1
                self.robot.position[0] += orientations[self.robot.orientation][0]
                self.robot.position[1] += orientations[self.robot.orientation][1]
                self.output_values = []
            if self.exit:
                return self.last_output
program = Program(init_data)
program.run()

n = 80
matrix = [[False] * n for _ in range(n)]

print(len(program.painted))
print(program.white)

shift = 40
for w in program.white:
    matrix[w[0] + shift][w[1] + shift] = True

for m in matrix:
    for v in m:
        print('X' if v else ' ', end = '')
    print()
