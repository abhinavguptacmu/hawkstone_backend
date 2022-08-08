fields = ['Reference', 'OrderStatus', 'RecievedDate']

status_code = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "",
                7: "", 8: "", 9: "", 10: "", 11: "", 12: '', 13: '',
                14: '', 15: '', 16: '', 17: '', 18: '', 19: ''}

def unpack_func(query):
    unpack = query.split(".")
    for k in range(len(unpack)):
        unpack[k] = unpack[k].split("&&")
    return unpack

#should try use map function here
def create_dict(unpack):
    i = 0
    Dict = {}
    for l in range(len(unpack)):
        add = {}
        for m in range(3):
            if len(unpack[l]) != 3:
                s = len(unpack[l])
                for s in range(4):
                    unpack[l].append("N/A")
                #print(unpack[l][m])
            if unpack[l][m] == "":
                unpack[l][m] = "N/A"
            add[fields[m]] = unpack[l][m]
        Dict[l] = add
    return Dict
