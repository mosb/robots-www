import os
import shutil
import re

os.chdir('/Users/michaelosborne/Documents/WWW/MosbWWW/robots-www/')

publication_types = [
    'Journal'
    # ,
    # 'Conference',
    # 'Preprints',
    # 'Reports',
    # 'Workshop',
    # 'Theses'
]

# Compile regex we'll use over and over below
regex = re.compile(r"(?<=file = {).*?(files/)", re.IGNORECASE)

for publication_type in publication_types:
    publication_bib = publication_type + '.bib'
    publication_bib_path = '_bibliography/' + publication_bib
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

    # shutil.copytree( -r _bibliography/Osborne/files/ public/pdf

#  _bibliography/osborne.bib
# rm -rf ./_bibliography/Osborne
# chmod -R a+rx ./public/pdf
# jekyll build
# rsync -avz /Users/michaelosborne/Documents/WWW/MosbWWW/robots-www/_site/ mosb@robots.ox.ac.uk:~/WWW
