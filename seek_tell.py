with open('os_module/example.txt') as f:
    f.seek(0)
    data = f.read()
print(data)

with open('os_module/example.txt') as f:
    data =f.read()

    current_position = f.tell()
print(current_position)


with open('os_module/example.txt', 'w') as f:
    f.write('jai shree ram\n')
    f.truncate(14)
    with open('os_module/example.txt', 'r') as f:
        data = f.read()
print(data)
