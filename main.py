from tabulate import tabulate
from time import sleep
import os

def main():
    print(tabulate([['Option', 'Tool'],['------','----'],['1','Merge PDFs in a given folder']]))
    print()
    tool_selected = input("# Enter option required :> ")
    if  tool_selected =="1":
            print()
            print("# Option (1) selected : Merge PDFs of a given Folder")
            import merge
    else:
        print("# invalid option entered")
        print('# try again ')
        sleep(1.2)
        os.system("cls")
        main()
main()