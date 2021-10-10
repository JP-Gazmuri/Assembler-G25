def hex_to_dec(number):
    new = number.strip("#")
    return int(new,16)

def validate_literal(value,position,message):
    if value.find('#') == -1:
        try:
            number = int(value)
            if 0 <= number < 256:
                return True
            elif number < 0:
                message[0] = True
                print(f"Error en linea {position}: El literal {value} no puede ser negativo")
                return False
            else:
                message[0] = True
                print(f"Error en linea {position}: El literal {value} sobrepasa el maximo valor posible (255)")
                return False
        except ValueError:
            return False
    else:
        try:
            number = hex_to_dec(value)
            if  0 <= number < 256:
                return True
            elif number < 0:
                message[0] = True
                print(f"Error en linea {position}: El literal {value} no puede ser negativo")
                return False
            else:
                message[0] = True
                print(f"Error en linea {position}: El literal {value} sobrepasa el maximo valor posible (255)")
                return False
        except ValueError:
            return False

def direction_validation(value,position,message):
    if value[0] == "(" and value[-1] == ")":
        direction = value.strip("()")
        if direction.find('#') == -1:
            try:
                number = int(direction)
                if 0 <= number < 256:
                    return True
                elif number < 0:
                    message[0] = True
                    print(f"Error en linea {position}: La direccion {value} no puede ser negativa")
                    return False
                else:
                    message[0] = True
                    print(f"Error en linea {position}: La direccion {value} sobrepasa el maximo valor posible (255)")
                    return False
            except ValueError:
                return False
        else:
            try:
                number = hex_to_dec(direction)
                if 0 <= number < 256:
                    return True
                elif number < 0:
                    message[0] = True
                    print(f"Error en linea {position}: La direccion {value} no puede ser negativa")
                    return False
                else:
                    message[0] = True
                    print(f"Error en linea {position}: La direccion {value} sobrepasa el maximo valor posible (255)")
                    return False
            except ValueError:
                return False
    else:
        return False

                

def validate_labels(instructions , start_of_CODE):
    inlabels = []
    outlabels = []
    not_inlabel = []
    i = start_of_CODE
    lenght = len(instructions)+start_of_CODE
    correct = True
    for instruction in instructions:
        if instruction['inlabel'] != "":
            inlabels.append(instruction['inlabel'])
        if instruction['outlabel'] != "":
            outlabels.append((instruction['outlabel'],i))
        i+=1
    
    for label in outlabels:
        if label[0] not in inlabels:
            not_inlabel.append(label)
            i+=1
    for outlbl in not_inlabel:
        if outlbl[0].find('#') == -1:
            try:
                position = int(outlbl[0])
                if position > lenght:
                    correct = False
                    print(f"Error en la línea numero {outlbl[1]}: La direccion {outlbl[0]} sobrepasa el largo del codigo")
                elif position > 255:
                    correct = False
                    print(f"Error en la línea numero {outlbl[1]}: La direccion {outlbl[0]} sobrepasa el valor maximo de 255")
            except ValueError:
                correct = False
                print(f"Error en la línea numero {outlbl[1]}: La etiqueta {outlbl[0]} no es declarada")
        else:
            position = hex_to_dec(outlbl[0])
            if position > lenght:
                correct = False
                print(f"Error en la línea numero {outlbl[1]}: La direccion {outlbl[0]} sobrepasa el largo del codigo")
    return correct


def validate_functions_syntax(lines, start_of_CODE):
    valid_functions = ["MOV","ADD","SUB","AND","OR","NOT","XOR","SHL","SHR","INC","RST","CMP","JMP","JEQ","JNE","JGT","JLT","JGE","JLE","JCR","JOV","CALL","RET","POP","PUSH"]
    correct = True
    i = start_of_CODE
    for line in lines:
        if line['function'] not in valid_functions:
            correct = False
            print(f"Error en la línea numero {i}: La funcion {line['function']} no existe.")
        i+=1
    return correct

