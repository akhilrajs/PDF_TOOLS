while True:
    def main():
        print("# PDF tools")
        print("# author : akhilrajs")
        from tabulate import tabulate
        print(tabulate([['Option', 'Tool'],['------','----'],['1','Merge PDFs in a given folder'],['2','Split a PDF into individual pages'],
                        ['3','Extract text from PDF']
                        ,['4','Convert PDF to JPEG']]))
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
                print("# Option (2) selected : Split a PDF into individual pages")
                from split import split_main
                split_main()
            except Exception as e:
                print("# ERROR : " + str(e))
        elif tool_selected == "3":
            try:
                print()
                print("# Option (3) selected : Extract text from PDF")
                from extract_text import extract_text_main
                extract_text_main()
            except Exception as e:
                print("# ERROR : " + str(e))
        elif tool_selected == "4":
            try:
                print()
                print("# Option (4) selected : Convert PDF to JPEG")
                from pdftojpeg import pdf_to_jpeg_main
                pdf_to_jpeg_main()
            except Exception as e:
                print("# ERROR : " + str(e))
        else:
            print("# invalid option entered")
            print('# try again ')
            from time import sleep
            sleep(1.2)
            from os import system
            system("cls")
            main()
    main()