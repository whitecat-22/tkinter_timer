import tkinter as tk
import tkinter.ttk as ttk

num = 0

root = tk.Tk()
root.title("プログレスバー")


#プログレスバーの初期設定
progressbar = ttk.Progressbar(
    root, orient="horizontal", length=300, mode="determinate")
progressbar.pack()
maximum_bar = 10
value_bar = 0
div_bar = 1
progressbar.configure(maximum=maximum_bar, value=value_bar)


#プログレスバーの更新
def var_start(value_bar):
    progressbar.configure(value=value_bar)


#ボタンを押したら1秒ずつカウント、maximumに達したら終了しましたを表示
def Click():
    global value_bar, div_bar, text_label, num
    for i in range(maximum_bar):
        value_bar += div_bar
        text_label.set(str(value_bar))

#        print("num = " + str(num))
#        num += 1

        if value_bar == maximum_bar:
            progressbar.after(1000, var_start(value_bar))
#            print("num = " + str(num))
            text_label.set("終了しました")
            root.destroy()

        else:
            progressbar.after(1000, var_start(value_bar))
            progressbar.update()


#ボタンとテキストラベルの作成
button = tk.Button(text=u"START", command=Click)
button.pack()
text_label = tk.StringVar()
text_label.set("0")
label = tk.Label(textvariable=text_label)
label.pack()

root.mainloop()
