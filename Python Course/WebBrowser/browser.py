import webbrowser

# webbrowser.open("https://www.python.org", new=1)
chrome = webbrowser.get('chrome %s').open_new_tab("https://www.python.org")