def copy_file_content(source, destination):
    """
    """
    with open(source, "r") as source_file:
        source_file_content = source_file.read()

    with open(destination, "w") as destination_file:
        destination_file.write(source_file_content)