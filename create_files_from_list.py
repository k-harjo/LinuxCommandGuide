import pandas as pd

file = "linux_commands.csv"
all_linux_cmds = pd.read_csv(file)

for item in all_linux_cmds["Command"]:
    with open(format(f"{item}.txt"), 'w') as f:
        f.write("EMPTY")