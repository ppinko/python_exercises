#-*- coding: iso-8859-2 -*-


def split_line(line, chars):
    L = list(reversed(line.split()))
    all_lines = []
    temp = ''
    while len(L) > 0:
        if len(temp) == 0:
            temp = L.pop()
        elif len(temp) + 1 + len(L[-1]) <= chars:
            temp += ' ' + L.pop()
        else:
            all_lines.append(temp)
            temp = L.pop()
    if len(temp) > 0:
        all_lines.append(temp)
    return all_lines


def copy_file(old, new, chars):
    with open (old, mode='r') as reader, open (new, mode='w') as writer:
        while True:
            line = reader.readline()
            if len(line) == 0:
                break
            line = line.strip()
            if len(line) <= chars:
                line += '\n'
                writer.write(line)
            else:
                all_lines = split_line(line, chars)
                for i in all_lines:
                    i += '\n'
                    writer.write(i)


copy_file(file1, file2, 62)