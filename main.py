while True:
    from tabulate import tabulate
    from time import sleep
    from os import system
    
    def main():
        print("# PDF tools")
        print("# author : akhilrajs")
        print(tabulate([['Option', 'Tool'],['------','----'],['1','Merge PDFs in a given folder'],['2','Split a PDF into individual pages']]))
        print()
        tool_selected = input("# Enter option required :> ")
        if  tool_selected =="1":
                print()
                print("# Option (1) selected : Merge PDFs of a given Folder")
                from merge import merge_main
                merge_main()
        elif tool_selected == "2":
            try:
                print()
                print("# Optoion (2) selected : Split a PDF into individual pages")
                from split import split_main
                split_main()
            except Exception as e:
                print("# ERROR : " + str(e))
        else:
            print("# invalid option entered")
            print('# try again ')
            sleep(1.2)
            system("cls")
            main()
    main()