import os

text = ''

for subdir, dirs, files in os.walk('.'):
    for file in files:
        if subdir.startswith('./modules/livrables/') and file.endswith('.md'):
            f = os.path.join(subdir, file)
            with open(f, 'r') as file:
                file_content = file.read()
                text += file_content
                text += '\n'

f = open("output.md", "w")
f.write(text)
f.close()
