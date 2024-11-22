import sys

def camel_case(strings):
    new_values_list = []

    for i in strings:
        list_values = i.split(';')
        new_string = ''
        string = list_values[2]
        first_step = False
        next_letter = False
        enter_method_function = False

        if 'C' in list_values:
            for a in string:
                if next_letter:
                    new_string += a.upper()
                    next_letter = False
                elif a == ' ':
                    next_letter = True
                    new_string = new_string.replace(a, '')
                else:
                    new_string += a
            if list_values[0] == 'C' and list_values[1] == 'C':
                new_string = new_string[0].upper() + new_string[1:]

        if 'M' in list_values and '()' in list_values[2]:
            enter_method_function = True
            string = list_values[2].replace('()', '')
        
        if 'S' in list_values:
            if 'C' in list_values:
                new_string = ''
            for j in string:
                if str(j).isupper() and first_step:
                    new_string += ' ' + str(j)
                else:
                    new_string += str(j)
                first_step = True

            new_string = new_string.lower()
        
        if 'M' in list_values and not '()' in list_values[2] and not enter_method_function:
            new_string = new_string + '()'
    
        new_values_list.append(new_string)
    return new_values_list




if __name__ == '__main__':
    strings = []
    input_lines = sys.stdin.read().strip().split('\n')

    for line in input_lines:
        strings.append(line.replace('\r', ''))
    
    results = camel_case(strings)

    for word in results:
        print(word)


    
