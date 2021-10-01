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
    stdline = {'inlabel':"",'function':"",'arg1':"",'arg2':"",'outlabel':""}
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
            if not two_arg:
                stdline['outlabel'] += line[i]
                i+=1
    stdline = clean_parameters(stdline)
    return stdline



def standarize_line(line):
    stdline = {'inlabel':"",'function':"",'arg1':"",'arg2':"",'outlabel':""}
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


