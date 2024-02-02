string1="aaa新年快乐bbb"
string2=string1.replace("新年快乐", "恭喜发财")
print(string2)

string3="aaa新年快乐bbb新年快乐ccc"
string4=string3.replace("新年快乐", "恭喜发财", 2)
print(string4)

string5='aaa,."bbb'
string6=string5.replace(',', '，')
string6=string6.replace('.', '。')
string6=string6.replace('"', '“')
print(string6)