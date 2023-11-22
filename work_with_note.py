import id_counter, ui, work_with_file
from datetime import datetime as dt

def create_note():
    note = []
    note.append(id_counter.next_id())
    note.append(ui.input_head())
    note.append(ui.input_body())
    note.append(str(dt.now().date()) + ' ' + str(dt.now().time().strftime("%H:%M:%S")))
    return note

def edit_note(note):
    res_note = []
    res_note.append(note[0])
    res_note.append(ui.input_head())
    res_note.append(ui.input_body())
    res_note.append(str(dt.now().date()) + ' ' + str(dt.now().time().strftime("%H:%M:%S")))
    return res_note

def find_note():
    date = ui.input_date()
    list = work_with_file.read_list_from_file(date)
    ui.print_list_of_notes(list)
    number = ui.print_number_of_note()
    note = get_note_by_number(list, number)
    if note != 0:
        ui.print_note(note)
        return note
    else:
        ui.print_massage('NO such number!')

def get_note_by_number(list, number):
    for note in list:
        data = str(note).split(';')
        if data[0] == number:
            return note.split(';')
    return 0
