print_bytes = lambda s: print(' '.join(f'{b:02x}' for b in s))


s = "Hi 🙂"

some_bytes = s.encode('utf-8')

print_bytes(some_bytes)

# some_some_bytes = s.encode('ascii')

# print_bytes(some_some_bytes)

some_some_some_bytes = s.encode('utf-16')

print_bytes(some_some_some_bytes)

some_string = some_bytes.decode('utf-16')

print(some_string)