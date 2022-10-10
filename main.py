import pyperclip as pc
from alive_progress import alive_bar

IP = input("Ip Address: ")
FirstPort = input("Start Port: ")
SecondPort = input("Finish Port: ")
Port = int(FirstPort)
Diff = int(SecondPort)-Port
pc.copy(str(IP)+":"+str(Port))
with alive_bar(Diff, ctrl_c=False, title=f'List is Copying Please Wait') as bar:
        for i in range(Diff):
            Port+=1
            pc.copy(pc.paste()+"\n"+str(IP)+":"+str(Port))
            bar()
