from tkinter import *
from Human import Human


if __name__ == '__main__':
  win = Tk()
  win.title('Test App')
  win.geometry("700x350")

  human = Human('Meier', 45, 184)
  human_name = Text(win, height=2, width=60)
  human_name.pack()
  human_name.insert(END, f'{human}')

  win.mainloop()

