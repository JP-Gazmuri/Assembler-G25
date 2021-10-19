from validation_functions import hex_to_dec

def write_instruction(line):
    if line['function'] == 'MOV':
        if line['arguments'] == "A,B":
            return '0000000'
        if line['arguments'] == "B,A":
            return "0000001"
        if line['arguments'] == "A,Lit":
            return "0000010"
        if line['arguments'] == "B,Lit":
            return "0000011"
        if line['arguments'] == "A,Dir":
            return "0100101"
        if line['arguments'] == "B,Dir":
            return "0100110"
        if line['arguments'] == "Dir,A":
            return "0100111"
        if line['arguments'] == "Dir,B":
            return "0101000"
        if line['arguments'] == "A,(B)":
            return "0101001"
        if line['arguments'] == "B,(B)":
            return "0101010"
        if line['arguments'] == "(B),A":
            return "0101011"
    if line['function'] == 'ADD':
        if line['arguments'] == "A,B":
            return "0000100"
        if line['arguments'] == "B,A":
            return "0000101"
        if line['arguments'] == "A,Lit":
            return "0000110"
        if line['arguments'] == "B,Lit":
            return "0000111"
        if line['arguments'] == "A,Dir":
            return "0101100"
        if line['arguments'] == "B,Dir":
            return "0101101"
        if line['arguments'] == "A,(B)":
            return "0101110"
        if line['arguments'] == "Dir":
            return "0101111"
    if line['function'] == 'SUB':
        if line['arguments'] == "A,B":
            return "0001000"
        if line['arguments'] == "B,A":
            return "0001001"
        if line['arguments'] == "A,Lit":
            return "0001010"
        if line['arguments'] == "B,Lit":
            return "0001011"
        if line['arguments'] == "A,Dir":
            return "0110000"
        if line['arguments'] == "B,Dir":
            return "0110001"
        if line['arguments'] == "A,(B)":
            return "0110010"
        if line['arguments'] == "Dir":
            return "0110011"
    if line['function'] == 'AND':
        if line['arguments'] == "A,B":
            return "0001100"
        if line['arguments'] == "B,A":
            return "0001101"
        if line['arguments'] == "A,Lit":
            return "0001110"
        if line['arguments'] == "B,Lit":
            return "0001111"
        if line['arguments'] == "A,Dir":
            return "0110100"
        if line['arguments'] == "B,Dir":
            return "0110101"
        if line['arguments'] == "A,(B)":
            return "0110110"
        if line['arguments'] == "Dir":
            return "0110111"
    if line['function'] == 'OR':
        if line['arguments'] == "A,B":
            return "0010000"
        if line['arguments'] == "B,A":
            return "0010001"
        if line['arguments'] == "A,Lit":
            return "0010010"
        if line['arguments'] == "B,Lit":
            return "0010011"
        if line['arguments'] == "A,Dir":
            return "0111000"
        if line['arguments'] == "B,Dir":
            return "0111001"
        if line['arguments'] == "A,(B)":
            return "0111010"
        if line['arguments'] == "Dir":
            return "0111011"
    if line['function'] == 'NOT':
        if line['arguments'] == "A,A":
            return "0010100"
        if line['arguments'] == "A,B":
            return "0010101"
        if line['arguments'] == "B,A":
            return "0010110"
        if line['arguments'] == "B,B":
            return "0010111"
        if line['arguments'] == "Dir,A":
            return "0111100"
        if line['arguments'] == "Dir,B":
            return "0111101"
        if line['arguments'] == "(B)":
            return "0111110"
    if line['function'] == 'XOR':
        if line['arguments'] == "A,B":
            return "0011000"
        if line['arguments'] == "B,A":
            return "0011001"
        if line['arguments'] == "A,Lit":
            return "0011010"
        if line['arguments'] == "B,Lit":
            return "0011011"
        if line['arguments'] == "A,Dir":
            return "0111111"
        if line['arguments'] == "B,Dir":
            return "1000000"
        if line['arguments'] == "A,(B)":
            return "1000001"
        if line['arguments'] == "Dir":
            return "1000010"
    if line['function'] == 'SHL':
        if line['arguments'] == "A,A":
            return "0011100"
        if line['arguments'] == "A,B":
            return "0011101"
        if line['arguments'] == "B,A":
            return "0011110"
        if line['arguments'] == "B,B":
            return "0011111"
        if line['arguments'] == "Dir,A":
            return "1000011"
        if line['arguments'] == "Dir,B":
            return "1000100"
        if line['arguments'] == "(B)":
            return "1000101"
    if line['function'] == 'SHR':
        if line['arguments'] == "A,A":
            return "0100000"
        if line['arguments'] == "A,B":
            return "0100001"
        if line['arguments'] == "B,A":
            return "0100010"
        if line['arguments'] == "B,B":
            return "0100011"
        if line['arguments'] == "Dir,A":
            return "1000110"
        if line['arguments'] == "Dir,B":
            return "1000111"
        if line['arguments'] == "(B)":
            return "1001000"
    if line['function'] == 'INC':
        if line['arguments'] == "B":
            return "0100100"
        if line['arguments'] == "Dir":
            return "1001001"
        if line['arguments'] == "(B)":
            return "1001010"
    if line['function'] == 'RST':
        if line['arguments'] == "Dir":
            return "1001011"
        if line['arguments'] == "(B)":
            return "1001100"
    if line['function'] == 'CMP':
        if line['arguments'] == "A,B":
            return "1001101"
        if line['arguments'] == "A,Lit":
            return "1001110"
        if line['arguments'] == "B,Lit":
            return "1001111"
        if line['arguments'] == "A,Dir":
            return "1010000"
        if line['arguments'] == "B,Dir":
            return "1010001"
        if line['arguments'] == "A,(B)":
            return "1010010"
    if line['function'] == 'JMP':
        return "1010011"
    if line['function'] == 'JEQ':
        return "1010100"
    if line['function'] == 'JNE':
        return "1010101"
    if line['function'] == 'JGT':
        return "1010110"
    if line['function'] == 'JLT':
        return "1010111"
    if line['function'] == 'JGE':
        return "1011000"
    if line['function'] == 'JLE':
        return "1011001"
    if line['function'] == 'JCR':
        return "1011010"
    if line['function'] == 'JOV':
        return "1011011"
    if line['function'] == 'CALL':
        return "1011100"
    if line['function'] == 'RET':
        return "1011101"
    if line['function'] == 'PUSH':
        if line['arguments'] == 'A':
            return "1011110"
        elif line['arguments'] == 'B':
            return "1011111"
    if line['function'] == 'POP':
        if line['arguments'] == 'A':
            return "1100000"
        elif line['arguments'] == 'B':
            return "1100001"

