from controller import *

def main():
    window = Tk()
    window.title('Hangman')
    window.geometry('800x600')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()

if __name__ == '__main__':
    main()
