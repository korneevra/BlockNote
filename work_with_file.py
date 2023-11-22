

def add_note_to_file(note):
    with open('notes.csv', 'a') as data:
        for i in note:
            data.write(str(i) + ';')
        data.write('\n')

def read_list_from_file(date):
    with open('notes.csv', 'r') as data:
        list = [x for x in data]
        sort = []
        for i in list:
            if date in i:
                sort.append(i)
    return sort

def delete_note_from_file(id):
    with open('notes.csv', 'r') as data:
        list = str(data).split()
    for i in list:
        print(str(i).split(';')[0])



