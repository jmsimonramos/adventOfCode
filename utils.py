def getInputData(filename):
    with open ("Input/"+filename, "r", encoding="utf-8") as file:
        data = [x.strip() for x in file.readlines()]
    return data