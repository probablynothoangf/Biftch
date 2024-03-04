# biftch
Display your system information with style :)

## Notice
v0.9.2

Documentation coming soon :)

so, stay tuned :)

## Installation
### Method 1: Manually

Make sure you have `python3` installed (>= 3.11)

Clone the repository using `git`

Go to `Biftch/biftch-git`, and place the file `/bin/biftch` to `$HOME/bin/biftch` (create it if it doesn't exist)

Now run `sudo ln -s $HOME/bin/biftch/biftch /usr/local/bin`

The program should work now (try `biftch --help` or `biftch --version`).

To make the program actually work (like displaying things), run `biftch --makeconfigpath /path/to/config_folder/` (e.g `biftch --makeconfigpath /home/probablynothoangf/.config`), this is required because the program needs to know where to load the config file

Now find the configs file (I stored the default config in `Biftch/biftch-bin/config`) and copy all of it's contents into the config folder you've just use in `--makeconfigpath`

Example file structure after the installation


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

That's it! Enjoy

If you encounter issues, feel free to tell me :)
