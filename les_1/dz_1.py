def palindrom(s):
    if s == s[::-1]:
        print('True')
    else:
        print('False')

palindrom('asdsddsf')
palindrom('abba')