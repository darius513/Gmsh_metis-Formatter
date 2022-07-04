import argparse
import os


def formatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        line = f.readline()
        skip = True

        with open(os.path.basename(path).split('.')[0] + '_formatted' + '.txt', 'w+', encoding='utf-8') as new_f:
            while line:
                # filter
                if skip:
                    skip = False if line == '$Elements\n' else True
                    if skip or not skip and line == '$Elements\n':
                        line = f.readline()
                        continue

                if line.rstrip('\n').isdigit():
                    new_f.write(line)
                element = line.split()
                del element[0:5]
                if len(element):
                    new_f.write(" ".join(element) + '\n')
                line = f.readline()
        print('output file name: ', format(os.path.basename(path).split('.')[0] + '_formatted' + '.txt'))


def get_parameters():
    parser = argparse.ArgumentParser(description='formatter')
    parser.add_argument('--path', type=str, default='cube2-2.msh', help='the path of *.msh')
    args = parser.parse_args()
    assert len(args.path) != 0
    return args.path


if __name__ == '__main__':
    formatter(get_parameters())
