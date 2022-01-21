pip install pytube

in pytube/cipher.py change the line:
var_regex = re.compile(r"^\w+\W")
on the
var_regex = re.compile(r"^\$*\w+\W")