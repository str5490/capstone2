from tkinter import *
from tkinter import ttk
import tkinter.messagebox

bg_color = 'beige'
root = Tk()
root.title("PAD")
root.configure(background = bg_color)
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda e: root.destroy())

window_wth, window_hgh = root.winfo_screenwidth(), root.winfo_screenheight()
large_font = ('Verdana', int(window_hgh / 12))
button_hgh = int(window_hgh / 8)
button_wth = int(window_wth / 3.5)
pady = (window_hgh - int(button_hgh * 7)) / 10
padx = (window_wth - int(button_wth * 3)) / 7

def button_pressed(value):
    if value == 'AC':
        number_entry.delete(0, 'end')
        print("취소")
    elif value == 'IN': import_num()
    elif value == 'OUT': export_num()
    else:
        number_entry.insert("end", value)
        print(value, "pressed")

def import_num():
    str_num = number_entry.get()
    if not (str_num == ''):
        result = tkinter.messagebox.askquestion(str_num, "입고하시겠습니까?")
        if result == 'no':
            print("입고취소")
        else :
            print(str_num, "입고완료")
            textfile = open("./numbers", "a")
            textfile.write('%s\n' %(str_num))
        number_entry.delete(0, 'end')
        
def export_num():
    delete_flag = False
    str_num = number_entry.get()
    if not (str_num == ''):
        result = tkinter.messagebox.askquestion(str_num, "출고하시겠습니까?")
        if result == 'no':
            print("출고취소")  
        else :
            with open("./numbers", 'r') as infile:
                data = infile.readlines()
            with open("./numbers", 'w') as outfile:
                for i in data:
                    if not (i[0:-1] == str_num):
                        outfile.write(i)
                    else : delete_flag = True
                if delete_flag == False :
                    tkinter.messagebox.showinfo("Error", "해당 번호의 차량이 입고되지 않았습니다.")
                else : print(str_num, "출고완료")
        number_entry.delete(0, 'end')

entry_value = StringVar(root, value = '')
number_entry = ttk.Entry(root, textvariable = entry_value, width = 10, font = large_font)
number_entry.grid(row = 0, columnspan = 3, pady = pady)

pixelVirtual = tkinter.PhotoImage(width = 1, height = 1)
def button_def(text, row, col, out):
    button = tkinter.Button(root, height = button_hgh, width = button_wth, text = text, 
                            image = pixelVirtual, bg = bg_color, compound = "c", font = large_font,
                            command = lambda:button_pressed(out))
    button.grid(row = row, column = col, padx = padx, pady = pady)

button_def('7', 1, 0, '7')
button_def('8', 1, 1, '8')
button_def('9', 1, 2, '9')

button_def('4', 2, 0, '4')
button_def('5', 2, 1, '5')
button_def('6', 2, 2, '6')

button_def('1', 3, 0, '1')
button_def('2', 3, 1, '2')
button_def('3', 3, 2, '3')

button_def('0', 4, 1, '0')

button_def('정정', 5, 0, 'AC')
button_def('입고', 5, 1, 'IN')
button_def('출고', 5, 2, 'OUT')

root.mainloop()