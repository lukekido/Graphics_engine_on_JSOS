This is a fork from randomusbs11's AutoVM, from replit.
In this fork I'll try to build Tengoku- over it and implement the graphics engine runtime to run on (async) parallel.

---

# Variables

`MEMORY = ` variable is the variable that is used to assign memory to the VM in Megabytes. I used 256 MB of RAM as the default.

`HDD_SPACE = ` variable is how much HDD space will be created when VM is run.

`SHOW_CREDITS = ` variable shows my handle.

`ISO_URL = ` variable is set to the ISO to download. Remember to set the link to an ISO file, not a redirect URL!

`AUTOSTART = ` variable is used when modifying the Repl name so that Replit does not keep restarting repl.

`FULLSCREEN = ` variable is used to tell QEMU to put VM in Fullscreen.

---

# How to set it up for yourself?
You can leave the default variables and only change the `ISO_URL = ` variable if you want to just run something. If you want to tinker more, then try changing some of the variables. What those variables do is listed above. Remember to only change the Variables, not the code.

# Future plans
- Allow for unzipping zipped ISOs
- Stop working if ISO is not detected.
- Integration with Tengoku- project
