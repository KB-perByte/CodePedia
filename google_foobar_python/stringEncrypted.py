preArr = []
for i in range(ord('a'), ord('z')+1):
    preArr.append(i)

def computeEnc(_str):
    _s = ''
    for i, ch in enumerate(_str):
        if ord(ch) in preArr:
            _s.join(chr(preArr[-1] - ord(ch) + preArr[0]))
    return _s

mystring = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
print(computeEnc(mystring))