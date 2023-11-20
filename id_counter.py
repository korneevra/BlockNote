# id = 0

def next_id():
    id = 0
    with open('id.txt', 'r') as file:
        t = file.read()
        if t == '':
            id = 1
        else:
            id = int(t) + 1
    with open('id.txt', 'w') as file:
        file.write(str(id))
    return id

# print(next_id())
# print(open('id.txt').read())
