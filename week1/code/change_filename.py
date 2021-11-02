import re
import os


SAMPLE = "adsf(1).pdf"
SAMPLE = "adsf.pdf"
regex = "^(.*)\(\d\)\.pdf$"

c = re.compile(regex)
# filename_without_ext = c.findall(SAMPLE)[0]

parent_path = os.path.abspath(os.curdir)
target_path = os.path.join(parent_path, "../practice")
targets = os.listdir(target_path)

os.chdir(target_path)

for each in targets:
    try:
        filename_without_ext = c.findall(each)[0]
    except IndexError:
        print(each, "has already been correctly renamed.")
        continue

    print(filename_without_ext)
    new_name = filename_without_ext + ".pdf"
    os.rename(each, new_name)

