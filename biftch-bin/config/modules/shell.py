import subprocess

def main():
    return subprocess.getoutput("echo ${SHELL##*/}")

#print(main())
