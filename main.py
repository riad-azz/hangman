import webview
from backend import app

if __name__ == '__main__':
    webview.create_window('Hangman', app, resizable=False, width=800, height=600)
    webview.start()
