def getFileContentByLineAsDbl(abs_file_path):
    text_file = open(abs_file_path, "r")
    lines =  text_file.read().splitlines()
    text_file.close()
    return map(float, lines)