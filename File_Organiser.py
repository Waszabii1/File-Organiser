import os
import shutil

img = (".jpg", ".png", ".jpeg", ".gif")

spread = (".xlsx", ".xlsm")

docs = (".docx", ".dotx", ".dotm", ".doc", ".dot", ".wbk")

pdfs = (".pdf")

ppts = (".ppt", ".pot", ".pps", ".ppa", ".pptx", ".pptm")


folders = ["Images", "Spreadsheets", "Documents", "PDF's", "PowerPoints", "IDK"]
final_path = ("C:\\XXXX\\XXXXX\\XXXXX\\")

for folder in folders:
        paths = os.path.join(final_path,folder)
        try:
            os.mkdir(paths)
        except OSError as error:
            print(error)


def is_image(file):
    return os.path.splitext(file)[1] in img
def is_spreadsheet(file):
    return os.path.splitext(file)[1] in spread
def is_doc(file):
    return os.path.splitext(file)[1] in docs
def is_pdf(file):
    return os.path.splitext(file)[1] in pdfs
def is_ppts(file):
    return os.path.splitext(file)[1] in ppts

os.chdir("C:\\XXXXX\\XXXXX\\XXXXX - XXXXX")

count = 0

for file in os.listdir():
    if is_image(file):
        shutil.move(file, "C:\\XXXXX\\XXXXX\\XXXXX\\Images")
        count += 1
    elif is_spreadsheet(file):
        shutil.move(file, "C:\\XXXXX\\XXXXX\\XXXXX\\Spreadsheets")
        count += 1
    elif is_doc(file):
        shutil.move(file, "C:\\XXXXX\\XXXXX\\XXXXX\\Documents")
        count += 1
    elif is_pdf(file):
        shutil.move(file, "C:\\XXXXX\\XXXXX\\XXXXX\\PDF's")
        count += 1
    elif is_ppts(file):
        shutil.move(file, "C:\\XXXXX\\XXXXX\\XXXXX\\PowerPoints")
        count += 1
    else:
        shutil.move(file, "C:\\XXXXX\\XXXXX\\XXXXX\\IDK")
        count += 1
print(str(count) + " files moved")


