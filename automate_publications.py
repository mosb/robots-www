import os
import shutil
import re
import subprocess

def copytree(src, dst, symlinks=False, ignore=None):
    # http://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)

os.chdir('/Users/michaelosborne/Documents/WWW/MosbWWW/robots-www/')

publication_types = [
    'Journal',
    'Conference',
    'Preprints',
    'Reports',
    'Workshop',
    'Theses'
]

# Compile regex we'll use over and over below
regex = re.compile(r"(?<=file = {).*?(files/)", re.IGNORECASE)

for publication_type in publication_types:
    publication_bib = publication_type + '.bib'
    publication_bib_out = publication_type + '_bib.bib'
    publication_bib_path = '_bibliography/' + publication_bib_out
    shutil.copyfile(
        '_bibliography/' + publication_type + '/' + publication_bib,
        publication_bib_path
    )

    # Read in the file
    file_data = None
    with open(publication_bib_path, 'r') as file :
        file_data = file.readlines()

    with open(publication_bib_path, 'w+') as file:
        for line in file_data:

            # Remove unnecessary':application/pdf'
            line = line.replace(':application/pdf', '')

            # Tidy up file paths : edit file links to eg {162/1403.4640.pdf}
            line = regex.sub("", line)

            # Write the file out again
            file.write(line)

    copytree('_bibliography/' + publication_type + '/files', 'public/pdf')

    # process = subprocess.Popen(
    #     "rm -rf ./_bibliography/" + publication_type,
    #     stdout=subprocess.PIPE
    # )
    # output, error = process.communicate()


bashCommand = """
chmod -R a+rx ./public/pdf
jekyll build
"""
# rsync -avz /Users/michaelosborne/Documents/WWW/MosbWWW/robots-www/_site/ mosb@robots.ox.ac.uk:~/WWW
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
