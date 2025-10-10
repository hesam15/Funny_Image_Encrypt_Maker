from PIL import Image

def decrypter(path):
    password = input('Give me your pass: ')
    pass_letters = [ord(pl) for pl in password]

    img = Image.open(path)

    first_pixel = img.getpixel((1, 1))
    second_pixel = img.getpixel((1, 2))

    if len(pass_letters) < first_pixel[2] - second_pixel[2]:
        for i in range((first_pixel[2] - second_pixel[2]) - len(pass_letters)):
            big_int = max(pass_letters)
            pass_letters.append(big_int+30)

    letters = []

    for pass_letter in pass_letters:
        r, g, b = img.getpixel((pass_letter*2, pass_letter))
        letters.append(b)

    message = [chr(letter) for letter in letters]

    print("".join(message))