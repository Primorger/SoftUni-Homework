import os

files = {}
directory = "../"

for el in os.listdir(directory):
    f = os.path.join(directory, el)

    if os.path.isfile(f):
        ext = el.split(".")[-1]

        if ext not in files:
            files[ext] = []

        files[ext].append(el)
    else:
        for element in os.listdir(f):
            dirname = os.path.join(f, element)

            if os.path.isfile(dirname):
                ext = element.split(".")[-1]

                if ext not in files:
                    files[ext] = []

                files[ext].append(element)

with open(os.path.join(directory, "report.txt"), "w") as output_file:

    for ext, file_names in sorted(files.items()):
        output_file.write(f"{ext}\n")

        for file_name in sorted(file_names):
            output_file.write(f"- - - {file_name}\n")