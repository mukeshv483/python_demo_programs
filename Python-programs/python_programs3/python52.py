 def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]
file=open("Newfile.py","r")
str1=file.readlines()
count=len(str1)-1
for line in str1:
    print str1[count]
    count=count-1   
file.seek(0,0)
str3=reverse(file.read())
file.close();
print str3
