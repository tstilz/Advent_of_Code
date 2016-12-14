import os
import sys

INPUT = ['RDLULDLDDRLLLRLRULDRLDDRRRRURLRLDLULDLDLDRULDDLLDRDRUDLLDDRDULLLULLDULRRLDURULDRUULLLUUDURURRDDLDLDRRDDLRURLLDRRRDULDRULURURURURLLRRLUDULDRULLDURRRLLDURDRRUUURDRLLDRURULRUDULRRRRRDLRLLDRRRDLDUUDDDUDLDRUURRLLUDUDDRRLRRDRUUDUUULDUUDLRDLDLLDLLLLRRURDLDUURRLLDLDLLRLLRULDDRLDLUDLDDLRDRRDLULRLLLRUDDURLDLLULRDUUDRRLDUDUDLUURDURRDDLLDRRRLUDULDULDDLLULDDDRRLLDURURURUUURRURRUUDUUURULDLRULRURDLDRDDULDDULLURDDUDDRDRRULRUURRDDRLLUURDRDDRUDLUUDURRRLLRR',
         'RDRRLURDDDDLDUDLDRURRLDLLLDDLURLLRULLULUUURLDURURULDLURRLRULDDUULULLLRLLRDRRUUDLUUDDUDDDRDURLUDDRULRULDDDLULRDDURRUURLRRLRULLURRDURRRURLDULULURULRRLRLUURRRUDDLURRDDUUDRDLLDRLRURUDLDLLLLDLRURDLLRDDUDDLDLDRRDLRDRDLRRRRUDUUDDRDLULUDLUURLDUDRRRRRLUUUDRRDLULLRRLRLDDDLLDLLRDDUUUUDDULUDDDUULDDUUDURRDLURLLRUUUUDUDRLDDDURDRLDRLRDRULRRDDDRDRRRLRDULUUULDLDDDUURRURLDLDLLDLUDDLDLRUDRLRLDURUDDURLDRDDLLDDLDRURRULLURULUUUUDLRLUUUDLDRUDURLRULLRLLUUULURLLLDULLUDLLRULRRLURRRRLRDRRLLULLLDURDLLDLUDLDUDURLURDLUURRRLRLLDRLDLDRLRUUUDRLRUDUUUR',
         'LLLLULRDUUDUUDRDUUURDLLRRLUDDDRLDUUDDURLDUDULDRRRDDLLLRDDUDDLLLRRLURDULRUUDDRRDLRLRUUULDDULDUUUDDLLDDDDDURLDRLDDDDRRDURRDRRRUUDUUDRLRRRUURUDURLRLDURDDDUDDUDDDUUDRUDULDDRDLULRURDUUDLRRDDRRDLRDLRDLULRLLRLRLDLRULDDDDRLDUURLUUDLLRRLLLUUULURUUDULRRRULURUURLDLLRURUUDUDLLUDLDRLLRRUUDDRLUDUDRDDRRDDDURDRUDLLDLUUDRURDLLULLLLUDLRRRUULLRRDDUDDDUDDRDRRULURRUUDLUDLDRLLLLDLUULLULLDDUDLULRDRLDRDLUDUDRRRRLRDLLLDURLULUDDRURRDRUDLLDRURRUUDDDRDUUULDURRULDLLDLDLRDUDURRRRDLDRRLUDURLUDRRLUDDLLDUULLDURRLRDRLURURLUUURRLUDRRLLULUULUDRUDRDLUL',
         'LRUULRRUDUDDLRRDURRUURDURURLULRDUUDUDLDRRULURUDURURDRLDDLRUURLLRDLURRULRRRUDULRRULDLUULDULLULLDUDLLUUULDLRDRRLUURURLLUUUDDLLURDUDURULRDLDUULDDRULLUUUURDDRUURDDDRUUUDRUULDLLULDLURLRRLRULRLDLDURLRLDLRRRUURLUUDULLLRRURRRLRULLRLUUDULDULRDDRDRRURDDRRLULRDURDDDDDLLRRDLLUUURUULUDLLDDULDUDUUDDRURDDURDDRLURUDRDRRULLLURLUULRLUDUDDUUULDRRRRDLRLDLLDRRDUDUUURLRURDDDRURRUDRUURUUDLRDDDLUDLRUURULRRLDDULRULDRLRLLDRLURRUUDRRRLRDDRLDDLLURLLUDL',
         'ULURLRDLRUDLLDUDDRUUULULUDDDDDRRDRULUDRRUDLRRRLUDLRUULRDDRRLRUDLUDULRULLUURLLRLLLLDRDUURDUUULLRULUUUDRDRDRUULURDULDLRRULUURURDULULDRRURDLRUDLULULULUDLLUURULDLLLRDUDDRRLULUDDRLLLRURDDLDLRLLLRDLDRRUUULRLRDDDDRUDRUULDDRRULLDRRLDDRRUDRLLDUDRRUDDRDLRUDDRDDDRLLRDUULRDRLDUDRLDDLLDDDUUDDRULLDLLDRDRRUDDUUURLLUURDLULUDRUUUDURURLRRDULLDRDDRLRDULRDRURRUDLDDRRRLUDRLRRRRLLDDLLRLDUDUDDRRRUULDRURDLLDLUULDLDLDUUDDULUDUDRRDRLDRDURDUULDURDRRDRRLLRLDLU']

