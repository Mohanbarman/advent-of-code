import string

sample_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def mul_nums(memory: str) -> int:
    cursor = 0
    res = 0

    do = True

    while cursor < len(memory):
        if memory[cursor : cursor + 7] == "don't()":
            do = False
            cursor += 7
        elif memory[cursor : cursor + 4] == "do()":
            do = True
            cursor += 4
        elif memory[cursor : cursor + 4] == "mul(" and do:
            cursor += 4
            operands = []
            while cursor < len(memory):
                if memory[cursor] in string.digits:
                    if not operands:
                        operands.append(memory[cursor])
                    else:
                        operands[-1] += memory[cursor]
                elif memory[cursor] == ",":
                    operands.append("")
                elif memory[cursor] == ")":
                    break
                else:
                    operands = []
                    break
                cursor += 1
            if operands:
                res += int(operands[0]) * int(operands[1])
        else:
            cursor += 1

    return res

# print(mul_nums(sample_input))

with open("day3-input.txt", "r") as f:
    print(mul_nums(f.read()))
