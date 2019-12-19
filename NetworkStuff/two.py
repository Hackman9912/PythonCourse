# plain text ABCDEFGHIJKLMNOPQRSTUVWXYZ
# cipher text LMNOPQRSTUVWXYZABCDEFGHIJK

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

str_in = input('Enter the word to convert: ').upper()
shift = int(input("Shift value, like 13: "))
n = len(str_in)
str_out = ''
for i in range(n):
    c = str_in[i]
    loc = alpha.find(c)
    new_loc = (loc + shift)%26
    str_out += alpha[new_loc]
print(f'Garbled, {str_out}')