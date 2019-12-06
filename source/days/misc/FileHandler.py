def getFileContentByLine(abs_file_path):
    text_file = open(abs_file_path, "r")
    lines =  text_file.read().splitlines()
    text_file.close()
    return lines

def getFileContentByCommaSeperation(abs_file_path):
    text_file = open(abs_file_path, "r")
    stringList =  text_file.read().split(',')
    text_file.close()
    return stringList