class RUNNER():
    def __init__(self):
      self.answer = None
      self.input = None
      self.part = None

    def setup(self, input=None, answer=None, part=0):
        self.input = input
        self.part = part
        self.result = self.solve(input)
        if (answer is not None):
            if (self.result == answer):
                print ('UnitTest Passed!')
            else:
                print ('UnitTest FAILED!   Correct answer is %s, Your result is %s.' % (answer, self.result))

        else:
           print ('                      Answer = %s' % self.result)

    def update_finger_pos(self, cmd):
        prev_x = self.finger_pos['x']
        prev_y = self.finger_pos['y']

        # Move Finger
        if cmd == 'U':
            self.finger_pos['y'] -=1
        if cmd == 'D':
            self.finger_pos['y'] +=1

        if cmd == 'R':
            self.finger_pos['x'] +=1
        if cmd == 'L':
            self.finger_pos['x'] -=1

        # Boundry Checks
        try:
            self.keypad[(self.finger_pos['x'],self.finger_pos['y'])]
        except KeyError:
            self.finger_pos['x'] = prev_x
            self.finger_pos['y'] = prev_y

    def set_start_button(self):
        if self.part is 1:
            self.finger_pos = {'x':1, 'y':1}
        elif self.part is 2:
            self.finger_pos = {'x':0, 'y':2}


    def generate_keypad(self):
        if self.part is 1:
            self.keypad = dict()
            key_num = 1
            for y in range(3):
                for x in range(3):
                    self.keypad.update({(x,y):hex(key_num)[2:].upper()})
                    key_num += 1
                    # print ('finger=(%d,%d), button=%s' %(x,y,self.keypad[(x,y)]))

        elif self.part is 2:
            self.keypad = dict()
            key_num = 1
            for y in range(5):
                for x in range(5):
                    if (((x+y) <= 1) or ((x+y) >= 7)):
                        continue
                    if (((x-y) >= 3) or ((x-y) <= -3)):
                        continue
                    self.keypad.update({(x,y):hex(key_num)[2:].upper()})
                    key_num += 1
                    # print ('finger=(%d,%d), button=%s' %(x,y,self.keypad[(x,y)]))


    def find_button_name(self):
        return [self.keypad[(self.finger_pos['x'],self.finger_pos['y'])]]

    def push_keypad(self):
        # print ('Finger Position = %s' % self.finger_pos)
        self.passcode += self.find_button_name()

    def solve(self, input=None):
        self.set_start_button()
        self.generate_keypad()
        self.passcode = []
        for num in input:
           for move in num:
               self.update_finger_pos(move)
           self.push_keypad()
        self.result = "".join([str(x) for x in self.passcode])
        # print ('The Bathroom Passcode is %s' % self.result)
        return self.result


def main():
  print ('Find the Bathroom Passcode : \n%s' % str(INPUT)[:80])
  runner = RUNNER()
  runner.setup(input=['ULL','RRDDD','LURDL','UUUUD'], answer='1985', part=1)
  runner.setup(input=INPUT, answer='33444', part=1)
  runner.setup(input=['ULL','RRDDD','LURDL','UUUUD'], answer='5DB3', part=2)
  runner.setup(input=INPUT, answer=None, part=2)
  return

if __name__ == '__main__':
   main()
