import pickle
from cryptography.fernet import Fernet
from os import getenv

password_file = "passwords.txt"
key_file = "key.key"


def write_key():
    if getenv('key'):
        key = getenv('key')
    else:
        key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open(key_file, "rb")
    key = file.read()
    file.close()
    return key


def export_dict(dict_passwords):
    pickle_out = open(password_file, "wb")
    pickle.dump(dict_passwords, pickle_out)  # send dict to file
    pickle_out.close()


def import_dict():
    pickle_in = open(password_file, "rb")
    dict_passwords = pickle.load(pickle_in)  # read dict from file
        
    pickle_in.close()
    return dict_passwords


def export_password(password):
    dict_passwords = import_dict()
    k, v = password.popitem()
    f = Fernet(load_key())
    v_dec = f.encrypt(v.encode()).decode()

    # user can have multiple passwords - creates list
    if k not in dict_passwords.keys():
        dict_passwords[k] = v_dec
    elif isinstance(dict_passwords[k], str):
        dict_passwords[k] = [dict_passwords[k], v_dec]
    else:
        dict_passwords[k] = dict_passwords[k].append(v_dec)

    export_dict(dict_passwords)


def import_password(name):
    dict_passwords = import_dict()
    passwords = dict_passwords[name]
    f = Fernet(load_key())
    if isinstance(passwords, str):
        return f.decrypt(passwords.encode()).decode()
    else:
        encrypted = []
        for password in passwords:
            enc = f.decrypt(password.encode()).decode()
            encrypted.append(enc)
        return encrypted


# passwords to input:
p1 = {'radek': 'ABC'}
p2 = {'karol': 'BCD'}
p3 = {'tomek': 'CDE'}
p4 = {'tomek': 'DEF'}

write_key()
export_dict({'test': 'test'})


export_password(p1)
export_password(p2)
export_password(p3)
export_password(p4)

print(import_password('radek'))
print(import_password('karol'))
print(import_password('tomek'))
