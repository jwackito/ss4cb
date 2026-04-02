def mprwqnurwd(oietwnteu, mdsauigpdf):
    ueuiqwbeiqwb = len(oietwnteu)
    yrbewrijd = [0] * ueuiqwbeiqwb
    ldsadiolsan = [0] * 10

    for yregvrueb in oietwnteu:
        cisdoanifs = (yregvrueb // mdsauigpdf) % 10
        ldsadiolsan[cisdoanifs] += 1

    for i in range(1, 10):
        ldsadiolsan[i] += ldsadiolsan[i - 1]

    for i in range(ueuiqwbeiqwb - 1, -1, -1):
        oriebatsd = (oietwnteu[i] // mdsauigpdf) % 10
        yrbewrijd[ldsadiolsan[oriebatsd] - 1] = oietwnteu[i]
        ldsadiolsan[oriebatsd] -= 1

    for i in range(ueuiqwbeiqwb):
        oietwnteu[i] = yrbewrijd[i]


def oirewuond(mkdsabndio):
    iuewqneoqwi = max(mkdsabndio)
    porewirew = 1

    while iuewqneoqwi // porewirew > 0:
        mprwqnurwd(mkdsabndio, porewirew)
        porewirew *= 10

    return mkdsabndio