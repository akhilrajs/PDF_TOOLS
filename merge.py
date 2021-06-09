import os
from merge_pdf import merge
from time import sleep 

if not os.path.exists('OUTPUT'):
        os.makedirs('OUTPUT')

folder = 'OUTPUT'
directory = os.getcwd()
SAVE_PATH = os.path.join(directory, folder)
open_output_address = SAVE_PATH
os.system("cls")
print("# MERGE TOOL")
print('# author - akhilrajs')
print('---------------------')
sleep(1)
print()
source_of_pdfs = input('''# Enter the address of the folder containing the PDFs to be merged
# Drag and drop the folder here :> ''')
name_of_output_pdf = input("enter the name of the output file without extension (example: results): ")
error_handle_path = SAVE_PATH
SAVE_PATH = str(SAVE_PATH) + "/" + str(name_of_output_pdf) + ".pdf"
print("# folder containig the PDFs : " + source_of_pdfs)
print("# destination of final PDF : " + SAVE_PATH)
print("# merging PDFs...")
try: 
    merge.Merge (SAVE_PATH).merge_folder (source_of_pdfs)
except Exception as e:
    print("# error : " + str(e))
    sleep(1)
    print("# trying to handle error ...")
    sleep(1)
    print('# changing name of output file : ' + str(name_of_output_pdf) +"_temp_")
    SAVE_PATH = error_handle_path + "/" + str(name_of_output_pdf)  + "_temp_" + ".pdf"
    sleep(1)
    print("# merging PDFs")
    try:
        merge.Merge (SAVE_PATH).merge_folder (source_of_pdfs)
        print("# PDFs merged ...")
        sleep(1)
        os.startfile(open_output_address)
        sleep(4)
    except Exception as e:
        print("# error : " + str(e))
        os.startfile(open_output_address)
        sleep(3)
    exit()
print()
print("# PDFs merged.")
sleep(2)
os.startfile(open_output_address)
sleep(2)
os.system("cls")
