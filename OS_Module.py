import os

#Checking method avialable for OS Module
print(dir(os))

#Check the Current Working Directory
print(os.getcwd())

#Rename a File
os.rename('news.txt','new-new.txt')
os.rename('new-new.txt','news.txt')

#Change the current working Directory
os.chdir("c:/")
print(os.getcwd())


#list inside a directory
print(os.listdir())


#MakeDirectory and Remove Diectory
#os.mkdir('Python-Test-Directory')
#os.rmdir('Python-Test-Directory')
#os.makedirs('Python-Test-Directory-001/Python-Test-SubDirectory-001/Python-Test-2SubDirectory-001')
#os.removedirs('Python-Test-Directory-001/Python-Test-SubDirectory-001/Python-Test-2SubDirectory-001')


#Traveresing through Directory
print("------------------------------------------")
print("Walking through directory")
print("------------------------------------------")

for dirpath,dirname,filenames in os.walk('c:/Users/Savit/Ruby'):
	print("CurrentPath :{}".format(dirpath))
	print('Directory Name: {}'.format(dirname))
	print("File-Name: {}".format(filenames))
	print("------------------------------------------")


