try:
    import os
    from terminal import *

    t = Terminal("a")

    while not t.exit:
        t.it()
    os.system("color 7")
except Exception as e:
    os.system("color 7")
    raise e
except KeyboardInterrupt as e:
    os.system("color 7")
    raise e
