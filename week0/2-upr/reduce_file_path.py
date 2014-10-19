def reduce_file_path(path):
    path = path.split("/")
    new_path = path[:]  # make a copy of a list
    reduced = []
    count_deletes = 0
    # check elements from the first to the last
    for i, item in enumerate(path):
        if item == "..":
            del new_path[i - count_deletes]
            del new_path[i - 1 - count_deletes]
            count_deletes += 2
        elif item == ".":
            del new_path[i - count_deletes]
            count_deletes += 1
        elif item == "" and i != 0:
            del new_path[i - count_deletes]
            count_deletes += 1
    if new_path == [] or len(new_path) == 1:
        return "/"
    else:
        reduced = "/".join(new_path)
    return reduced
