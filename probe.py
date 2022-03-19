
for ch in ['?','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'']:
    if ch in src:
        src = src.replace(ch, " ")
print(src)


