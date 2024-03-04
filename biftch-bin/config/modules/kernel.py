import subprocess

def main(style = "f"):
    if style == "f" or style == "full":
        return subprocess.getoutput("uname -s") + ' ' + subprocess.getoutput("uname -r")
    elif style == "s" or style == "short":
        return subprocess.getoutput("uname -r")
    else:
        return ""

#print(main("s"))
