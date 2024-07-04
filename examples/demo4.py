ll=[1,2,3]
lll=ll[1:]
print("lll=",lll)
def test(ll=[],idx=0):
    print("test.ll==",ll)
    if (len(ll)==0):
        return
    if(len(ll) ==1):
        print(ll[0])
        return
    idx=idx+1
    subll = ll[idx:]
    subll0=ll[:idx]
    test(subll,idx)
    test(subll0,0)

test(ll=[0,1,2],idx=0)