import os
import sys


class RUNNER():

    def __init__(self, problem_statement=''):
        self.answer = None
        self.input = None
        self.part = None
        self.problem_statement = problem_statement

    def read_input(self, filename):
        self.input = []
        int_list = []
        with open(filename) as f:
            lines = f.readlines()
            for line in lines:
                line = [line[:6], line[6:10], line[10:15]]
                line = [int(x) for x in line]
                int_list += line

        if self.part is 1:
            while (len(int_list) > 0):
                triangle = []
                for i in range(3):
                    triangle += [int_list.pop(0)]
                self.input += [triangle]

        elif self.part is 2:
            while (len(int_list) > 0):
                triangles_3 = []
                for i in range(3):
                    triangle = []
                    for j in range(3):
                        triangle += [int_list.pop(0)]
                    triangles_3 += [triangle]
                rotated = list(zip(*triangles_3[::-1]))
                for i in range(3):
                    self.input += [rotated[i]]

    def setup(self, input=None, answer=None, part=0):
        self.part = part
        self.read_input(input)
        print('%s : \n%s' % (self.problem_statement, str(self.input)[:80]))

        self.result = self.solve(self.input)
        if (answer is not None):
            if (self.result == answer):
                print('UnitTest Passed!')
            else:
                print(
                    'UnitTest FAILED!   Correct answer is %s, Your result is %s.' %
                    (answer, self.result))

        else:
            print('                      Answer = %s' % self.result)

    def solve(self, input=None):
        self.result = 0
        for triangle in input:
            triangle = sorted(triangle)
            valid = True
            for i in [0]:
                if ((triangle[i %
                              3] + triangle[(i + 1) %
                                            3]) <= triangle[(i + 2) %
                                                            3]):
                    valid = False
            if valid:
                self.result += 1
        return str(self.result)


def main():
    runner = RUNNER(problem_statement='Find valid trianges')
    runner.setup(part=1, answer='1', input='day_3_input_unittest.txt')
    runner.setup(part=1, answer='983', input='day_3_input.txt')
    runner.setup(part=2, answer='3', input='day_3_input_unittest.txt')
    runner.setup(part=2, answer=None, input='day_3_input.txt')

    return

if __name__ == '__main__':
    main()
