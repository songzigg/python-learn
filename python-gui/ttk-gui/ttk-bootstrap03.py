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

    # 添加表头，包括“行号”、“编辑”和“操作”列
    columns = ['行号'] + list(df.columns) + ['编辑', '操作']
    tree["columns"] = columns
    tree["show"] = "headings"

    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center')

    # 添加数据行和“行号”、“编辑”列
    for idx, row in df.iterrows():
        # 行号从 1 开始
        row_number = idx + 1
        values = [row_number] + list(row) + ["编辑", f"操作 {row_number}"]
        tree.insert("", tk.END, values=values, iid=str(idx))

    # 绑定事件
    tree.bind("<ButtonRelease-1>", on_click)

def on_click(event):
    item = tree.identify_row(event.y)
    column = tree.identify_column(event.x)

    if column == f"#{len(tree['columns'])-2}":  # 编辑列
        show_edit_popup(item)
    elif column == f"#{len(tree['columns'])-1}":  # 操作列
        show_popup(item)

def show_edit_popup(item):
    item_values = tree.item(item, 'values')
    row_number = item_values[0]

    edit_popup = tk.Toplevel()
    edit_popup.title("编辑数据")
    edit_popup.geometry("400x300")

    def save_edit():
        new_values = [row_number]
        for entry in entries:
            new_values.append(entry.get())
        new_values.append(item_values[-2])  # 保留原操作列内容
        tree.item(item, values=new_values)
        edit_popup.destroy()

    ttk.Label(edit_popup, text="编辑数据：").pack(pady=10)
    entries = []
    for col, value in zip(tree["columns"][1:-2], item_values[1:-2]):
        ttk.Label(edit_popup, text=col).pack(pady=5)
        entry = ttk.Entry(edit_popup)
        entry.insert(0, value)
        entry.pack(pady=5, fill=tk.X, padx=10)
        entries.append(entry)

    save_button = ttk.Button(edit_popup, text="保存", command=save_edit)
    save_button.pack(pady=10)

def show_popup(item):
    popup = tk.Toplevel()
    popup.title("交互命令输入")
    popup.geometry("400x300")

    command_label = ttk.Label(popup, text="命令输入区：")
    command_label.pack(pady=10)

    command_entry = ttk.Entry(popup)
    command_entry.pack(pady=10, fill=tk.X, padx=10)

    output_label = ttk.Label(popup, text="输出：")
    output_label.pack(pady=10)

    output_text = tk.Text(popup, height=10, state="normal")
    output_text.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)

    def submit_command():
        command = command_entry.get()
        response = f"Executing command: {command}"  # 模拟命令执行
        output_text.insert(tk.END, response + "\n")
        # 可以在这里添加实际的命令执行逻辑
        output_text.insert(tk.END, "Command executed\n")

    submit_button = ttk.Button(popup, text="提交", command=submit_command)
    submit_button.pack(pady=10)

def log_action(action):
    console.insert(tk.END, action + "\n")
    console.see(tk.END)

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

# 创建控制台输出区域
console_label = ttk.Label(app, text="控制台输出：")
console_label.pack(pady=10)

console_frame = ttk.Frame(app)
console_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

console = tk.Text(console_frame, height=8, state="normal")
console.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

console_scroll = ttk.Scrollbar(console_frame, orient="vertical", command=console.yview)
console_scroll.pack(side=tk.RIGHT, fill=tk.Y)
console.configure(yscrollcommand=console_scroll.set)

# 运行主循环
app.mainloop()
