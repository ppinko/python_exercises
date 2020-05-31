"""
https://edabit.com/challenge/Rww5GiNRH3b2BRC83
"""


from collections import OrderedDict


def data_regex_lovely(html: str):
    d = OrderedDict()
    L = html.split('&')
    for i in L:
        if 'desc=' in i:
            d['desc'] = i[5:]
        elif 'val=' in i:
            d['val'] = i[4:]
        elif 'time=' in i:
            d['time'] = i[5:]
        elif 'id=' in i:
            d['id'] = int(i[3:])
    reg_d = dict(d)
    return reg_d


assert data_regex_lovely("desc=dzgr&val=xyz54&time=01:41&id=1") == {'desc':"dzgr",'val':"xyz54",'time':"01:41",'id':1}
assert data_regex_lovely("time=01:41&id=1&desc=dzgr&val=12345") == {'desc':"dzgr",'val':"12345",'time':"01:41",'id':1}
assert data_regex_lovely("time=11:41&id=10&desc=dzgraa&val=54") == {'desc':"dzgraa",'val':"54",'time':"11:41",'id':10}

print('Success')