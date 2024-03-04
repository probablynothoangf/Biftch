import subprocess

def main(style = "f"):
    if style == "f" or style == "full":
        return subprocess.getoutput("lsb_release -ds")[1:-1]
    elif style == "s" or style == "short":
        return subprocess.getoutput("lsb_release -is")
    else:
        return ""

#print(main())
