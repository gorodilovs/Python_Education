colors = ['red', 'green', 'blue']

# Select mode to file
data = open('file.txt', 'a')
data.writelines(colors)
data.close()

# Auto-close file
with open('file.txt', 'w') as data:
    data.write('line1\n')
    data.write('line2\n')

# Read file and print it to console
path = 'file.txt'
data = open('file.txt', 'r')
for line in data:
    print(line)
data.close()
