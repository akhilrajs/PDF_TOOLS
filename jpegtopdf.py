# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 19:13:03 2021

@author: akhilrajs
"""
def jpeg_to_pdf_main():
    from time import sleep
    from os import path
    from os import makedirs
    from os import getcwd
    from os import system 
    from os import startfile
    from os import listdir
    
    folder = 'PDF of JPEG/'
    directory = (getcwd()) + "/OUTPUT/"
    SAVE_PATH = path.join(directory, folder)
    if not path.exists(SAVE_PATH):
        makedirs(SAVE_PATH)
    system("cls")
    print("# JPEG TO PDF TOOL")
    print('# author - akhilrajs')
    print('---------------------')
    sleep(1)
    print()
    print("# before running the program make sure the folder contains only images u want to make into a pdf")
    
    path = input("# drag the folder containing the images as jpegs here : ")# get the path of images
    listPages = listdir(path)
    pdfFileName = input("# enter name for PDF file : ")
    print("# creating PDF . . .")
    print("# please wait.")
    path = str(path) + "/"
    from fpdf import FPDF
    from PIL import Image
    cover = Image.open(str(path) + str(listPages[0]))
    width, height = cover.size
    
    pdf = FPDF(unit = "pt", format = [width, height])
    
    for page in listPages:
        pdf.add_page()
        pdf.image(path + str(page) + "", 0, 0)
        print("# added " + str(page))
         
    pdf.output(SAVE_PATH + pdfFileName + ".pdf", "F")
    startfile(SAVE_PATH)
    system("cls")