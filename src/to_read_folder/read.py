from pathlib import Path

print("Dir ->")
p = Path(input())
file = Path("meu_arquivo.txt")
def read_arquiv():
    create_file(file)
    for path in p.iterdir():
        add_text(path.name)

def create_file(file):
    file.write_text("", encoding="utf-8")

def add_text(args):
  f = file.open('a', encoding="utf-8")
  f.write(f"{args}\n")
