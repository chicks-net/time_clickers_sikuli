# Time Clickers automation with Sikuli

[![GPLv2 license](https://img.shields.io/badge/License-GPLv2-blue.svg)](https://github.com/chicks-net/time_clickers_sikuli/blob/master/LICENSE)

Automate time warps in [Time Clickers](http://store.steampowered.com/app/385770/) with [Sikuli](http://www.sikuli.org/).

## Setup

To get this to work you should:

* be on a Mac (otherwise the `switchApp` will probably break) - patches welcomed :bowtie:
* run Time Clickers in a Window at 1024x768
* have upgraded :trophy: **Starting Gold** 44 times - otherwise the constant in the `range(90)` for "upgrade a bunch" will be off
* have enough Weapon Cubes to have all 3 Click Weapons (Pistol :gun:, Launcher, Cannon :bomb:)

## Scripts

* [TimeWarp](https://chicks-net.github.io/time_clickers_sikuli/TimeWarp.sikuli/TimeWarp.html) - handle a Time Warp
* [UpgradeRandomly](https://chicks-net.github.io/time_clickers_sikuli/UpgradeRandomly.sikuli/UpgradeRandomly.html) - upgrade team members randomly
* [UpgradeEverybody](https:///chicks-net.github.io/time_clickers_sikuli/UpgradeEverybody.sikuli/UpgradeEverybody.html) - upgrade all team members evenly
* [UpgradeStepped](https:///chicks-net.github.io/time_clickers_sikuli/UpgradeStepped.sikuli/UpgradeStepped.html) - get team members into step wise fashion then upgrade them evenly

## Technical notes

I did this:

* on a Mac running OSX 10.10.5
* with SikulixIDE 1.10
