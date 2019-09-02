import os
env =  {"PATH":".", "XYZ":"BlaBla"}
args = ("test","abc")
os.execvpe("test.sh", args, env)