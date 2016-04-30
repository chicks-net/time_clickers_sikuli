# Time Clickers automation with Sikuli

Automate time warps in [Time Clickers](http://store.steampowered.com/app/385770/) with [Sikuli](http://www.sikuli.org/).

## Setup

To get this to work you should:

* be on a Mac (otherwise the `switchApp` will probably break) - patches welcomed :bowtie:
* run Time Clickers in a Window at 1024x768
* have upgraded :trophy: **Starting Gold** 44 times - otherwise the constant in the `range(90)` for "upgrade a bunch" will be off
* have enough Weapon Cubes to have all 3 Click Weapons (Pistol :gun:, Launcher, Cannon :bomb:)

## Scripts

* [TimeWarp](https://rawgit.com/chicks-net/time_clickers_sikuli/master/TimeWarp.sikuli/TimeWarp.html) - handle a Time Warp
* [UpgradeRandomly](https://rawgit.com/chicks-net/time_clickers_sikuli/master/UpgradeRandomly.sikuli/UpgradeRandomly.html) - upgrade team members randomly
* [UpgradeEverybody](https://rawgit.com/chicks-net/time_clickers_sikuli/master/UpgradeEverybody.sikuli/UpgradeEverybody.html) - upgrade all team members evenly
* [UpgradeStepped](https://rawgit.com/chicks-net/time_clickers_sikuli/master/UpgradeStepped.sikuli/UpgradeStepped.html) - get team members into step wise fashion then upgrade them evenly

## Technical notes

I did this:

* on a Mac running OSX 10.10.5
* with SikulixIDE 1.10
