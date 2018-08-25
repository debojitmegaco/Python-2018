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
#Create Single Directory
os.mkdir('Python-Test-Directory') 
#Remove Single Directory
os.rmdir('Python-Test-Directory') 
#Make Recursive Directory
os.makedirs('Python-Test-Directory-001/Python-Test-SubDirectory-001/Python-Test-2SubDirectory-001')
#Delete Recursive Directory
os.removedirs('Python-Test-Directory-001/Python-Test-SubDirectory-001/Python-Test-2SubDirectory-001')

'''
#Traveresing through Directory
print("------------------------------------------")
print("Walking through directory")
print("------------------------------------------")

for dirpath,dirname,filenames in os.walk('c:/Users/Savit/Ruby'):
	print("CurrentPath :{}".format(dirpath))
	print('Directory Name: {}'.format(dirname))
	print("File-Name: {}".format(filenames))
	print("------------------------------------------")
'''

#Python OS.path 

print(os.path.exists("No_suct_file.txt"))#Returns Bolean True or False  =>False
print((os.path.basename("C:\\Users\\Savit\\python\\Os_Module.py"))) #Reten the File name OS_Modile.txt
print(os.path.splitext("Os_Module.py")) #Reurn the file Name and the extention ('Os_Module', '.py')
print(os.path.join("C:\\Users\\Savit\\python","Os_Module.py"))#joins the File Name with Path

