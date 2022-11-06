# cd to your model local repository
import os as os
os.getcwd()

def model_hash(filename):
    try:
        with open(filename, "rb") as file:
            import hashlib as hashlib
            m = hashlib.sha256()
            file.seek(0x100000)
            m.update(file.read(0x10000))
            return m.hexdigest()[0:8]
    except FileNotFoundError:
        return 'NOFILE'

model_hash('model.ckpt')
