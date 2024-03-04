import subprocess

def main():
    return subprocess.getoutput("echo $(pstree -sA $$ | awk -F \"---\" \'{ print $2 }\')")

#print(main())
