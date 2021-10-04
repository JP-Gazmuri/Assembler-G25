def validate_labels(instructions):
    inlabels = []
    outlabels = []
    for instruction in instructions:
        if instruction['inlabel'] != "":
            inlabels.append(instruction['inlabel'])
        if instruction['outlabel'] != "":
            outlabels.append(instruction['outlabel'])
    for label in outlabels:
        if label not in inlabels:
            return False
    return True