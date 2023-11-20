

def add_note_to_file(note):
    with ('notes.csv', 'w') as file:
        # for i in note:
        file.write(';')
        # file.write('\n')