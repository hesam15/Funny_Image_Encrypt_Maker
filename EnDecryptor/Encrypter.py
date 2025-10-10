from PIL import Image

def encrypt(path):
    message = input('Give me your secret message: ')
    password = input('Give me your pass: ')

    new_name = input('Give me a new name: ')

    letters = [ord(l) for l in message]
    pass_letters = [ord(pl) for pl in password]

    if(len(pass_letters) < len(letters)):
        for i in range(len(letters) - len(pass_letters)):
            big_int = max(pass_letters)
            pass_letters.append(big_int+30)

    img = Image.open(path)

    r, g, b = img.getpixel((1, 2))
    img.putpixel((1, 1), (r, g, b+len(pass_letters)))

    print(len(pass_letters), len(letters))
    
    sum = 0
    for pass_letter in pass_letters:
        r,g,b = img.getpixel((pass_letter*2, pass_letter))
        img.putpixel((pass_letter*2, pass_letter), (r, g, letters[sum]))
        sum += 1

    img.save(f'./images/{new_name}.png')