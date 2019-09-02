import os

path = os.environ["PATH"] + ":." 
env =  {"PATH":path, "XYZ":"BlaBla"}
os.execlpe("test.sh", "test","abc", env)