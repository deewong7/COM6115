# import helloworld
# print(helloworld.key)

# from helloworld import key
# print(key)

import sys # works perfectly
sys.path.append("../../")


# import os # will not work
# PYTHONPATH = os.environ["PYTHONPATH "]
# PYTHONPATH = "../../"
# os.environ["PYTHONPATH"] = "../../"

# print(PYTHONPATH)
# print(os.environ["PYTHONPATH"])


import lib.key_modules as km

km.key_func()
