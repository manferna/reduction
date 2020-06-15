import pylab as pl
import numpy as np
import json
from pathlib import Path
from astropy import units as u


# copy-pasted from parse_contdotdat
def parse_contdotdat(filepath):

    selections = []

    with open(filepath, 'r') as fh:
        for line in fh:
            if "LSRK" in line:
                selections.append(line.split()[0])


    return ";".join(selections)

lines_to_overplot = {
    "n2hp": "93.173700GHz",
    "sio": "217.104984GHz",
    "h2co303": "218.222195GHz",
    "12co": "230.538GHz",
    "h30a": "231.900928GHz",
    "h41a": "92.034434GHz",
    "c18o": "219.560358GHz",
    #"ch3ccn": "92.26144GHz",
    #"ch3cch": "102.547983GHz",
}

frequency_coverage = {
    'B3': {
           1: (93.0931359128077, 93.21807487765145, 2048),
           0: (91.6824842830137, 92.6819960017637, 2048),
           2: (102.08163478365731, 103.08114650240731, 2048),
           3: (104.48007228365731, 105.47958400240731, 2048),
          },
    'B6': {
        0: (216.058164552243, 216.2924174819305, 1920),
        1: (217.008115724118, 217.242246583493, 960),
        2: (218.08794227907555, 218.32219520876305, 1920),
        3: (219.47637001345055, 219.59343544313805, 960),
        4: (219.86137977907555, 219.97832313845055, 480),
        5: (230.26977356280713, 230.73754700030713, 480),
        6: (231.01931579913526, 231.48782165851026, 1920),
        7: (231.48238541765087, 233.35640885515087, 1920),
    }
}

basepath = Path('/orange/adamginsburg/ALMA_IMF/2017.1.01355.L')
with open(basepath / 'contdatfiles.json', 'r') as fh:
    contdatfiles = json.load(fh)

fields = sorted("G008.67 G337.92 W43-MM3 G328.25 G351.77 G012.80 G327.29 W43-MM1 G010.62 W51-IRS2 W43-MM2 G333.60 G338.93 W51-E G353.41".split())
nfields = len(fields)
fields_and_numbers = list(enumerate(fields))

included_bw = {}

for fignum,band in enumerate((3,6)):
    pl.close(fignum)
    pl.figure(fignum, figsize=(12,6))


    frqmasks = {}

    fcov = frequency_coverage[f'B{band}']

    nspw = len(fcov)

    included_bw[band] = {}

    for spwn,(spw,(minfrq, maxfrq, nfrqs)) in enumerate(fcov.items()):
        frqmask = np.zeros([nfields, nfrqs], dtype='bool')

        included_bw[band][spw] = {}

        for fieldnum,field in fields_and_numbers:
            frqarr = np.linspace(minfrq, maxfrq, nfrqs)*u.GHz
            dnu = (maxfrq-minfrq)/nfrqs

            if f'{field}B{band}' not in contdatfiles:
                print(f"Skipping field {field} band {band} for lack of contdotdat.")
                continue

            contdat = parse_contdotdat(contdatfiles[f'{field}B{band}'])

            for frqline in contdat.split(";"):
                fsplit = frqline.split("~")
                f2 = u.Quantity(fsplit[1])
                f1 = u.Quantity(float(fsplit[0]), f2.unit)

                assert f1 < f2

                sel = (frqarr > f1) & (frqarr < f2)
                frqmask[fieldnum, sel] = True

            frqmasks[spw] = frqmask

            included_bw[band][spw][field] = (~frqmask[fieldnum,:]).sum() * dnu


        assert frqmask.sum() > 0

        if band == 6:
            # W41-MM1 B6 doesn't exist
            assert not np.any(frqmask[10,:])

        ax = pl.subplot(1, nspw, spwn+1)
        #print(ax,spwn)
        yticklocs = (np.arange(nfields) + np.arange(1, nfields+1))/2.
        tick_maps = list(zip(yticklocs, fields))
        #print(tick_maps)
        if spwn == 0:
            ax.set_yticks(yticklocs)
            ax.set_yticklabels(fields)
        else:
            ax.set_yticks([])

        ax.set_xticks([minfrq, (minfrq+maxfrq)/2, maxfrq])
        ax.set_xticklabels([f"{frq:0.2f}" for frq in ax.get_xticks()])
        if spwn % 2 == 1:
            ax.xaxis.set_ticks_position('top')

        ax.imshow(frqmask, extent=[minfrq, maxfrq, nfields, 0],
                  interpolation='none', cmap='gray')
        ax.set_aspect((maxfrq-minfrq)*2 / (nfields))

        for linename,linefrq in lines_to_overplot.items():
            linefrq = u.Quantity(linefrq).to(u.GHz).value
            if (minfrq < linefrq) & (maxfrq > linefrq):
                ax.vlines(linefrq, 0, nfields, color='r')


    pl.tight_layout()
    pl.subplots_adjust(wspace=0.05, hspace=0)

    pl.savefig(f"continuum_selection_regions_band{band}.png", bbox_inches='tight')
    pl.savefig(f"continuum_selection_regions_band{band}.pdf", bbox_inches='tight')

print({k:v.sum(axis=1)/v.shape[1] for k,v in frqmasks.items()})
print(included_bw)

included_bw_byband = {band: {field: sum(x[field] for x in included_bw[band].values())
                             for field in fields if field in included_bw[band][0]}
                      for band in (3,6)}
print(included_bw_byband)
total_bw = {band: sum(entry[1]-entry[0] for entry in flist.values()) for band,flist in frequency_coverage.items()}

bandfrac = {band: {field: included_bw_byband[band][field]/total_bw[f"B{band}"] for field in included_bw_byband[band]} for band in (3,6)}