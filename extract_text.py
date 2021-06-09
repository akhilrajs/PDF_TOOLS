def extract_text_main():
    from PyPDF2 import PdfFileReader
    from time import sleep
    from time import sleep
    from os import path
    from os import makedirs
    from os import getcwd
    from os import system 
    from tabulate import tabulate
    from os import startfile
    from shutil import move
    
    folder = 'TEXT_PAGES/'
    directory = (getcwd()) + "/OUTPUT/"
    SAVE_PATH = path.join(directory, folder)
    if not path.exists(SAVE_PATH):
        makedirs(SAVE_PATH)
    system("cls")
    print("# TEXT EXTRACTION TOOL")
    print('# author - akhilrajs')
    print('---------------------')
    sleep(1)
    print()
    PDF_location = input('''# Drag and drop the PDF here :> ''')
    PDF = open(PDF_location, 'rb')
    read_pdf = PdfFileReader(PDF)
    no_of_pages = read_pdf.numPages
    print("# Number of pages : " + str(no_of_pages))
    sleep(1)
    print()
    print(tabulate([['#   1', 'Convert entire pdf to text'],['#   2','Convert a range of pages to text'],['#   3','Convert selected page to text']]))
    choice = input("# enter your choice : ")
    if choice == "1":
        print("# convert entire pdf to text")
        for i in range(0,no_of_pages):
            j = int(i) + 1
            print("# converting page " + str(j))
            page_ = "page " + str(j)
            text_file_name = page_
            page_ = read_pdf.getPage(i)
            text = page_.extractText().split("\n")
            print("# text extracted for " + text_file_name)
            text_file_location = str(SAVE_PATH) + str(text_file_name) +".txt"
            text_file = open(text_file_location,"a")
            for line_ in text:
                text_file.write(line_)
            text_file.close()
    elif choice == "2":
        print("# convert a range of pages to text")
        start = input("# enter the starting page : ")
        end = input("# enter the ending page : ")
        print()
        start = int(start) - 1
        end = int(end) - 1
        for i in range(start,end):
            j = int(i) + 1
            print("# converting page " + str(j))
            page_ = "page " + str(j)
            text_file_name = page_
            page_ = read_pdf.getPage(i)
            text = page_.extractText().split("\n")
            print("# text extracted for " + text_file_name)
            text_file_location = str(SAVE_PATH) + str(text_file_name) +".txt"
            text_file = open(text_file_location,"a")
            for line_ in text:
                text_file.write(line_)
            text_file.close()
    elif choice == "3":
        print("# convert the selected page to text ")
        page_number = input("# enter the page number :")
        text_file_name = "page " + str(page_number)
        page_number = int(page_number) - 1
        page_ = read_pdf.getPage(page_number)
        text = page_.extractText().split("\n")
        print("# text extracted for " + text_file_name)
        text_file_location = str(SAVE_PATH) + str(text_file_name) + ".txt"
        text_file =open(text_file_location, "a")
        for line_ in text:
            text_file.write(line_)
        text_file.close()
    startfile(SAVE_PATH)
    system("cls")