def load_files_into_array(path):
    with open(path, 'r', encoding='utf-8') as p:
        return [line.strip() for line in p]

user = load_files_into_array('usernames.txt')
psswd = load_files_into_array('passwords.txt')

cipher = ""

for i, nama in enumerate(user):
    if nama == 'cultiris':
        cipher = psswd[i]
        break

print(cipher)