import id_counter, ui
from datetime import datetime as dt

def create_note():
    note = []
    note.append(id_counter.next_id())
    note.append(ui.input_head())
    note.append(ui.input_body())
    note.append(str(dt.now().date()) + ' ' + str(dt.now().time().strftime("%H:%M:%S")))
    return note

# print(create_note())