# エラーを出力するプログラム
try:
    import requests
except Exception as e:
    print(e.__class__.__name__) 
    print(e.args) 
    print(e) 
    print(f"{e.__class__.__name__}: {e}") 

ln -nfs /usr/bin/idle3 /usr/bin/idle
ln -nfs /usr/bin/pydoc3 /usr/bin/pydoc
ln -nfs /usr/bin/python3 /usr/bin/python
ln -nfs /usr/bin/python3-config /usr/bin/python-config
ln -nfs /usr/bin/pip3 /usr/bin/pip