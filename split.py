def split_main():
    from os import system 
    from time import sleep
    from os import path
    from os import makedirs
    from os import getcwd 
    from os import startfile
    from PyPDF2 import PdfFileWriter, PdfFileReader
    from shutil import move
    
    folder = 'SPLIT_PAGES'
    directory = (getcwd()) + "/OUTPUT/"
    SAVE_PATH = path.join(directory, folder)
    if not path.exists(SAVE_PATH):
        makedirs(SAVE_PATH)

    system("cls")
    print("# SPLIT TOOL")
    print('# author - akhilrajs')
    print('---------------------')
    sleep(1)
    print()
    source_pdf_address = input('''# Drag and drop the PDF here :> ''')
    source_pdf = PdfFileReader(open(source_pdf_address, "rb"))
    pdf_info = (source_pdf.getDocumentInfo())
    print()
    sleep(0.5)
    print("# PDF details")
    print("# -----------")
    sleep(0.5)
    print("# Author : " + str(pdf_info.author))
    sleep(0.5)
    print("# Created by : " + str(pdf_info.creator))
    sleep(0.5)
    print("# Produced by : " + str(pdf_info.producer))
    sleep(0.5)
    print("# Title : " + str(pdf_info.title))
    sleep(0.5)
    print("# No of pages :" + str(source_pdf.numPages))
    print("# splitting document ")
    sleep(1)
    print()

    for page in range(source_pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(source_pdf.getPage(page))    
        output_filename = '{}page {}.pdf'.format("", page+1)    
        with open(output_filename, 'wb') as out:
            pdf_writer.write(out)
            print('Created : {}'.format(output_filename))
        source = output_filename
        destination = SAVE_PATH
        move(source, destination)

    startfile(SAVE_PATH)
    system("cls")