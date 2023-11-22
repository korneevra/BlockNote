import model

def menu():
    return input('------------------\n'
                 '1. Create new note\n'
                 '2. Read note\n'
                 '3. Edit note\n'
                 '4. Delete note\n'
                 '------------------\n'
                 '>_')

def input_head():
    return input("Input head:_")

def input_body():
    return input("Input note:_")

def input_date():
    return input("Input date (YYYY-MM-DD):_")

def print_note(note):
    print('--------------------------')
    print('  ID:  ' + str(note[0]))
    print('Date:  ' + note[3])
    print('Head:  ' + note[1])
    print('Note:  ' + note[2])
    print('--------------------------')

def print_save():
    return input('Save? (Y/N) >_')

def print_edit():
    return input('Edit? (Y/N) >_')

def print_delete():
    return input('Delete? (Y/N) >_')

def print_press_enter():
    return input('Press Enter >_')

def print_save_complit_press_enter():
   return input('Save complete, Press Enter >_')

def print_delete_complit_press_enter():
   return input('Delete complete, Press Enter >_')

def print_massage(massage):
    print(massage)

def print_number_of_note():
    return input('Input number >_')

def print_list_of_notes(list):
    print('--------------------------')
    for i in list:
        data = str(i).split(';')
        print('Note: #' + data[0] + '. ' + data[1])
    print('--------------------------')
