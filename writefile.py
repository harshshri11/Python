f= open('example.txt', 'w')
lines = ['jai shree ram 1\n', 'jai shree ram 2\n', 'jai shree ram 3\n']
f.writelines(lines)
f.close()