def write_file(instructions,data):
    final = []
    zeros = '00000000'
    for instruction in instructions:
        if instruction['outlabel'] == "":
            bits = write_instruction(instruction)
            if instruction['arguments'].find("Lit") != -1:
                bits = bits + lit_to_8bit(instruction['arg2'])
                final.append(bits)
            elif instruction['arguments'].find("Dir") == 0:
                bits = bits + dir_to_8bit(instruction['arg1'],data)
                final.append(bits)
            elif instruction['arguments'].find("Dir") != -1:
                bits = bits + dir_to_8bit(instruction['arg2'],data)
                final.append(bits)
            else:
                bits = bits + zeros
                final.append(bits)
        else:
            final.append(write_instruction(instruction)+lit_to_8bit(instruction['outlabel']))
    return final

def filter_lines(lines):
    filtered = []
    for line in lines:
        if not line['function'] == "":
            filtered.append(line)
    return filtered

def lit_to_8bit(value):
    if value.find('#') == -1:
        number = int(value)
        if number < 0:
            number = 256 + number
        binary = format(number,"b")
        while len(binary) < 8:
            binary = "0" + binary
        return binary
    else:
        number = hex_to_dec(value)
        binary = format(number,"b")
        while len(binary) < 8:
            binary = "0" + binary
        return binary

def dir_to_8bit(value,data):
    if value.find("#") == -1:
        number = value.strip("()")
        number = int(number)
        binary = format(number,"b")
        while len(binary) < 8:
            binary = "0" + binary
        return binary
    else:
        number = value.strip("()#")
        number = hex_to_dec(number)
        binary = format(number,"b")
        while len(binary) < 8:
            binary = "0" + binary
        return binary

def full_write_file(instructions,data):
    lines = filter_lines(instructions)
    return write_file(lines,data)

