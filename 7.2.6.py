def main():
    """Applies actions on list of items according to the input command.
    first input: list of items, seperate by ','
    second input: command number (1-9)
    """
    my_list = input("Enter grocery list: ").split(',')
    command = None
    while command != 9:
        command = int(input("Enter command: "))
        if command == 1:
            print(my_list)
        if command == 2:
            print(len(my_list))
        if command == 3:
            check_for = input("check for an item: ")
            print(check_for in my_list)
        if command == 4:
            check_for = input("count an item: ")
            print(my_list.count(check_for))
        if command == 5:
            my_list.remove(input("remove an item: "))
        if command == 6:
            my_list.append(input("add an item: "))
        if command == 7:
            print([item for item in my_list if (len(item) < 3 or not item.isalpha())])
        if command == 8:
            my_list = list(set(my_list))


if __name__ == "__main__":
    main()