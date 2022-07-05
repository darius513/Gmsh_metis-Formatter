import argparse
import os

files = {
    "msh": {"start": '$Elements', "delete_count": 5, "Separator": " ", "begin_Separator": "\n"},
    "inp": {"start": '*ELEMENT', "delete_count": 1, "Separator": ",", "begin_Separator": ", "}
}


def formatter(path):
    ele_num = 0  # element number
    file_inf = files.get(os.path.basename(path).split('.')[1], "Invalid file type")
    file_name = os.path.basename(path).split('.')[0]
    with open(path, 'r', encoding='utf-8') as f:
        line = f.readline()
        skip = True

        with open(file_name + '_formatted' + '.txt', 'w+', encoding='utf-8') as new_f:
            while line:
                # Termination condition
                if not skip and not line.split(file_inf.get("Separator"))[0].strip('\n ').isdigit():
                    break
                if skip:
                    skip = False if line.split(file_inf.get("begin_Separator"))[0] == file_inf.get("start") else True
                    # Ignore the first line at the beginning of the element block
                    if skip or not skip and line.split(file_inf.get("begin_Separator"))[0] == file_inf.get("start"):
                        line = f.readline()
                        continue

                # Removing spaces from each node str of each element
                element = list(map(lambda x: x.strip(), line.split(file_inf.get("Separator"))))
                del element[0:file_inf.get("delete_count")]
                if len(element):
                    ele_num = ele_num + 1
                    new_f.write(" ".join(element) + '\n')
                line = f.readline()

        # Number of elements written at the beginning of the file
        with open(file_name + '_formatted' + '.txt', 'r+', encoding='utf-8') as new_f:
            content = new_f.read()
            new_f.seek(0, 0)
            new_f.write(str(ele_num) + '\n' + content)

        print('output file name: ', format(file_name + '_formatted' + '.txt'))


def get_parameters():
    parser = argparse.ArgumentParser(description='formatter')
    parser.add_argument('--path', type=str, default='cube2-2.msh', help='the path of *.msh')
    args = parser.parse_args()
    assert len(args.path) != 0
    return args.path


if __name__ == '__main__':
    formatter(get_parameters())