import os

files = {
    'Luminaria': 'luminaria.py',
    'Cinzeiro': 'cinzeiro.py',
    'Livro.py': 'livro.py'
}

def exec_script(script):
    os.system("python3 {}".format(script))

for item in files:
    print("// Codigo da {}".format(item))
    exec_script(files[item])
