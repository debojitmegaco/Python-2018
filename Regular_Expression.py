import re

string = 'This line having ip address 192.168.92.1'

regex = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
mo = regex.search(string)
print(f'print IP address : {mo.group()}')
#print IP address : 192.168.92.1

string = 'My land Line number is 033-2577-2247'
regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
mo = regex.search(string)
print(f'my land line number is {mo.group()}')
#my land line number is 033-2577-2247


regex = re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
mo = regex.search(string)
print(f'my area line number is {mo.group(1)}')
#my area line number is 033


string1 = "Robert's number is 033-2577-2246"
string2 = "Paul's number is 2577-2233"

regex = re.compile(r'(\d\d\d-)?(\d\d\d\d-\d\d\d\d)')
mo1 = regex.search(string1)
mo2 = regex.search(string2)

print(f"Robert's Number is {mo1.group(2)}")
print(f"Paul's Number is {mo2.group(2)}")
#Robert's Number is 2577-2246
#Paul's Number is 2577-2233


string = 'Hello this is string starts with Hello and Ends with number 123456789'
regex1= re.compile(r'^Hello')
regex2= re.compile(r'\d+$')
mo1=regex1.search(string)
mo2=regex2.search(string)
print(mo1.group())
print(mo2.group())
#Hello
#123456789
