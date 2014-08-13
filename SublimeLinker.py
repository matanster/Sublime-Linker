import sublime
import sublime_plugin
import webbrowser
import re, os, os.path
import platform
import subprocess

#
# Forked from https://github.com/leonid-shevtsov/ClickableUrls_SublimeText
# Also inspired by https://github.com/jturcotte/SublimeClipboardPath
#

class UrlOpener(sublime_plugin.EventListener):
    print("SublimeLinker plugin instantiated")
    # Thanks Leonid Shevtsov https://github.com/leonid-shevtsov/ClickableUrls_SublimeText
    # Thanks Jeff Atwood http://www.codinghorror.com/blog/2008/10/the-problem-with-urls.html
    # ^ that up here is a URL that should be matched
    WEB_URL         = "\\bhttps?://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&@#/%=~_(|]"
    FILE_OR_DIR_URL = "\\bfile?://[-A-Za-z0-9+&@#/%?=~_()|!:,.;]*[-A-Za-z0-9+&@#/%=~_(|]"

    # TODO this amount should be configurable
    # TODO URL underlining should also be disableable from the config
    MAX_URLS = 200

    urls_for_view = {}
    scopes_for_view = {}
    ignored_views = []

def open_file(path):
    print("SublimeLinker plugin opening file " + path)
    sublime.active_window().open_file(path)

def open_directory(path):
    print("SublimeLinker plugin opening directory " + path)
    if platform.system() == "Windows":
        command = "explorer " + path
    if platform.system() == "Linux":
        command = ["/usr/bin/nautilus", path] # see http://askubuntu.com/questions/31069/how-to-open-a-file-manager-of-the-current-directory-in-the-terminal for possibly more genericism
    subprocess.Popen(command)

def open_by_url_type(url):
    if url.startswith("file://"):
        filepath = url[7:].replace("%20", " ")
        if filepath.endswith("/"):
            open_directory(filepath)
        else:
            open_file(filepath)

    if url.startswith("http"):
        print("SublimeLinker plugin opening web url " + url)
        webbrowser.open(url, autoraise=True) # for launching a specific browser see - https://docs.python.org/3.5/library/webbrowser.html


class OpenUrlCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # find all urls
        urls = self.view.find_all(UrlOpener.FILE_OR_DIR_URL) + self.view.find_all(UrlOpener.WEB_URL)

        selection = self.view.sel()[0]
        if selection.empty():
            selection = next((url for url in urls if url.contains(selection)), None)
            if not selection:
                return
        url = self.view.substr(selection) 

        open_by_url_type(url)


class OpenAllUrlsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        ranges = self.view.find_all(UrlOpener.FILE_OR_DIR_URL) + self.view.find_all(UrlOpener.WEB_URL)
        for range in ranges:
            url = self.view.substr(range)
            open_by_url_type(url)
