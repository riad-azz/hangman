import webview
from backend import app


def show_confirmation_dialog(message):
    return webview.windows.confirm("Confirm", message)


if __name__ == '__main__':
    webview.create_window('Hangman', app, resizable=False)
    webview.start()
