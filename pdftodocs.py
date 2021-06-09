def pdftodocs_main():
    from pdf2docx import Converter
    from time import sleep
    from os import path
    from os import makedirs
    from os import getcwd
    from os import system 
    from tabulate import tabulate
    from os import startfile
    
    if not path.exists('OUTPUT'):
            makedirs('OUTPUT')

    folder = 'OUTPUT'
    directory = getcwd()
    SAVE_PATH = path.join(directory, folder)
    open_output_address = SAVE_PATH
    system("cls")
    print("# PDF TO DOCX TOOL")
    print('# author - akhilrajs')
    print('---------------------')
    sleep(1)
    print()
    PDF = input('''# Drag and drop the PDF here :> ''')
    DOCX = input('''# Enter the name for the .docx file (example : results) : ''')
    SAVE_PATH = str(SAVE_PATH) + "/" + str(DOCX) + ".docx"
    print(tabulate([['#   1', 'Convert entire pdf to docx'],['#   2','Convert a range of pages to docx'],['#   3','Convert selected pages to docx']]))
    choice = input("# enter your choice : ")
    if choice == "1":
        print()
        print("# converting all pages to docx . . .")
        cv = Converter(PDF)
        cv.convert(SAVE_PATH)      # all pages by default
        cv.close()
    elif choice == "2":
        print()
        start_ = input("# enter the starting page : ")
        end_   = input("# enter the end page : ")
        cv = Converter(PDF)
        cv.convert(SAVE_PATH, start = start_, end = end_)
        cv.close()
    elif choice == "3":
        print()
        no_of_pages = input("# Enter the number of pages to be converted : ")
        no_of_pages = int(no_of_pages)
        print("# Enter the page numbers line by line")
        lst =[]
        for i in range(0, no_of_pages):
            pg_no = int(input())
            lst.append(pg_no)
        cv = Converter(PDF)
        cv.convert(SAVE_PATH, pages = lst)
        cv.close()
    startfile(open_output_address)
    system("cls")