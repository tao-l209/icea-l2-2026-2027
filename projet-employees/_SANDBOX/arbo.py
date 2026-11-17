import os

# Liste des dossiers à exclure
EXCLUDE = [
    'node_modules', '.git', 'vendor', 'logs', 'tmp', 
    'arbo.txt', 'arbo.php', 'arbo.py', 'bootstrap', 
    'TEMPLATE_LAYOUT', 'templateOLD', 'fonts', 'tests', 'webfonts'
]
OUTPUT = 'arbo.txt'

def scan(dir_path, exclude, depth, f):
    try:
        items = sorted(os.listdir(dir_path))
    except PermissionError:
        return
    
    for item in items:
        if item in ['.', '..']:
            continue
        path = os.path.join(dir_path, item)
        if os.path.isdir(path):
            if item not in exclude:
                f.write('  ' * depth + '📁 ' + item + '\n')
                scan(path, exclude, depth + 1, f)
        else:
            f.write('  ' * depth + '📄 ' + item + '\n')

# Cible : juste un cran au-dessus du dossier contenant le script (ex: _SANDBOX -> dossier du projet)
script_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.abspath(os.path.join(script_dir, '..'))

output_path = os.path.join(script_dir, OUTPUT)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(f"Arborescence du dossier : {target_dir}\n")
    scan(target_dir, EXCLUDE, 0, f)

print(f"Fichier '{OUTPUT}' créé !")