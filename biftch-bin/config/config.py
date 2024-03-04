### BIFTCH CONFIGURATION FILE, made by probablynothoangf (https://github.com/probablynothoangf)
### 
### This is a python file (will be loaded as a module), so keep the file extension as python file extension (.py, .pyi, etc.)
### This will be loaded in program startup



### COLOR PRESETS
# Custom colors presets (custom colors are still enable but if you want ur setup to look uniformed then this is for you)
# USAGE: cN = [r,g,b] (N must be 0123456789ABCDEF)
#        if you don't need a color, just don't use them as removing them breaks the code
# To do custom colors (in selected text) you use col(string, r, g, b) (you should not)

c0 = [255,255,255]
c1 = [51,51,51]
c2 = [23,147,209]
c3 = [255,0,0]
c4 = [0,255,0]
c5 = [255,165,0]
c6 = [0,128,128]
c7 = [0,0,255]
c8 = [0,255,255]
c9 = [0,0,0]
cA = [0,0,0]
cB = [0,0,0]
cC = [0,0,0]
cD = [0,0,0]
cE = [0,0,0]
cF = [0,0,0]


### LOAD MODULES
# If you want to load your own custom modules (be sure that it is safe by inspecting the code :) ), you put the filename you want to add into the list
# Modules that are not in this list won't be loaded during runtime
# USAGE: loadlist = [('module1','args'), ('module2','args'), ('module3','args'), etc.]
#                   (args are arguments for each module, leave '' if the module doesn't require/you don't want to use arguments)
# EXAMPLE: loadlist = [('user',''), ('shell',''),('os','s')] will be available in layouts as 'user.py' <-> loadlist[0] with no arguments, 'shell.py' <-> loadlist[1] with no args, 'os.py' <-> loadlist[2] with 's' (or 'short' in the module code), which displays the module in short style (e.g: no arguments: Arch Linux, with 's' argument: Arch)

loadlist = [('user',''), ('hostname',''), ('os','s'), ('kernel','s'), ('shell',''), ('term',''), ('wm','')]


### LAYOUT PATH
# Path to the layout you want to load (required)
# e.g: '/.config/biftch/layout' means it will find the 'layout' file in '$HOME/.config/biftch/layout'

layoutpath = '/.config/biftch/layout'


### ART PATH
# Path to the art you want to load (optional)
# The load directory will start from $HOME (like LAYOUT PATH)

artpath = '/.config/biftch/art'


### RENDERING ART
# Where should i put the art (on the top, bottom, left, right to the layout)
# This is for those who want the art to be below the layout, the art to the right to the layout, etc.
# Accepted values: 'top', 'bottom', 'left', 'right'

renderart = 'top'


### ART  ALIGNMENT
# Like text alignment, but this is for the art :)
# Accepted values: 'left', 'center', 'right'
# If the art shape is rectangular (no tabs), this should be almost useless in left/right mode

aalign = 'center'


### TEXT ALIGNMENT
# Does the same thing as ART ALIGNMENT, but for the layout
# Accepted values are the same as ART ALIGNMENT

talign = 'center'


### ART/LAYOUT SEPARATOR 
# Spaces between the art and the layout
# For vertical mode ('top', 'bottom'): * any number n between 1-200 and (-1)-(-200) means |n| line breaks between 2 frames, otherwise 0 line breaks (negative values just to avoid changes when you switch mode :))
# For horizontal mode ('left', 'right'): * any number n between 1-200 means n spaces between 2 frames
#                                        * 0 means no spaces
#                                        * otherwise means automatic spaces (2 frams at the corner of the console)

spaces = -1
