def get_data(file_path):
    with open(file_path, 'r') as file:
        return file.read(), file_path
