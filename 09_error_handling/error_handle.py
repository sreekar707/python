file=open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()


with open('youtube.txt', 'w') as file:
    file.write("cahi aur python")