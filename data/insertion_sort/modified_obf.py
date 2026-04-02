def a(iyporemten):
    for jsiodjaoid in range(1, len(iyporemten)):
        mnbasidgasidg = iyporemten[jsiodjaoid]
        vbdsavdrte = jsiodjaoid - 1

        while vbdsavdrte >= 0 and iyporemten[vbdsavdrte] > mnbasidgasidg:
            iyporemten[vbdsavdrte + 1] = iyporemten[vbdsavdrte]
            vbdsavdrte -= 1

        iyporemten[vbdsavdrte + 1] = mnbasidgasidg

    return iyporemten