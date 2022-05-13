
def parse_digit(string):
    res_str = ''.join([string[i] for i in range(len(string)) if ord(string[i]) >= 48 and ord(string[i]) <= 57])
    return int(res_str)