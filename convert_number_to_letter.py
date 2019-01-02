def make_string(number):
    num_dict = {
        1: "one",
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }
    new_str = ''
    first = number // 1000
    second = (number % 1000) // 100
    if (number % 100) < 20:
        third = (number % 100)
        fourth = 0
    else:
        fourth = number % 10
        third = (number % 100) - fourth
    if first != 0:
        new_str += num_dict[first] + ' ' + 'thousand'
    if second != 0:
        new_str += ' ' + num_dict[second] + ' ' + 'hundred'
    if third != 0:
        new_str += ' ' + num_dict[third]
    if fourth != 0:
        new_str += ' ' + num_dict[fourth]   
    return new_str


print(make_string(int(input('Enter one or two or tree or four digit number '))))
