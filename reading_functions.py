def clean_parameters(line):
    line['inlabel'] = line['inlabel'].strip(' ')
    line['function'] = line['function'].strip(' ')
    line['arg1'] = line['arg1'].strip(' ')
    line['arg2'] = line['arg2'].strip(' ')
    line['outlabel'] = line['outlabel'].strip(' ')
    line['inlabel'] = line['inlabel'].strip('\n')
    line['function'] = line['function'].strip('\n')
    line['arg1'] = line['arg1'].strip('\n')
    line['arg2'] = line['arg2'].strip('\n')
    line['outlabel'] = line['outlabel'].strip('\n')
    return line

def std_no_label(line):
    stdline = {'inlabel':"",'function':"",'arg1':"",'arg2':"",'outlabel':"",'len':1}
    label_using_functions = ["JMP","JEQ","JNE","JGT","JLT","JGE","JLE","JCR","JOV","CALL"]
    if line[0] == " " and line.find(':') == -1:
        if line.find(',') == -1:
            two_arg = False
        else:
            two_arg = True
        i = 1
        first = True
        while i < len(line):
            if line[i] == " " and first:
                i += 1
                continue
            elif line[i] != " ":
                first = False
                stdline['function'] += line[i]
                i += 1
            else:
                i+=1
                break
        post_coma = False
        while i < len(line):
            if two_arg:
                if  line[i] != "," and not post_coma:
                    stdline['arg1'] += line[i]
                    i+=1
                elif line[i] == ",":
                    post_coma = True
                    i += 1
                else:
                    stdline['arg2'] += line[i]
                    i += 1
            elif stdline['function'] in label_using_functions:
                stdline['outlabel'] += line[i]
                i+=1
            else:
                stdline['arg1'] += line[i]
                i += 1
    stdline = clean_parameters(stdline)
    return stdline



def standarize_line(line):
    stdline = {'inlabel':"",'function':"",'arg1':"",'arg2':"",'outlabel':"",'len':1}
    if line[0] == " " and line.find(':') == -1:
        stdline = std_no_label(line)
    elif line.find(':') != -1:
        i = 0
        line = line.strip()
        while i < len(line):
            if line[i] != ":" :
                stdline['inlabel'] += line[i]
                i+=1
            else:
                break
        stdline['inlabel'] == stdline['inlabel'].strip(" ")
        i += 1
        line = line[i:]
        if (len(line) > 2):
            next = std_no_label(line)
            stdline['function'] = next['function']
            stdline['arg1'] = next['arg1']
            stdline['arg2'] = next['arg2']
            stdline['outlabel'] = next['outlabel']

    stdline = clean_parameters(stdline)
    return stdline

def delete_lines(lines):
    i = 0
    while i < len(lines):
        if lines[i]['function'] == "" and lines[i] != lines[-1]:
            del lines[i]
        i+=1

def stack_labels(instructions):
    i = 0
    while i < len(instructions):
        if instructions[i]['inlabel'] != "" and instructions[i]['function'] == "":
            if i < len(instructions)-1:
                instructions[i+1]['inlabel'] = instructions[i]['inlabel']
                instructions[i+1]['len'] = 2
        i+=1
    delete_lines(instructions)

def swap_variables(lines, data):
    var = []
    for d in data:
        var.append(d[0])
    
    for line in lines:
        if line['arg1'] in var:
            line['arg1'] = str(var.index(line['arg1']))
        if line['arg2'] in var:
            line['arg2'] = str(var.index(line['arg2']))
        if line['arg1'].strip("()") in var and len(line['arg1'].strip("()")) != len(line['arg1']):
            arg = line['arg1'].strip("()")
            line['arg1'] = f"({var.index(arg)})" 
        if line['arg2'].strip("()") in var and len(line['arg2'].strip("()")) != len(line['arg2']):
            arg = line['arg2'].strip("()")
            line['arg2'] = f"({var.index(arg)})" 

def value_labels(instructions):
    i = 0
    ret = {}
    for instruction in instructions:
        if instruction['inlabel'] != "":
            ret[instruction['inlabel']] = i
        i+=1
    return ret



def swap_labels(instructions):
    labels = value_labels(instructions)
    for instruction in instructions:
        if instruction['outlabel'] in labels.keys():
            instruction['outlabel'] = str(labels[instruction['outlabel']])

        

