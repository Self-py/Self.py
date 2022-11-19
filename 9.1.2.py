file_name = input("Enter a file path: ")
the_file = open(file_name, "r")
task_name = input("Enter a task: ")
if task_name == "sort":
    lst = list()
    newlist = []
    for line in the_file:
        lst += line.split()
    for item in lst:
        if item not in newlist:
            newlist.append(item)
    newlist.sort()
    print(newlist)
if task_name == "rev":
    for line in the_file:
        print(line[::-1])
if task_name == "last":
    n = int(input("Enter a number: "))
    lines = the_file.readlines()
    last_lines = lines[-(n):]
    print(last_lines)
the_file.close()