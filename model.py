import id_counter, ui, save_to_file
from datetime import datetime as dt
note = []

def create_note():
    global note
    note = []
    note.append(id_counter.next_id())
    note.append(ui.input_head())
    note.append(ui.input_body())
    note.append(str(dt.now().date()) + ' ' + str(dt.now().time().strftime("%H:%M:%S")))
    return note

def start():
    while True:
        i = ui.menu()
        if i == '1':
            note = create_note()
            if ui.print_note(note) == 'y':
                save_to_file.add_note_to_file(note)
