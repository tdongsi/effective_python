
handle = open('/tmp/random_data.txt', 'w', encoding='utf-8')
handle.write('success\nand\nnew\nlines')
handle.close()

handle = open('/tmp/random_data.txt')  # Raise IOError
try:
    data = handle.read()   # Raise UnicodeDecodeError
finally:
    handle.close()
