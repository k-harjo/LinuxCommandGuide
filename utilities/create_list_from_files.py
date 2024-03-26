import pandas as pd

file = "linux_commands.csv"
all_linux_cmds = pd.read_csv(file)
item_list = []
for item in all_linux_cmds["Command"]:
    txt_name = format(f"html/{item}.html")
    item_list.append(txt_name)
all_linux_cmds["Html_Path"] = item_list
all_linux_cmds.to_csv("linux_commands.csv", index=False)