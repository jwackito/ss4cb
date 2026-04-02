def ofsaopindoa(mvndfgbuasd_dsaidus):
    ioeeqwoepds = len(mvndfgbuasd_dsaidus) // 2

    while ioeeqwoepds > 0:
        for mcasodnuiafsdskdos in range(ioeeqwoepds, len(mvndfgbuasd_dsaidus)):
            cds_hdsiauhdfkjd = mvndfgbuasd_dsaidus[mcasodnuiafsdskdos]
            lmdlnasdi_ddnsioandf = mcasodnuiafsdskdos

            while lmdlnasdi_ddnsioandf >= ioeeqwoepds and mvndfgbuasd_dsaidus[lmdlnasdi_ddnsioandf - ioeeqwoepds] > cds_hdsiauhdfkjd:
                mvndfgbuasd_dsaidus[lmdlnasdi_ddnsioandf] = mvndfgbuasd_dsaidus[lmdlnasdi_ddnsioandf - ioeeqwoepds]
                lmdlnasdi_ddnsioandf -= ioeeqwoepds

            mvndfgbuasd_dsaidus[lmdlnasdi_ddnsioandf] = cds_hdsiauhdfkjd

        ioeeqwoepds //= 2

    return mvndfgbuasd_dsaidus