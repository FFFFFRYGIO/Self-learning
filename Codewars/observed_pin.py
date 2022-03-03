import itertools

def get_pins(observed):
    borderers = {
        '0': ['0','8'],
        '1': ['1','2','4'],
        '2': ['1','2','3','5'],
        '3': ['2','3','6'],
        '4': ['1','4','5','7'],
        '5': ['2','4','5','6','8'],
        '6': ['3','5','6','9'],
        '7': ['4','7','8'],
        '8': ['5','7','8','9','0'],
        '9': ['6','8','9'],
    }
    observed=str(observed)
    result = []
    pockets = []
    # creating list of sets for every space in result
    for c in observed:
        pockets.append(borderers[c])
    # creating a Cartesian product of pockets
    for element in itertools.product(*pockets):
        r = ''
        print(element)
        # creating a single result
        for e in element:
            r += e
        result.append(r)
    return result
