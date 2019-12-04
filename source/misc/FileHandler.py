def getFileContentByLineAsDbl(abs_file_path):
    text_file = open(abs_file_path, "r")
    lines =  text_file.read().splitlines()
    text_file.close()
    return map(float, lines)


# numpy/pandas doesn't work on my machine, hence this workaround...
def getFileContentByCommaSeperation(abs_file_path):
    text_file = open(abs_file_path, "r")
    numbers =  text_file.read().split(',')
    text_file.close()
    return list(map(int, numbers))
