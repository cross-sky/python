import os

path = 'C:\DRIVERS'

def travelTree(currentPath, count):

    if not os.path.exists(currentPath):
        print('path does not exit!')
        return

    if os.path.isfile(currentPath):
        fileName = os.path.basename(currentPath)
        print('t'*count + '|--' + fileName)
    elif os.path.isdir(currentPath):
        print('t'*count + '|--' + currentPath)
        pathList = os.listdir(currentPath)
        for eachPath in pathList:
            travelTree(currentPath+ '/' + eachPath,count + 1)

travelTree(path, 1)

'''
os.path basename listdir 递归
'''