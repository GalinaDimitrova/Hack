def reduce_file_path(path):
    path = path.split("/")
    new_path = path[:]  # make a copy of a list
    reduced = []
    # check elements from the last to the first
    for i in range(len(path) - 1, 0, -1):
        if path[i] == "..":
            del new_path[i]
            del new_path[i - 1]
        elif path[i] == ".":
            del new_path[i]
        elif path[i] == "" and i != 0:
            del new_path[i]
    if new_path == [] or len(new_path) == 1:
        return "/"
    else:
        reduced = "/".join(new_path)
    return reduced
