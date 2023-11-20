

def add_note_to_file(note):
    with open('notes.csv', 'a') as data:
        for i in note:
            data.write(str(i) + ';')
        data.write('\n')