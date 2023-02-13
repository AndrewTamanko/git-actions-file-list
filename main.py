import os
import sys
import json

def main():
    path = os.environ["INPUT_PATH"]
    extension = os.environ["INPUT_TYPE"]

    path_count = 0
    paths = ''
    filenames = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(f'{extension}'):
                paths = paths + root + '/' + str(file) + ' '
                path_count = path_count + 1
                filenames.append(str(file))
                
    j = {}
    j['path_count'] = path_count
    j['paths'] = paths
    j['filenames'] = filenames
    with open(os.environ["GITHUB_OUTPUT"], "w") as myfile:
        myfile.write(json.dumps(j))
    print(paths)

    sys.exit(0)


if __name__ == "__main__":
    main()
