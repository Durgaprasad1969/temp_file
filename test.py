from pathlib import Path
for f in Path().cwd().glob("../*.v"):
    print(f)
