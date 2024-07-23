import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if file_path:
        display_excel(file_path)


def display_excel(file_path):
    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 清空Treeview
    for item in tree.get_children():
        tree.delete(item)

    # 添加表头
    tree["columns"] = list(df.columns) + ["操作"]
    tree["show"] = "headings"
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center')

    # 添加数据行和操作列
    for _, row in df.iterrows():
        values = list(row) + ["操作"]
        tree.insert("", tk.END, values=values)

    # 绑定事件
    tree.bind("<ButtonRelease-1>", on_click)


def on_click(event):
    item = tree.identify_row(event.y)
    column = tree.identify_column(event.x)

    if column == f"#{len(tree['columns'])}":  # 操作列
        show_popup(item)


def show_popup(item):
    popup = tk.Toplevel()
    popup.title("交互命令输入")
    popup.geometry("300x200")

    label = ttk.Label(popup, text="请输入命令：")
    label.pack(pady=10)

    entry = ttk.Entry(popup)
    entry.pack(pady=10)

    def submit_command():
        command = entry.get()
        messagebox.showinfo("命令输入", f"你输入的命令是: {command}")
        popup.destroy()

    submit_button = ttk.Button(popup, text="提交", command=submit_command)
    submit_button.pack(pady=10)


# 创建主窗口
app = tk.Tk()
app.title("Excel文件导入示例")
app.geometry("800x600")

# 创建导入文件按钮
import_button = ttk.Button(app, text="导入Excel文件", command=open_file)
import_button.pack(pady=20)

# 创建Treeview以展示Excel数据，并添加滚动条
frame = ttk.Frame(app)
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# 设置Treeview样式，显示行和列的网格线
style = ttk.Style()
style.configure("Treeview", rowheight=25, borderwidth=1, relief="solid")
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
style.map("Treeview", background=[("selected", "blue")])

tree = ttk.Treeview(frame, style="Treeview")
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 添加水平滚动条
h_scroll = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
tree.configure(xscrollcommand=h_scroll.set)

# 添加垂直滚动条
v_scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
tree.configure(yscrollcommand=v_scroll.set)

# 运行主循环
app.mainloop()
