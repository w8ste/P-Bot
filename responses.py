import sys
p_array = [sys.maxsize]


def handle_response(massage) -> str:
    if massage[0] == '!':
        massage = massage[1:]
        p_massage = massage.lower()
        if p_massage == 'obi':
            return 'Hello there! \n'
        elif p_massage[0] == 'p':
            if p_massage in p_array:
                return f'{p_massage} was mentioned already'
            else:
                p_array.append(p_massage)
                return f'Good Job, {p_massage} is a new word'

