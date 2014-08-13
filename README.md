# Sublime Linker

A plugin for [Sublime Text 2 and 3](http://sublimetext.com) on Ubuntu linux.

## What it does
This plugin lets you open URLs contained in the file your are viewing or editing in Sublime Text, with just a keystroke. Just position the caret over a URL, then hit `Ctrl+Enter` or `Ctrl+space`, whichever you prefer. 

You can also have it simultaneously open _all URLs_ contained in the file being viewed/edited, by using the mega keyboard combination `Ctrl+Shift+Alt+Enter`, or `Ctrl+Shift+Alt+space`, whichever you prefer.

Opens urls of types `file://` and `http(s)://`.

## Installation

Drop the plugin into Sublime Text's Packages/User folder (typically your `~/.config/sublime-text-3/Packages/User/`)

## Personalization

You can change the key combinations monitored by this plugin, by fiddling simple JSON inside the installed package. Just check out Preferences --> Key Bindings (`default` and `user`) first however, to avoid surprise collisions.

## Credits

Forked and overhauled from [Leonid Shevtsov](http://leonid.shevtsov.me)'s https://github.com/leonid-shevtsov/ClickableUrls_SublimeText

## Other platforms

It is easy to migrate to other platforms and flavours. I just didn't do/test it.

## How to debug
Hit Ctrl + ` to toggle Sublime's embedded python console
