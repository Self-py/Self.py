def who_is_missing(file_name):
    fid = open(file_name, "r")
    line = fid.read()
    n_list = [int(n) for n in line.split(',')]
    fid.close()
    for n in range(1, len(n_list) + 2):
        if n not in n_list:
            fout = open("found.txt", "w")
            fout.write(str(n))
            return n