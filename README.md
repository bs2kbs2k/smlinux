#  smlinux -Super Mario Linux- Install Build Update Script
<img src=https://github.com/enigma9o7/smlinux/raw/screenshot/MarioPC-small.png> 
<img src=https://github.com/enigma9o7/smlinux/raw/screenshot/screenshot1.jpg>

# 
1. Installs Required Packages (build tools & dependencies)
2. Installs latest version of itself to user path 
3. Clones (downloads) sm64 source repository from Github
4. Extract Assets from ROM and prepares for use
5. Optionally applies community sourced upscale modifications 
6. Makes (compiles and links) into binary
7. Creates Menu Entry & Desktop Shortcut
8. Launches Super Mario 64 on your Personal Computer or Android Device!

...and! you can use it again later to quickly rebuild and sync to the latest updates from github.
 
## **Download & Installation Instructions**    

Paste either of the following into a terminal:  
(*Both commands do the exact same thing using different tools; use whichever works for you.*)
               
	bash -c "$(curl -fsSL https://raw.githubusercontent.com/enigma9o7/smlinux/master/smlinux)"
OR
	
	wget https://raw.githubusercontent.com/enigma9o7/smlinux/master/smlinux;bash smlinux;rm smlinux
	
	
That's all you have to do for mac and ubuntu based linux. You will be prompted to approve build options, specify your romfile,  and if needed provide password to install build tools.  smlinux will then run unattended and before the time you finish reading the FAQ you will hear "It's me, Mario!".  
(**Do not run smlinux as root; you will be prompted for password automatically if needed during installation.**)

You must provide your own legally backed up Super Mario 64 ROM file during smlinux installation. 

smlinux will be installed in the first directory in your path, usually ~/bin. After initial installation, just type `smlinux` when you want to use smlinux to update your current version or build another.   Note: If the first directory in your path requires root to write to, smlinux will use ~/bin and instruct you how to manually add it to path or reboot before next use.

If for some reason the process freezes during compilation, perhaps on pc with low memory, then set `MAXJOBS=1`. When undefined, smlinux will run make with multiple jobs at once which speeds up the build process on PCs with multiple cores and plenty of memory, but occasionally causes issues on under-powered systems (that can still run the game just fine).

