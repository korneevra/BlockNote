import model

def menu():
    return input('1. Create new note\n'
                 '2. Read note\n'
                 '3. Edit note\n'
                 '4. Delete note\n'
                 '5. Save to csv\n'
                 '>_')

def input_head():
    return input("Input head:_")

def input_body():
    return input("Input note:_")

def print_note(note):
    print('--------------------------')
    print('  ID:  ' + str(note[0]))
    print('Date:  ' + note[3])
    print('Head:  ' + note[1])
    print('Note:  ' + note[2])
    print('--------------------------')
    return input('Save? (Y/N) >_')

# print_note(model.create_note())