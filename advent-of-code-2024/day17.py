from advent import dataclass, field

@dataclass
class Computer:
    prog:   list
    areg:   int  = 0
    breg:   int  = 0
    creg:   int  = 0
    pc:     int  = 0
    output: list = field(default_factory=list)

    def run(self):
        while self.pc < len(self.prog) - 1:
            opcode  = self.prog[self.pc]
            operand = self.prog[self.pc+1]
            self.pc += 2

            match opcode:
                case 0: self.areg = int(self.areg / (2 ** self.combo(operand)))
                case 1: self.breg ^= operand
                case 2: self.breg = self.combo(operand) % 8
                case 3: self.pc = operand if self.areg != 0 else self.pc
                case 4: self.breg ^= self.creg
                case 5: self.output.append(self.combo(operand) % 8)
                case 6: self.breg = int(self.areg / (2 ** self.combo(operand)))
                case 7: self.creg = int(self.areg / (2 ** self.combo(operand)))

        return ",".join([ str(x) for x in self.output ])

    def combo(self, operand):
        match operand:
            case 0 | 1 | 2 | 3: return operand
            case 4: return self.areg
            case 5: return self.breg
            case 6: return self.creg

assert Computer(areg=65804993,prog=[2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0]).run() == "5,1,4,0,5,1,0,2,6"
