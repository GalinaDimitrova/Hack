# def reduce_file_path(path):
#     path = path.split('/')
#     print(path)
#     result = []
#     for i, item in enumerate(path):
#          if item == '..':
#              del path[i]
#              result.append(path)

#     # reduce '/'.join(result)


# reduce_file_path("/")
# reduce_file_path("/srv/../")
# reduce_file_path("/srv/www/htdocs/wtf/")
# reduce_file_path("/srv/www/htdocs/wtf")
# reduce_file_path("/srv/./././././")
# reduce_file_path("/etc//wtf/")
# reduce_file_path("/etc/../etc/../etc/../")
# reduce_file_path("//////////////")
# reduce_file_path("/../")