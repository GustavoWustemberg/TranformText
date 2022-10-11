x = 0

while x < 4:
    x = int(input('Choose one of the options below:\n'
                  '1 - Upper case\n'
                  '2 - Lower case\n'
                  '3 - Capitalize\n'
                  '4 - Close\n'))
    if x == 1:
        text = input('Digite seu texto: ').upper()
        print(text)
    elif x == 2:
        text = input('Digite seu texto: ').lower()
        print(text)
    elif x == 3:
        text = input('Digite seu texto: ').capitalize()
        print(text)
