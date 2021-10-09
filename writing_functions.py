def write_instruction(line):
    #line['function'], line['arguments']
    if line['function'] == 'MOV':
        if line['arguments'] == "A,B":
            return '0000000'