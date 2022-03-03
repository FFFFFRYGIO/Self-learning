import pickle


def export_dict(example_dict):
    pickle_out = open("dict.pickle", "wb")
    pickle.dump(example_dict, pickle_out)  # send dict to file
    pickle_out.close()


def import_dict():
    pickle_in = open("dict.pickle", "rb")
    example_dict = pickle.load(pickle_in)  # read dict from file
    pickle_in.close()
    return example_dict


example_dict = {1: "6", 2: "2", 3: "f"}
example_dict2 = {1: "A", 2: "B", 3: "C"}

export_dict(example_dict)
export_dict(example_dict2)
# 2nd export overrites prior export

example_dict_import = import_dict()
example_dict_import2 = import_dict()
# they import the same object (2nd)

print(example_dict_import, example_dict_import2)

for k in example_dict_import.keys():
    print(k, example_dict_import[k])

for k in example_dict_import2.keys():
    print(k, example_dict_import2[k])