import os
import sys

INPUT = 'R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5'
# INPUT = 'R2, R2, R2'
# INPUT = 'R5, L5, R5, R3'
# INPUT = 'R8, R4, R4, R8'


# class unittest():

class RUNNER():

    def __init__(self, input=None):
        self.answer = None
        self.input = input
        self.history = set()
        self.distance = [0, 0]
        self.heading = 0

    # def setup_unittest(self):
    #   unittest_input = [(None, None)]
    #   unittest_input =

    def update_path_history(self):
        location = (self.distance[0], self.distance[1])
        if location in self.history:
            self.answer = abs(self.distance[0]) + abs(self.distance[1])
            print(
                'you have been at %s before! %d steps' %
                (str(location), self.answer))
        else:
            self.history.add(location)

    def find_shortest_path(self):
        input_list = self.input.split(', ')
        while (len(input_list) > 0):
            cmd = input_list.pop(0)
            turn = cmd[0]
            dist = int(cmd[1:])

            # find heading
            if turn is 'R':
                self.heading += 1
            elif turn is 'L':
                self.heading -= 1
            self.heading = self.heading % 4

            if self.heading is 0:
                for x in range(0, dist):
                    self.distance[0] += 1
                    self.update_path_history()
                print('walk north %d' % dist)
            elif self.heading is 1:
                for y in range(0, dist):
                    self.distance[1] += 1
                    self.update_path_history()
                    # distance[1] += dist
                print('walk east  %d' % dist)
            elif self.heading is 2:
                for x in range(0, dist):
                    self.distance[0] -= 1
                    self.update_path_history()
                print('walk south %d' % dist)
            elif self.heading is 3:
                for y in range(0, dist):
                    self.distance[1] -= 1
                    self.update_path_history()
                print('walk west  %d' % dist)

        directions = ['', '']
        directions[0] = 'Walk %s%d' % ("North" if self.distance[
                                       0] >= 0 else "South", self.distance[0])
        directions[1] = 'Walk %s%d' % ("East" if self.distance[
                                       1] >= 0 else "West", self.distance[1])
        print("%s, %s" % (directions[0], directions[1]))

        self.answer = abs(self.distance[0]) + abs(self.distance[1])
        return self.answer


def main():
    print('Find Shorted Path on Grid for INPUT: \n%s' % INPUT[:50])
    runner = RUNNER(input=INPUT)
    runner.find_shortest_path()
    print("Shortest Path =  %s" % runner.answer)
    return

if __name__ == '__main__':
    main()
    pass
