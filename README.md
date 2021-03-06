# Sublime Linker

A plugin for [Sublime Text 2 and 3](http://sublimetext.com) on Ubuntu linux.

## What it does
This plugin lets you open URLs contained in the file your are viewing or editing in Sublime Text, with just a keystroke. Just position the caret over a URL, then hit `Ctrl + Enter` or `Ctrl + space`, whichever you prefer. 

You can also have it simultaneously open _all URLs_ contained in the file being viewed/edited, by using the mega keyboard combination `Ctrl + Shift + Alt + Enter`, or `Ctrl + Shift + Alt + space`, whichever you prefer.

If the url is a file url, opens the file in a new Sublime tab. In case of a file directory url, opens the directory.
Opens urls of types `file://` and `http(s)://`. 

## Installation

Download this repo, and drop the files directly into Sublime Text's Packages/User folder (typically your `~/.config/sublime-text-3/Packages/User/`). If any of the configuration files are already there - bummer - you'll have to merge rather than overwrite. Hope to properly package this later on... 

## Personalization

You can change the key combinations monitored by this plugin, by fiddling simple JSON inside the installed package. Just check out Preferences --> Key Bindings (`default` and `user`) first however, to avoid surprise collisions.

## Credits

Forked and overhauled from [Leonid Shevtsov](http://leonid.shevtsov.me)'s https://github.com/leonid-shevtsov/ClickableUrls_SublimeText

## Other platforms

It is easy to migrate to other platforms and flavours. I just didn't do/test it.

## How to debug
Hit Ctrl + ` to toggle Sublime's embedded python console
