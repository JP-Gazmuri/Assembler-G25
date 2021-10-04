def validate_labels(instructions):
    inlabels = []
    outlabels = []
    outlabels_positions = []
    i = 0
    correct = True
    for instruction in instructions:
        if instruction['inlabel'] != "":
            inlabels.append(instruction['inlabel'])
        if instruction['outlabel'] != "":
            outlabels.append(instruction['outlabel'])
            outlabels_positions.append(i)
        i+=1
    i = 0
    for label in outlabels:
        if label not in inlabels:
            print(f"La etiqueta usada en linea {i} {label} no es declarada")
            correct = False
        i+=1
    return correct