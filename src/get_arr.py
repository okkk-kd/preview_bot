
def get_arr(path_fie):
    file = open(path_fie, 'rb')
    line = file.readline().decode('utf-8')
    uni = []
    while (line):
        uni.append(line)
        line = file.readline().decode('utf-8')
    return uni