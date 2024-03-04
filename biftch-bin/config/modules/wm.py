import subprocess

def main():
    return subprocess.getoutput("echo $XDG_SESSION_DESKTOP")

#print(main())
