import hid

for d in hid.enumerate(0xfe01, 0):
    keys = list(d.keys())
    keys.sort()
    for key in keys:
        print ("%s : %s" % (key, d[key]))
    print ("")
