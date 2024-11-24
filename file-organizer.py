#!/usr/bin/env python3

import os, sys, shutil



def create_storage_folder(folder_name: str) -> None:
    if os.path.isdir(folder_name):
        return
    os.mkdir(folder_name)


def organize_file_into_specific_folder(file_name: str) -> None:
    if file_name.endswith(".jpg")      \
        or file_name.endswith(".png")  \
        or file_name.endswith(".gif")  \
        or file_name.endswith(".eps")  \
        or file_name.endswith(".bmp")  \
        or file_name.endswith(".svg")  \
        or file_name.endswith(".ico")  \
        or file_name.endswith("flif"):
        # An image file
        shutil.move(file_name, "./Images/")
        return
    
    if file_name.endswith(".mp3")      \
        or file_name.endswith(".wav")  \
        or file_name.endswith(".aiff") \
        or file_name.endswith(".aac")  \
        or file_name.endswith(".flac") \
        or file_name.endswith(".ogg"):
        # An audio file
        shutil.move(file_name, "./Audios/")
        return

    if file_name.endswith(".mp4")       \
        or file_name.endswith(".avi")   \
        or file_name.endswith(".mov")   \
        or file_name.endswith(".wmw")   \
        or file_name.endswith(".flac")  \
        or file_name.endswith(".ogg"):
        # An audio file
        shutil.move(file_name, "./Videos/")
        return

    if file_name.endswith(".zip")      \
        or file_name.endswith(".rar")  \
        or file_name.endswith(".7z")   \
        or file_name.endswith(".cpt")  \
        or file_name.endswith(".tar")  \
        or file_name.endswith(".gz"):
        # An archive file
        shutil.move(file_name, "./Archives/")
        return

    if file_name.endswith(".xls") \
        or file_name.endswith(".xlsx") \
        or file_name.endswith(".xlsm") \
        or file_name.endswith(".xltm") \
        or file_name.endswith(".ods"):
        # An Excel Spreadsheet file
        shutil.move(file_name, "./Data/EXCEL-data")
        return

    if file_name.endswith(".doc")       \
        or file_name.endswith(".docx")  \
        or file_name.endswith(".odt"):
        # A Word document file
        shutil.move(file_name, "./Docs/")
        return

    if file_name.endswith(".ppt")        \
        or file_name.endswith(".pptx")   \
        or file_name.endswith(".pptsx")  \
        or file_name.endswith(".odp"):
        # A PPTX presentation file
        shutil.move(file_name, "./Presentations/")
        return

    if file_name.endswith(".pdf"):
        # A PDF file
        shutil.move(file_name, "./PDFs/")
        return

    if file_name.endswith(".txt"):
        # A text file
        shutil.move(file_name, "./Text/")
        return

    if file_name.endswith(".xml"):
        # A XML file
        shutil.move(file_name, "./Data/XML-data")
        return

    if file_name.endswith(".yaml"):
        # A YAML file
        shutil.move(file_name, "./Data/YAML-data")
        return

    if file_name.endswith(".csv"):
        # A CSV file
        shutil.move(file_name, "./Data/YAML-data")
        return





def iterate_files_in_cwd() -> None:
    for dir_entry in os.listdir(os.getcwd()):
        if not os.path.isfile(dir_entry):
            continue
        organize_file_into_specific_folder(dir_entry)

    





def main():
    create_storage_folder("./Images/")
    create_storage_folder("./Audios/")
    create_storage_folder("./Videos/")
    create_storage_folder("./Docs/")
    create_storage_folder("./PDFs/")
    create_storage_folder("./Archives/")
    create_storage_folder("./Data/")
    create_storage_folder("./Data/XML-data")
    create_storage_folder("./Data/YAML-data")
    create_storage_folder("./Data/JSON-data")
    create_storage_folder("./Data/CSV-data")
    create_storage_folder("./Data/EXCEL-data")
    create_storage_folder("./Presentations/")
    create_storage_folder("./Text/")
    create_storage_folder("./Others/")

    iterate_files_in_cwd()



if __name__ == '__main__':
    main()
