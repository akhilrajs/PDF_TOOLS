def pdf_to_jpeg_main():
    from time import sleep
    from os import path
    from os import makedirs
    from os import getcwd
    from os import system 
    from os import startfile
    from shutil import move
    from pdf2image import convert_from_path
    
    folder = 'JPEGS_of_PDF/'
    directory = (getcwd()) + "/OUTPUT/"
    SAVE_PATH = path.join(directory, folder)
    if not path.exists(SAVE_PATH):
        makedirs(SAVE_PATH)
    system("cls")
    print("# PDF TO JPEG TOOL")
    print('# author - akhilrajs')
    print('---------------------')
    sleep(1)
    print()
    PDF_location = input('''# Drag and drop the PDF here :> ''')
    print("# converting the pdf to jpeg ...")
    print("# please wait.")
    images = convert_from_path(PDF_location,500, poppler_path = r'poppler-0.68.0\bin')
    for i in range(len(images)):
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')
        source = "page" + str(i) + '.jpg'
        destination = SAVE_PATH
        move(source, destination)
        print("converted page " + str(int(i + 1)))
    system("cls")        