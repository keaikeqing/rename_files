import os
import sys
import tkinter as tk


def re_fileName(path, old, new, idx):
    fileList = os.listdir(path)
    for file in fileList:
        if '.' in file:
            used_fileName, extension = os.path.splitext(file)
            new_name = used_fileName.replace(old, new, idx)
            new_file = new_name + extension
            os.rename(path + file, path + new_file)


def rename_files():
    path = path_entry.get()
    if path != str(''):
        if not os.path.exists(path):
            result_label.config(text="文件夹路径不存在，请检查！", fg="red", font=("微软雅黑", 10))
            result_label.after(5000, lambda: result_label.config(text=""))
        else:
            path = path + '\\'
            old_name = oldname_entry.get()
            new_name = newname_entry.get()
            idx = int(idx_entry.get())

            re_fileName(path, old_name, new_name, idx)

            result_label.config(text="文件重命名完成！", fg="green", font=("微软雅黑", 10))
            result_label.after(5000, lambda: result_label.config(text=""))
    else:
        result_label.config(text="未输入路径，请检查！", fg="red", font=("微软雅黑", 10))
        result_label.after(5000, lambda: result_label.config(text=""))


if __name__ == '__main__':
    root = tk.Tk()
    root.title("批量替换")
    root.option_add("*Font", "微软雅黑 10")
    # 获取当前可执行文件的目录
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(__file__)
    # 图标的路径现在是相对于当前可执行文件的目录
    icon_path = os.path.join(application_path, 'rename.ico')
    # 在 Tkinter 窗口中设置图标
    root.iconbitmap(icon_path)
    root.geometry("250x180")

    path_label = tk.Label(root, text="路径:", font=("微软雅黑", 10))
    path_label.grid(row=0, column=0)

    path_entry = tk.Entry(root, font=("微软雅黑", 10))
    path_entry.insert(0, str(''))  # 插入默认值
    path_entry.grid(row=0, column=1)

    oldname_label = tk.Label(root, text="旧字符:", font=("微软雅黑", 10))
    oldname_label.grid(row=1, column=0)

    oldname_entry = tk.Entry(root, font=("微软雅黑", 10))
    oldname_entry.insert(0, str(''))  # 插入默认值
    oldname_entry.grid(row=1, column=1)

    newname_label = tk.Label(root, text="新字符:", font=("微软雅黑", 10))
    newname_label.grid(row=2, column=0)

    newname_entry = tk.Entry(root, font=("微软雅黑", 10))
    newname_entry.insert(0, str(''))  # 插入默认值
    newname_entry.grid(row=2, column=1)

    idx_label = tk.Label(root, text="需替换个数:", font=("微软雅黑", 10))
    idx_label.grid(row=3, column=0)

    idx_entry = tk.Entry(root, font=("微软雅黑", 10))
    idx_entry.insert(0, str(1))  # 插入默认值
    idx_entry.grid(row=3, column=1)

    rename_button = tk.Button(root, text="重命名", command=rename_files, font=("微软雅黑", 10))
    rename_button.grid(row=4, column=1, padx=0, pady=10)

    result_label = tk.Label(root, text="")
    result_label.grid(row=5, column=0, columnspan=2)

    root.mainloop()