def function_validation(line,combinations , position):
    message = [False]
    if "A,B" in combinations:
        if line['arg1'] == "A" and line['arg2'] == "B":
            line['arguments'] = "A,B"
            return True
    
    if "B,A" in combinations:
        if line['arg1'] == "B" and line['arg2'] == "A":
            line['arguments'] = "B,A"
            return True

    if "A,Lit" in combinations:
        if line['arg1'] == "A" and validate_literal(line['arg2'],position,message):
            line['arguments'] = "A,Lit"
            return True
    
    if "B,Lit" in combinations:
        if line['arg1'] == "B" and validate_literal(line['arg2'],position,message):
            line['arguments'] = "B,Lit"
            return True
    
    if "A,(B)" in combinations:
        if line['arg1'] == "A" and line['arg2'] == "(B)":
            line['arguments'] = "A,(B)"
            return True
    
    if "B,(B)" in combinations:
        if line['arg1'] == "B" and line['arg2'] == "(B)":
            line['arguments'] = "B,(B)"
            return True
    
    if "(B),A" in combinations:
        if line['arg1'] == "(B)" and line['arg2'] == "A":
            line['arguments'] = "(B),A"
            return True
    
    if "A,A" in combinations:
        if line['arg1'] == "A" and line['arg2'] == "A":
            line['arguments'] = "A,A"
            return True

    if "B,B" in combinations:
        if line['arg1'] == "B" and line['arg2'] == "B":
            line['arguments'] = "B,B"
            return True
        
    if "(B)" in combinations:
        if line['arg1'] == "(B)" and line['arg2'] == "":
            line['arguments'] = "(B)"
            return True
    
    if "B" in combinations:
        if line['arg1'] == "B" and line['arg2'] == "":
            line['arguments'] = "B"
            return True
    
    if "A" in combinations:
        if line['arg1'] == "A" and line['arg2'] == "":
            line['arguments'] = "A"
            return True

    if "A,Dir" in combinations:
        if line['arg1'] == "A" and direction_validation(line['arg2'],position,message):
            line['arguments'] = "A,Dir"
            return True
    
    if "B,Dir" in combinations:
        if line['arg1'] == "B" and direction_validation(line['arg2'],position,message):
            line['arguments'] = "B,Dir"
            return True
    
    if "Dir,A" in combinations:
        if direction_validation(line['arg1'],position,message) and line['arg2'] == "A":
            line['arguments'] = "Dir,A"
            return True
    
    if "Dir,B" in combinations:
        if direction_validation(line['arg1'],position,message) and line['arg2'] == "B":
            line['arguments'] = "Dir,B"
            return True
    
    if "Dir" in combinations:
        if direction_validation(line['arg1'],position,message) and line['arg2'] == "":
            line['arguments'] = "Dir"
            return True

    if not message[0]:
        print(f"Error en linea {position}: Los argumentos no cumplen la logica para la funcion {line['function']}")
    return False

def logic_validation(lines, start_of_CODE):
    posible_arguments = {}
    posible_arguments['MOV'] = ["A,B","B,A","A,Lit","B,Lit","A,Dir","B,Dir","Dir,A","Dir,B","A,(B)","B,(B)","(B),A"]
    posible_arguments['ADD'] = ["A,B","B,A","A,Lit","B,Lit","A,Dir","B,Dir","A,(B)","Dir"]
    posible_arguments['SUB'] = ["A,B","B,A","A,Lit","B,Lit","A,Dir","B,Dir","A,(B)","Dir"]
    posible_arguments['AND'] = ["A,B","B,A","A,Lit","B,Lit","A,Dir","B,Dir","A,(B)","Dir"]
    posible_arguments['OR'] = ["A,B","B,A","A,Lit","B,Lit","A,Dir","B,Dir","A,(B)","Dir"]
    posible_arguments['NOT'] = ["A,A","A,B","B,A","B,B","Dir,A","Dir,B","(B)"]
    posible_arguments['XOR'] = ["A,B","B,A","A,Lit","B,Lit","A,Dir","B,Dir","A,(B)","Dir"]
    posible_arguments['SHL'] = ["A,A","A,B","B,A","B,B","Dir,A","Dir,B","(B)"]
    posible_arguments['SHR'] = ["A,A","A,B","B,A","B,B","Dir,A","Dir,B","(B)"]
    posible_arguments['INC'] = ["B","Dir","(B)"]
    posible_arguments['RST'] = ["Dir","(B)"]
    posible_arguments['CMP'] = ["A,B","A,Lit","B,Lit","A,Dir","B,Dir","A,(B)"]
    posible_arguments['PUSH'] = ["A","B"]
    posible_arguments['POP'] = ["A","B"]
    i = start_of_CODE
    answer = True
    for line in lines:
        if line['function'] in posible_arguments.keys():
            if not function_validation(line,posible_arguments[line['function']],i):
                answer = False
        i+=1
    return answer


def full_validation(lines,start_of_CODE):
    ret = True
    if not validate_labels(lines,start_of_CODE):
        ret = False
    if not validate_functions_syntax(lines,start_of_CODE):
        ret = False
    if not logic_validation(lines,start_of_CODE):
        ret = False
    return ret
