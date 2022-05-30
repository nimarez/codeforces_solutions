import math

def main():
    num_lines = int(input())
    for _ in range(num_lines):
        string = input()
        if is_excel_format(string):
            # excel to row columns
            for i, s in enumerate(string):
                if s.isnumeric():
                    print(f"R{string[i:]}C{alpha_to_num(string[:i])}")
                    break
        else:
            # row columns to excel
            r_idx = string.find('R')
            c_idx = string.find('C')
            row = int(string[r_idx+1:c_idx])
            column = int(string[c_idx+1:])
            print(f"{num_to_alpha(column)}{row}")


        

def is_excel_format(string):
    r_idx = string.find('R')
    c_idx = string.find('C')
    if r_idx == -1 or c_idx == -1 or not string[r_idx+1:c_idx].isnumeric():
        return True
    return False


def alpha_to_num(string):
    num = 0
    for i, c in enumerate(reversed(string)):
       num += (26 ** i) * (ord(c) - 64)
    return num

def num_to_alpha(num):
    output = []
    while num > 0:
        r = num % 26
        output.append(chr(r + 64) if r != 0 else chr(90))
        num = num // 26 if r != 0 else num // 26 - 1
    output.reverse()
    return "".join(output)

def test_helpers():
    assert num_to_alpha(1) == "A"
    assert alpha_to_num("A") == 1
    assert num_to_alpha(27) == "AA"
    assert alpha_to_num("AA") == 27
    assert num_to_alpha(28) == "AB"
    assert alpha_to_num("AB") == 28
    assert num_to_alpha(53) == "BA"
    assert alpha_to_num("BA") == 53


if __name__ == '__main__':
    main()