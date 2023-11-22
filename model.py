import id_counter, ui, work_with_file, work_with_note
from datetime import datetime as dt


def start():
    while True:
        i = ui.menu()
        if i == '1':   #Create new note
            note = work_with_note.create_note()
            ui.print_note(note)
            if ui.print_save() == 'y':
                work_with_file.add_note_to_file(note)

        elif i == '2':  #Read note
            work_with_note.find_note()
            ui.print_press_enter()

        elif i == '3':  #Edit note
            note = work_with_note.find_note()
            if ui.print_edit() == 'y':
                note = work_with_note.edit_note(note)
                if ui.print_save() == 'y':
                    if work_with_file.delete_note_from_file(note[0]):
                        work_with_file.add_note_to_file(note)
                        ui.print_save_complit_press_enter()
                    else:
                        ui.print_massage('Note NOT saved!')

        elif i == '4': #Delete note
            note = work_with_note.find_note()
            if ui.print_delete() == 'y':
                if work_with_file.delete_note_from_file(note[0]):
                    ui.print_delete_complit_press_enter()
                else:
                    ui.print_massage('Note NOT deleted!')

        else:
            ui.print_massage('Wrong number!!!')






