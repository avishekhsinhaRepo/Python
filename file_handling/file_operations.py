def save_to_file(content, file_name):
    with open(file_name, "w") as file:
        file.write(content)


def read_file(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        return content