[<strong>What about Linux distros that are not Ubuntu-based?</strong>](#what-about-distros-other-than-ubuntu)  
Install dependencies first or add reccommended list to smlinux config file - click for details.

**_macOS notes_**
Only sm64ex and cheaterex are fully supported, although should have coop working shortly and will change this note then; web could likely be fixed upon request if not working already; and likely android easily added upon request.  R96ex will work when they pull malloc fix from sm64ex. DOS builds wont work. If you dont already have homebrew and/or apple command line tools installed, smlinux will install them but you may have to enter your password more than once and it can take quite a while to install that stuff first before the actual build tools smlinux depends on can even be installed.  Feedback appreciated, so far only confirmed in Sierra, High Sierra, Mojove and Big Sur virtual machines.  

[<strong>Jump to FAQ Table of Contents</strong>](#frequently-asked-questions) 

<img src=https://github.com/enigma9o7/smlinux/raw/screenshot/screenshot2.jpg>
<img src=https://github.com/enigma9o7/smlinux/raw/screenshot/screenshot3.jpg>

# Frequently Asked Questions
* [<strong>How to download and install?</strong>](#download--installation-instructions)      
* [<strong>What preset/repo/branch should I use?</strong>](#what-presetrepobranch-should-i-use)
* [<strong>What does the InstallHD=1 option do?</strong>](#what-does-the-installhd1-option-do)
* [<strong>What about other branches?</strong>](#what-about-other-branches)
* [<strong>When to use RENDER_API=GL_LEGACY?</strong>](#when-to-use-render_apigl_legacy)
* [<strong>How to update, rebuild, or change build options later?</strong>](#how-to-update-rebuild-or-change-build-options-later)
* [<strong>How do I build a different version?</strong>](#how-do-i-build-a-different-version)
* [<strong>How to I configure options like controllers, camera, rumble, etc?</strong>](#how-to-i-configure-options-like-controllers-camera-rumble-etc)
* [<strong>Where are my configuration files and saved games stored?</strong>](#where-are-my-configuration-files-and-saved-games-stored)
* [<strong>Are there any cheats?</strong>](#are-there-any-cheats)
* [<strong>How do I apply external data such as textures?</strong>](#how-do-i-apply-external-data-such-as-textures)
* [<strong>How to apply a patch?</strong>](#how-to-apply-a-patch)
* [<strong>How to remove a patch?</strong>](#how-to-remove-a-patch)
* [<strong>What about distros other than Ubuntu?</strong>](#what-about-distros-other-than-ubuntu)
* [<strong>How do I create my rom file?</strong>](#how-do-i-create-my-rom-file)
* [<strong>How do I remove everything smlinux created during install?</strong>](#how-do-i-remove-everything-smlinux-created-during-install)
* [<strong>How do I tell smlinux to download sm64 repositories to a folder other than home?</strong>](#how-do-i-tell-smlinux-to-download-sm64-repositories-to-a-folder-other-than-home)
<img src=https://github.com/enigma9o7/smlinux/raw/screenshot/presets.png>

## **What preset/repository/branch should I use?**
If you want to build for PC, the source repository from the team who decompiled the rom, sm64-port, offers the cleanest code and duplication of N64, with currently very few add-ons available.  The unofficial forks, sm64ex and sm64nx, include enhancements and support for many add-ons (which are optional on sm64ex).  sm64ex offers the most flexibility, but you are encouraged to build more than one and try for yourself.  Further forks of sm64ex offer additional enhancements, such as render96ex with added Luigi Keys, sm64ex-coop for a 2 player network mode, or cheaterex for all the latest experimental add-ons. For android or web, presets are available based on sm64-port or sm64ex, while for for dos sm64-port based forks are used. 

## **What does the InstallHD=1 option do?**

See the presets table above the FAQ for details.  This will usually modify your source with the repo-provided 60fps patch, HD Mario (Old School V2) and HD Bowser character models from #modding-releases , and apply the 3D Coin Patch (V2).  Additionally, on the sm64pc/sm64ex based forks upscaled textures will be added to your build from the Cleaner Aesthetics github repo, and hq sounds from MapAnon's github release.
On the render96ex fork, the latest Render 96 Model Pack and Render 96 Texture Pack will be applied.  Note these are large so require more download time, game load time, and better comupter to perform well.
*Note that precaching these textures will make the game use more memory and increase initial startup time, but may be necessary for some computers.*

On the sm64nx fork only, 60fps is already default, and with InstallHD in addition to the models and textures mentioned above, a few other add-ons are obtained which can be enabled from the in-game menu if you prefer, including SGI models and HD Luigi.

Some of these addons require files remaining available in discord or github, so not gauranteed to work.  What is included with this option may periodically change as new mods are released. See presets table for more details.

## **What about other branches?**

If you chose one of the presets, an appropriate branch is used automatically.  For `PRESET=sm6ex` the nightly branch is used; if you would like the master branch instead use `PRESET=sm64pc`. If sm64ex nightly works for you, I'd reccommend it as it is the most updated, but if a recent change causes build failure or other problems, use the more stable sm64pc master. For advanced users, branches other than those defined by preset can be built by setting `PRESET` to any unknown name, in which case the user specified `GIT` and `BRANCH`settings are used and folder named after user defined `PRESET`.

## **When to use RENDER_API=GL_LEGACY?** 
*only applies to sm64pc/sm64ex based forks*

For old video cards that support OpenGL 1.1 but not 2.1 (from year 200X).  Check your OpenGL version with the following command: 
	
	glxinfo | grep "OpenGL version"
 
If 1.1-2.0, you must use the legacy renderer.  For 2.1 or greater, standard GL renderer is reccommended, although some old computers that do support 2.1 may perform better with the legacy renderer.

## **How to update, rebuild, or change build options later?**
    
	smlinux update <options>
For example: 
 
	smlinux update
	       or
	smlinux update --hd
	       or
	smlinux update --config
		or
	smlinux update --sgi

Updates existing install to latest from github while retaining custom textures and addons.  If updated source fails to build, restores previous build.

You can also use this option to rebuild after you apply patches or edit your source or source assets like actors manually.

Note` --config` is only needed if `CONFIG=0` in your config file, otherwise it will come up automatically.

Note` --hd` only needs to be applied if `UpdateHD=0` in smlinux configuration, and what was initally installed with`InstallHD=1` has changed/updated since you last built, or if you wish to add HD add-ons to an existing build that was made with `InstallHD=0`.

Note smlinux automatically saves one previous build by adding the suffix .old to its foldername (and restores it if your update fails to build). If you want prevent it from being erased during the next update, rename it (anything) before running smlinux, for example: 
 
	mv ~/sm64pc/build/us_pc.old ~/sm64pc/build/firstbuild

## **How do I build a different version?**

	smlinux build --config

Change your preset to another version and it will be installed in its own folder with its own seperate menu entry.  You can build as many versions as you like.  If you wish to build a version other than a predefined preset, leave preset blank or make your own name (which will be used for its foldername), and set GIT and BRANCH.

Note `--config` is only necessary if `CONFIG=0`and/or you havent edited your smlinuxcfg.txt before build.


## **How to I configure options like controllers, camera, rumble, etc?**
*dont not apply to sm64-port repository*

Pause then press R with controller or R_Shift with keyboard. For the controller settings, it is recommended to keep the first column for keyboard controls and using the middle for controller. Use the third column if you want additional keys/buttons assigned to the same function, or for mouse buttons. Be sure to map something to L for use with the camera or cheats. I personally enable mouse control for camera and turn up my aggression and pan up to 100. 

You can also just edit the configuration file with a text editor.

## **Where are my configuration files and saved games stored?**

~/.local/share/sm64pc smlinux and sm64pc/ex master  
~/.local/share/sm64ex sm64ex nightly  
~/.local/share/render96ex render96ex *only if launched with shortcut*  
~/.local/share/sm64ex-coop sm64ex-coop 
~/.local/share/cheaterex cheaterex *only if launched with shortcut*    
~/.local/share/sm64-port sm64-port *only if launched with shortcut*    
~/.local/share/sm64nx sm64nx *smlinux creates links in game dir*  

## **Are there any cheats?**
*only applies to sm64pc/sm64ex and sm64nx based builds*

Some cheats are built in and enabled automatically if launched from shortcut and available in options menu.  On compatible sm64ex basd versions additional cheats are applied with $4Y$'s CHEATER patch.

## **How do I apply external data such as textures?**

Texture and sound packs can be added to the appropriate resource folder after build.

sm64pc/sm64ex:  
Put the zipfile (or gfx or sound folder) directly into build/us_pc/res and the next time you run the game it'll use it automatically.  The zip file must contain a "gfx" and/or "sound" folder. Do not move or remove base.zip, it should remain in "res" as fallback.
  
sm64nx:  
Create a subdirectory in build/us_pc/romfs for each pak and place the pak file inside, and the next time you run the game it'll load that pak automatically. If you would prefer it to start disabled, use ~ at the beginning of the folder name.  Do not move or remove !!base.pak, it should remain in "romfs" as fallback.

## **How to apply a patch?**
*change path from sm64pc to sm64-port or sm64ex for newer repos*

Put the patch file into ~/sm64pc/enhancements (or specify the path differently when applying):
   
	cd ~/sm64pc
	git apply enhancements/filename.patch
	smlinux update
	
If the patch errors when you try to apply it, and you want to use it anyway, you can force it to apply with:
	
	git apply --reject enhancements/filename.patch

## **How to reverse (remove) a patch?** 
*change path from sm64pc to sm64-port or sm64ex for newer repos*
   
	cd ~/sm64pc
	git apply -R enhancements/filename.patch
	smlinux update


## **What about distros other than Ubuntu?**
*Tested on Bodhi 5.1,32 & 64-bit, so should work as-is on recent Ubuntu/debian. Arch and Fedora also confirmed working by users.*

Change your `Linux=` parameter during first install to one that works with your distro such as those listed below, or just install dependencies first and run smlinux with `Linux=""` (or just ignore the error from apt).  smlinux only installs dependendencies automatically during the very first installation; if you wish to force reinstallation append ` --depends` during next update or build.

If your distro needs additional dependencies not listed here, please let me know their names so I can add them.  The Ubuntu list is confirmed complete even on WSL.  Some build targets depend on an additional package not listed below.  Android builds require the android-sdk package, web targets emscriptem sdk, dos targets djgpp, and sm64nx requires g++-8 or higher.  smlinux will attempt to install these as needed, but updating gcc will only be attempted if apt is present, other distros will need to install manually.  If gcc --version does not report 8 or newer when building sm64nx, smlinux will attempt first to install gcc-9 then if unsuccesful gcc-8.  (Note Ubuntu 20.04 build-essential provides gcc9.3, whereas for 18.04 its gcc7.5.)  

Arch: 
    
	sudo pacman -S base-devel python audiofile sdl2 glew python-zstandard python-pip zstd zenity
Debian / Ubuntu:  

	sudo apt install -y build-essential bsdmainutils binutils wget git python3 libaudiofile-dev libglew-dev libsdl2-dev libusb-1.0-0-dev libzstd-dev python3-pip zenity mplayer
	
Fedora  / Red Hat:

	sudo dnf install make gcc python3 audiofile-devel glew-devel SDL2-devel zstd zenity g++
openSuSE:

	sudo zypper in gcc make python3 libaudiofile1 glew-devel libSDL2-devel zenity
Solus:
	
	sudo eopkg install make gcc python3 audiofile-devel glew-devel sdl2-devel zenity

Void: 

	sudo xbps-install -S base-devel python3 audiofile-devel SDL2-devel glew-devel zstd zenity
Alpine:

	sudo apk add build-base python3 audiofile-dev sdl2-dev glew-dev zenity
	
MacOS:

	brew install libxdg-basedir coreutils git wget nano mingw-w64 gcc@9 sdl2 pkg-config glew glfw3 libusb audiofile unzip unrar newt go python3

MinGW64: 
	
	pacman -S mingw-w64-x86_64-glew mingw-w64-x86_64-SDL2 python3 git make mingw-w64-x86_64-gcc
	
MinGW32:

	pacman -S mingw-w64-i686-glew mingw-w64-i686-SDL2 python3 git make mingw-w64-x86_i686-gcc

## **How do I create my rom file?**

Backup N64 cartridge with a dumper such as Retrode2 or Mr. Backup, from Wii with vcromclaim, or buy for Wii U Virtual Console and extract with title dumper or other homebrew tools.  
[Dragonbox Store](https://www.dragonbox.de/en/accessories/cartridge-dumper/retrode2-with-all-plugins) &nbsp; [Stoneage Gamer](https://stoneagegamer.com/retrode-2-cart-reader-rom-dumper-for-super-nintendo-genesis-more.html) &nbsp; 
[Nintendo Wii U Store](https://www.nintendo.com/games/detail/super-mario-64-wii-u) &nbsp; [WiiU Title Dumper](https://gbatemp.net/threads/ddd-wiiu-title-dumper.418492) &nbsp; [Wii Virtual Console ROM Claim]( https://github.com/JanErikGunnar/vcromclaim)  
*Note that 3D All-Stars contains the Shindou version of the ROM which isn't fully supported by PC port.*  
## **How do I remove everything smlinux created during install?**
 
	smlinux purge
This erases everything created running smlinux including automatically created game saves and config files.
This does not remove any packages installed as build tools or dependencies. Remove those with your package manager.
(Development libraries can always safely be removed if you don't plan to build again, and binaries will still run.)
This also does not restore or remove any prior sm64 folders backed up if you ran full install more that once (versus update);
delete those folders manually from any file manager.
## **How do I tell smlinux to download sm64 repositories to a folder other than home?**

	smlinux config
Set BASEPATH= to any existing path that you have permission to write to. 
