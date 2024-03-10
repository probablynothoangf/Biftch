<div align="center">
    <a href="https://github.com/probablynothoangf/Biftch">
        <img width="250" src="https://github.com/probablynothoangf/Biftch/blob/main/logo.png" alt="Logo">
    </a>
    <p align="center">displays your system information, with style</p>
</div>

<img align="right" width=400 src="https://github.com/probablynothoangf/Biftch/blob/main/screenshot1.png">

> [!WARNING]
> This program code is still messy and unoptimized, I'm gonna update it (and make a version for Windows because the program executes shell commands inside the code therefore it isn't compatible for Windows) when I have time. :)

> [!WARNING]
> There aren't any documentations yet about this program, so stay tuned! :)

`biftch` is a mininalistic, pretty customizable command-line fetcher, using only `python3`! (>= 3.11)

This program displays informations about your system, with style :)

This program is clearly used for flexing (because i use arch btw).

**Features**

* Minimalistic!

* Creating beautiful system information in a matter of seconds!

* Pretty much customizable!

* Modular - displays any kind of (single line) information on biftch!

**Installation**

> [!IMPORTANT]
> Be sure to have `python3` (>= 3.11) installed (check the version with`python3 --version`)

* **Method 1: Installation script(coming soon)**
* **Method 2: Manually**
  + Clone the repository (e.g using `git clone https://github.com/probablynothoangf/Biftch.git`)
  + Go to `Biftch/biftch-git`, and place the file `/bin/biftch` to `$HOME/bin/biftch` (create it if it doesn't exist)
  + Now run `sudo ln -s $HOME/bin/biftch/biftch /usr/local/bin` (check if it is installed by either `biftch --help` or `biftch --version`)
  + To make the program actually work (like displaying things), run `biftch --makeconfigpath /path/to/config_folder/` (e.g `biftch --makeconfigpath /home/probablynothoangf/.config`), this is required because the program needs to know where to load the config file
  + Now find the configs file (I stored the default config in `Biftch/biftch-bin/config`) and copy all of it's contents into the config folder you've just use in `--makeconfigpath`

Example directory structure after the installation process is done successfully:

```text
home/
└── probablynothoangf/
    ├── .config/
    │   └── biftch/
    │       ├── modules/
    │       │   ├── hostname.py
    │       │   ├── kernel.py
    │       │   └── ...
    │       ├── art
    │       ├── config.py
    │       └── layout 
    └── bin/
        └── biftch/
            ├── configpath     # this is created after running biftch --makeconfigpath
            └── biftch
```

<br clear="right"/>

That's it! Have fun :)

>[!NOTE]
>If you encounter issues, feel free to tell me about it :)
