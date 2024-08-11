import os

dpath = "C:\\Users\\sthor\\Downloads\\"

dirList = os.listdir(dpath)

def printdir():
    dirList = os.listdir(dpath)
    for file in dirList:
        print(file)
    


docExt = [".pdf", ".doc", ".docx", ".txt"]
pptExt = [".ppt", ".pptx", ".xlsx"]

imgExt = [".png", ".jpg"]
mediaExt = [".mp3", ".mp4"]

compressed = [".zip", ".rar"]

printdir()

        
newPaths = ["Docs", "PowerPoints","Images", "Media", "Compressed"]

for path in newPaths:
    dirChild = os.path.join(dpath, path)
    if(os.path.isdir(dirChild) == False):
        os.mkdir(dirChild)

for file in dirList:
    splitFile = os.path.splitext(file)
    fullFilePath = os.path.join(dpath, file)
    if splitFile[1] in docExt:
        os.rename(fullFilePath, os.path.join(dpath, newPaths[0]) + "\\" + file)
    elif splitFile[1] in pptExt:
        os.rename(fullFilePath, os.path.join(dpath, newPaths[1]) + "\\" + file)
    elif splitFile[1] in imgExt:
        os.rename(fullFilePath, os.path.join(dpath, newPaths[2]) + "\\" + file)
    elif splitFile[1] in mediaExt:
        os.rename(fullFilePath, os.path.join(dpath, newPaths[3]) + "\\" + file)
    elif splitFile[1] in compressed:
        os.rename(fullFilePath, os.path.join(dpath, newPaths[4]) + "\\" + file)

printdir()
