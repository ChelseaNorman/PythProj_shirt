import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    command_argv_check()
    try:
        muppetImage = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    idealSize = shirt.size
    muppetImage = ImageOps.fit(muppetImage, idealSize)
    muppetImage.paste(shirt, shirt)
    muppetImage.save(sys.argv[2])

def command_argv_check():
    #Checks to make sure arguments are right length and match
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if check_extension(file1[1]) == False:
        sys.exit("Invalid input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid output")
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")

def check_extension(file):
    #checks to see if extensions are correct
    if file in [".jpg", ".png", ".jpeg"]:
        return True
    else:
        return False

if __name__=="__main__":
    main()