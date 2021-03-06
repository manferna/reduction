"""
Imaging parameters for all continuum imaging work.

The first variable is used by ``continuum_imaging.py``.  It specifies the
parameters to be used for the first-pass imaging before any self-calibration is
done.  Please add your source name to the 'field' section.
DO NOT modify the default imaging parameters; if there are any that are
unsuitable for your target field, add them to the
``imaging_parameters_nondefault`` keyword, following the naming scheme laid out
there.

If you want to specify a different set of imaging parameters, you can do so by
passing a dictionary instead of a single number.  For example, instead of
    threshold: '1mJy'
you can use
    threshold: {0: '2mJy', 1:'1mJy', 2:'0.75mJy'}
The requirements are:
    (1) you must have a zero entry (which is used by continuum_imaging.py)
    (2) you must have the same number of entries in each dictionary as there
    are in the calibration parameters list below

The self-calibration parameters are specified in ``selfcal_pars``.  The default is to
do 4 iterations of phase-only self calibration.  If you would like to add additional
steps, you can add them by adding new entries to the self-calibration parameter
dictionary for your source following the template laid out below.


You can copy any set of parameters and add `_bsens` to the end of the name to
have it use special parameters only for the bsens imaging.  For example:
    'G010.62_B3_12M_robust0': {...},
    'G010.62_B3_12M_robust0_bsens: {...},'
would be the parameters used for non-bsens and for bsens data, respectively.
If you have ONLY a non-bsens parameter key (you do not have a _bsens set
of parameters), the bsens selfcal & imaging will use the same as the non-bsens.

CONTRIBUTOR NOTE:
    This file is to be formatted with python's "black" formatter:

        black -t py27 -l 120 imaging_parameters.py
"""
import copy

allfields = "G008.67 G337.92 W43-MM3 G328.25 G351.77 G012.80 G327.29 W43-MM1 G010.62 W51-IRS2 W43-MM2 G333.60 G338.93 W51-E G353.41".split()

# set up global defaults
imaging_parameters = {
    "{0}_{1}_{2}_robust{3}".format(field, band, array, robust): {
        "threshold": "1mJy",  # RMS ~0.5-0.6 mJy
        "pblimit": 0.1,
        "niter": 100000,
        "robust": robust,
        "weighting": "briggs",
        "scales": [0, 3, 9],
        "gridder": "mosaic",
        "specmode": "mfs",
        "deconvolver": "mtmfs",
        "usemask": "user",
        "nterms": 2,
    }
    for field in allfields
    for band in ("B3", "B6")
    for array in ("12M", "7M12M", "7M")
    for robust in (-2, 0, 2)
}

# added for 7M only data: higher threshold
for key in imaging_parameters:
    if "_7M_" in key:
        imaging_parameters[key]["threshold"] = "5mJy"
    if "7M" in key:
        imaging_parameters[key]["scales"] = [0, 3, 9, 27]


imaging_parameters_nondefault = {
    "G008.67_B6_12M_robust0": {
        "threshold": {0: "6.5mJy", 1: "5.5mJy", 2: "4.5mJy", 3: "3.5mJy", 4: "2.9mJy", 5: "0.75mJy",},
        "niter": {0: 1500, 1: 1500, 2: 3000, 3: 5000, 4: 50000, 5: 50000},
        "maskname": {
            0: "mask_G008_B6_0.crtf",
            1: "mask_G008_B6_0.crtf",
            2: "mask_G008_B6_1.crtf",
            3: "mask_G008_B6_4.crtf",
            4: "mask_G008_B6_4.crtf",
            "final": "mask_G008_B6_4_final.crtf",
        },
    },
    "G008.67_B6_12M_robust0_bsens": {
        "threshold": {0: "7.5mJy", 1: "6.5mJy", 2: "5.5mJy", 3: "4.5mJy", 4: "3.25mJy", 5: "0.5mJy",},
        "niter": {0: 1500, 1: 1500, 2: 3000, 3: 5000, 4: 50000, 5: 50000},
        "maskname": {
            0: "mask_G008_B6_0.crtf",
            1: "mask_G008_B6_0.crtf",
            2: "mask_G008_B6_1.crtf",
            3: "mask_G008_B6_1.crtf",
            4: "mask_G008_B6_4.crtf",
            "final": "mask_G008_B6_4_final.crtf",
        },
    },
    "G008.67_B6_7M12M_robust0": {
        "threshold": {0: "6.0mJy", 1: "5.0mJy", 2: "4.0mJy", 3: "3.5mJy", 4: "2.9mJy", 5: "0.75mJy",},
        "niter": {0: 1500, 1: 1500, 2: 3000, 3: 5000, 4: 50000, 5: 50000},
        "maskname": {
            0: "mask_G008_B6_0.crtf",
            1: "mask_G008_B6_0.crtf",
            2: "mask_G008_B6_1.crtf",
            3: "mask_G008_B6_4.crtf",
            4: "mask_G008_B6_4_final.crtf",
            "final": "mask_G008_B6_4_final.crtf",
        },
    },
    "G008.67_B3_12M_robust0": {
        "threshold": {0: "2.5mJy", 1: "2.0mJy", 2: "1.5mJy", 3: "1.0mJy", 4: "0.7mJy", 5: "0.3mJy",},
        "niter": {0: 700, 1: 700, 2: 2000, 3: 5000, 4: 50000, 5: 50000},
        "maskname": {
            0: "mask_G008_B3_1.crtf",
            1: "mask_G008_B3_2.crtf",
            2: "mask_G008_B3_3.crtf",
            3: "mask_G008_B3_3.crtf",
            4: "mask_G008_B3_3.crtf",
            "final": "mask_G008_B3_4.crtf",
        },
    },
    "G008.67_B3_7M12M_robust0": {
        "threshold": {0: "5.0mJy", 1: "4.5mJy", 2: "4.0mJy", 3: "4.5mJy", 4: "2.5mJy", 5: "0.4mJy",},
        "niter": {0: 1000, 1: 1000, 2: 2000, 3: 5000, 4: 25000, 5: 50000},
        "maskname": {
            0: "mask_G008_B3_7M12M_0.crtf",
            1: "mask_G008_B3_7M12M_1.crtf",
            2: "mask_G008_B3_7M12M_2.crtf",
            3: "mask_G008_B3_7M12M_3.crtf",
            4: "mask_G008_B3_7M12M_4.crtf",
            "final": "mask_G008_B3_7M12M_4.crtf",
        },
    },
    "G008.67_B3_12M_robust0_bsens": {
        "threshold": {0: "3.0mJy", 1: "2.5mJy", 2: "1.5mJy", 3: "0.8mJy", 4: "0.3mJy", 5: "0.16mJy",},
        "niter": {0: 1200, 1: 1500, 2: 3000, 3: 5000, 4: 70000, 5: 90000},
        "maskname": {
            0: "mask_G008_B3_1.crtf",
            1: "mask_G008_B3_2.crtf",
            2: "mask_G008_B3_2.crtf",
            3: "mask_G008_B3_2_bsens.crtf",
            4: "mask_G008_B3_2_bsens.crtf",
            5: "mask_G008_B3_final_bsens.crtf",
            "final": "mask_G008_B3_final_bsens.crtf",
        },
    },
    "G010.62_B3_7M12M_robust0": {
        "threshold": {0: "10mJy", 1: "5mJy", 2: "2.5 mJy", 3: "0.8mJy", 4: "0.5mJy", 5: "0.32mJy",},
        "niter": {0: 700, 1: 1300, 2: 2500, 3: 5000, 4: 15000, 5: 15000},
        "maskname": {
            0: "G010.62_55arcsecCircle.crtf",
            1: "G010_ds9_15mJy.crtf",
            2: "G010_ds9_15mJy.crtf",
            3: "G010_ds9_1mJy.crtf",
            4: "G010_ds9_0.5mJy.crtf",
            5: "G010_ds9_0.3mJy.crtf",
        },
    },
    "G333.60_B3_12M_robust0": {
        "threshold": {0: "0.8mJy", 1: "0.8mJy", 2: "0.4mJy", 3: "0.2mJy", 4: "0.1mJy", 5: "0.07mJy",},
        "niter": {0: 3000, 1: 3000, 2: 10000, 3: 30000, 4: 90000, 5: 90000},
        "maskname": {
            0: "mask_G333_B3_12m_0.1.crtf",
            1: "mask_G333_B3_12m_0.1.crtf",
            2: "mask_G333_B3_12m_0.03.crtf",
            3: "mask_G333_B3_12m_0.01.crtf",
            4: "mask_G333_B3_12m_0.003.crtf",
            5: "mask_G333_B3_12m_0.0015.crtf",
        },
        "scales": [0, 3, 9, 27],
    },
    "G333.60_B3_12M_robust2": {
        "threshold": "0.07mJy",
        "niter": 90000,
        "scales": [0, 3, 9],
        "maskname": "mask_G333_B3_12m_0.0015.crtf",
    },
    "G333.60_B3_12M_robust-2": {
        "threshold": "0.07mJy",
        "niter": 90000,
        "scales": [0, 3, 9, 27],
        "maskname": "mask_G333_B3_12m_0.0015.crtf",
    },
    "G333.60_B3_7M12M_robust0": {
        "threshold": {0: "0.8mJy", 1: "0.8mJy", 2: "0.4mJy", 3: "0.2mJy", 4: "0.1mJy", 5: "0.07mJy",},
        "niter": {0: 3000, 1: 3000, 2: 10000, 3: 30000, 4: 90000, 5: 90000},
        "maskname": {
            0: "mask_G333_B3_7m12m_0.1.crtf",
            1: "mask_G333_B3_7m12m_0.1.crtf",
            2: "mask_G333_B3_7m12m_0.05.crtf",
            3: "mask_G333_B3_7m12m_0.01.crtf",
            4: "mask_G333_B3_7m12m_0.002.crtf",
            5: "mask_G333_B3_7m12m_0.0015.crtf",
        },
        "scales": [0, 3, 9, 27],
    },
    "G333.60_B3_7M12M_robust2": {
        "threshold": "0.07mJy",
        "niter": 90000,
        "scales": [0, 3, 9],
        "maskname": "mask_G333_B3_7m12m_0.0015.crtf",
    },
    "G333.60_B3_7M12M_robust-2": {
        "threshold": "0.07mJy",
        "niter": 90000,
        "scales": [0, 3, 9, 27],
        "maskname": "mask_G333_B3_7m12m_0.0015.crtf",
    },
    "G333.60_B6_12M_robust0": {
        "threshold": {
            0: "1.2mJy",
            1: "1.2mJy",
            2: "0.8mJy",
            3: "0.4mJy",
            4: "0.2mJy",
            5: "0.15 mJy",
            "final": "0.15 mJy",
        },
        "niter": {0: 3000, 1: 3000, 2: 6000, 3: 12000, 4: 24000, 5: 48000, "final": 70000,},
        "maskname": {
            0: "mask_G333_B6_12m_0.1.crtf",
            1: "mask_G333_B6_12m_0.1.crtf",
            2: "mask_G333_B6_12m_0.03.crtf",
            3: "mask_G333_B6_12m_0.03.crtf",
            4: "mask_G333_B6_12m_0.01.crtf",
            5: "mask_G333_B6_12m_0.01.crtf",
            "final": "mask_G333_B6_12m_final.crtf",
        },
        "scales": [0, 3, 9],
    },
    "G333.60_B6_12M_robust2": {
        "threshold": "0.15mJy",
        "niter": 70000,
        "maskname": "mask_G333_B6_12m_final.crtf",
        "scales": [0, 3, 9],
    },
    "G333.60_B6_12M_robust-2": {
        "threshold": "0.1mJy",
        "niter": 70000,
        "maskname": "mask_G333_B6_12m_final.crtf",
        "scales": [0, 3, 9],
    },
    "G333.60_B6_7M12M_robust0": {
        "threshold": {
            0: "1.2mJy",
            1: "1.2mJy",
            2: "0.8mJy",
            3: "0.4mJy",
            4: "0.2mJy",
            5: "0.15 mJy",
            "final": "0.15 mJy",
        },
        "niter": {0: 3000, 1: 3000, 2: 6000, 3: 12000, 4: 24000, 5: 48000, "final": 70000,},
        "maskname": {
            0: "mask_G333_B6_7m12m_0.1.crtf",
            1: "mask_G333_B6_7m12m_0.1.crtf",
            2: "mask_G333_B6_7m12m_0.03.crtf",
            3: "mask_G333_B6_7m12m_0.03.crtf",
            4: "mask_G333_B6_7m12m_0.01.crtf",
            5: "mask_G333_B6_7m12m_0.01.crtf",
            "final": "mask_G333_B6_7m12m_final.crtf",
        },
        "scales": [0, 3, 9, 27],
    },
    "G333.60_B6_7M12M_robust2": {
        "threshold": "0.15mJy",
        "niter": 70000,
        "maskname": "mask_G333_B6_7m12m_final.crtf",
        "scales": [0, 3, 9],
    },
    "G333.60_B6_7M12M_robust-2": {
        "threshold": "0.1mJy",
        "niter": 70000,
        "maskname": "mask_G333_B6_7m12m_final.crtf",
        "scales": [0, 3, 9, 27],
    },
    "G012.80_B3_7M12M_robust0": {
        "threshold": {0: "10.0mJy", 1: "10mJy", 2: "3mJy", 3: "3mJy", 4: "1mJy", 5: "0.25mJy",},
        "niter": {0: 100, 1: 500, 2: 1000, 3: 1500, 4: 3000, 5: 5000},
        "scales": {0: [0, 3, 9, 27, 100]},
    },
    "G012.80_B3_12M_robust0": {
        "threshold": {0: "10.0mJy", 1: "10mJy", 2: "5mJy", 3: "3mJy", 4: "1mJy", 5: "0.25mJy",},
        "niter": {0: 500, 1: 100, 2: 1000, 3: 3000, 4: 5000, 5: 7000},
    },
    "G012.80_B6_12M_robust0": {
        "threshold": {0: "3.0mJy", 1: "2mJy", 2: "1.5mJy", 3: "1mJy", 4: "1mJy", 5: "0.25mJy",},
        "niter": {0: 0, 1: 1500, 2: 3000, 3: 5000, 4: 7000, 5: 10000},
    },
    "G337.92_B3_12M_robust0": {"threshold": "0.25mJy", "scales": [0, 3, 9, 27]},
    "W51-IRS2_B6_12M_robust0": {
        "threshold": {
            0: "0.3mJy",
            1: "0.25mJy",
            2: "0.25mJy",
            3: "0.25mJy",
            4: "0.25mJy",
            5: "0.25mJy",
            6: "0.2mJy",
            7: "0.2mJy",
            8: "0.2mJy",
        },
        "scales": [0, 3, 9, 27],
    },
    "W51-IRS2_B3_12M_robust0": {
        "threshold": {0: "0.3mJy", 1: "0.2mJy", 2: "0.2mJy", 3: "0.1mJy", 4: "0.08mJy"},
        "scales": [0, 3, 9, 27],
    },
    "W51-IRS2_B3_7M12M_robust0": {
        "threshold": {0: "0.5mJy", 1: "0.3mJy", 2: "0.2mJy", 3: "0.1mJy", 4: "0.08mJy"},
        "scales": [0, 3, 9, 27],
        "cell": ["0.0375arcsec", "0.0375arcsec"],
        "imsize": [5000, 5000],
    },
    "G338.93_B3_12M_robust0": {
        "threshold": {0: "0.36mJy", 1: "0.30mJy", 2: "0.15mJy", "final": "0.1mJy"},
        "niter": {0: 2000, 1: 2000, 2: 5000, "final": 200000},
    },
    "G338.93_B3_12M_robust2": {"threshold": {"final": "0.10mJy"}, "niter": {"final": 200000},},
    "G338.93_B3_12M_robust-2": {"threshold": {"final": "0.30mJy"}, "niter": {"final": 200000},},
    "G338.93_B3_12M_robust0_bsens": {
        "threshold": {0: "0.34mJy", 1: "0.25mJy", 2: "0.15mJy", 3: "0.12mJy", "final": "0.1mJy",},
        "niter": {0: 2000, 1: 2000, 2: 5000, 3: 8000, "final": 200000},
    },
    "G338.93_B3_12M_robust2_bsens": {"threshold": {"final": "0.10mJy"}, "niter": {"final": 200000},},
    "G338.93_B3_12M_robust-2_bsens": {"threshold": {"final": "0.30mJy"}, "niter": {"final": 200000},},
    "G338.93_B3_7M12M_robust0": {
        "threshold": {0: "0.5mJy", 1: "0.4mJy", 2: "0.2mJy", "final": "0.1mJy"},
        "niter": {0: 2000, 1: 5000, 2: 8000, "final": 200000},
        "scales": [0, 3, 9, 27],
    },
    "G338.93_B3_7M12M_robust2": {"threshold": {"final": "0.1mJy"}, "niter": {"final": 200000},},
    "G338.93_B3_7M12M_robust-2": {"threshold": {"final": "0.1mJy"}, "niter": {"final": 200000},},
    "W51-E_B6_12M_robust0": {
        "threshold": {0: "0.3mJy", 1: "0.25mJy", 2: "0.25mJy", 3: "0.25mJy", 4: "0.25mJy", 5: "0.25mJy", 6: "0.2mJy",},
        "scales": [0, 3, 9, 27],
    },
    "W51-E_B3_12M_robust0": {
        "threshold": {0: "0.15mJy", 1: "0.15mJy", 2: "0.1mJy", 3: "0.09mJy", 4: "0.09mJy", 5: "0.08mJy", 6: "0.07mJy",},
        "scales": [0, 3, 9, 27],
        "imsize": [5000, 5000],
        "cell": ["0.0375arcsec", "0.0375arcsec"],
    },
    "W51-E_B3_12M_robust2": {"threshold": "3mJy", "scales": [0, 3, 9, 27]},
    "W51-E_B3_12M_robust-2": {"threshold": "1mJy", "scales": [0, 3, 9]},
    "W51-E_B6_7M12M_robust0": {"threshold": "3mJy", "scales": [0, 3, 9, 27]},
    "W51-E_B3_7M12M_robust0": {
        "threshold": {0: "5mJy", 1: "3mJy", 2: "1mJy", 3: "1mJy"},
        "scales": {0: [9, 27], 1: [3, 9, 27], 2: [0, 3, 9, 27], 3: [0, 3, 9, 27],},
        "cell": ["0.0375arcsec", "0.0375arcsec"],
        "imsize": [5000, 5000],
    },
    "W43-MM2_B6_12M_robust0": {
        "threshold": {
            0: "2.0mJy",
            1: "2.0mJy",
            2: "0.7mJy",
            3: "0.5mJy",
            4: "0.35mJy",
            5: "0.25mJy",
            "final": "0.35mJy",
        },
        "niter": {0: 1000, 1: 3000, 2: 10000, 3: 12000, 4: 15000, 5: 15000, "final": 22000,},
        "scales": [0, 3, 9, 27],
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "W43-MM2_B6_7M12M_robust0": {
        "threshold": {0: "2.0mJy", 1: "2.0mJy", 2: "1.0mJy", 3: "0.5mJy", 4: "0.4mJy", "final": "0.5mJy",},
        "niter": {0: 1000, 1: 5000, 2: 10000, 3: 10000, 4: 10000, "final": 25000},
        "scales": {
            0: [0, 3, 9, 27],
            1: [0, 3, 9, 27],
            2: [0, 3, 9, 27],
            3: [0, 3, 9, 27],
            4: [0, 3, 9, 27],
            "final": [0, 3, 9, 27, 81],
        },
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "W43-MM3_B6_12M_robust0": {
        "threshold": {
            0: "1.0mJy",
            1: "1.0mJy",
            2: "0.25mJy",
            3: "0.25mJy",
            4: "0.25mJy",
            5: "0.25mJy",
            "final": "0.23mJy",
        },
        "niter": {0: 1000, 1: 3000, 2: 12000, 3: 12000, 4: 12000, 5: 15000, "final": 18000,},
        "scales": [0, 3, 9, 27],
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "W43-MM3_B6_7M12M_robust0": {
        "threshold": {0: "1.0mJy", 1: "1.0mJy", 2: "0.7mJy", 3: "0.35mJy", 4: "0.35mJy", "final": "0.5mJy",},
        "niter": {0: 1000, 1: 5000, 2: 10000, 3: 10000, 4: 10000, "final": 10000},
        "scales": {
            0: [0, 3, 9, 27],
            1: [0, 3, 9, 27],
            2: [0, 3, 9, 27],
            3: [0, 3, 9, 27],
            4: [0, 3, 9, 27],
            "final": [0, 3, 9, 27, 54],
        },
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "W43-MM1_B3_12M_robust0": {
        "threshold": {0: "1.0mJy", 1: "0.25mJy", 2: "0.15mJy", 3: "0.1mJy", 4: "0.1mJy", "final": "0.12mJy",},
        "niter": {0: 1000, 1: 9000, 2: 15000, 3: 15000, 4: 17000, "final": 25000},
        "scales": {
            0: [0, 3, 9, 27],
            1: [0, 3, 9, 27],
            2: [0, 3, 9, 27],
            3: [0, 3, 9, 27],
            4: [0, 3, 9, 27],
            "final": [0, 3, 9, 27, 81],
        },
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "W43-MM1_B3_7M12M_robust0": {
        "threshold": {0: "1.0mJy", 1: "1.0mJy", 2: "0.23mJy", 3: "0.15mJy", 4: "0.1mJy", "final": "0.05mJy",},
        "niter": {0: 1000, 1: 9000, 2: 13000, 3: 15000, 4: 17000, "final": 26000},
        "scales": {
            0: [0, 3, 9, 27],
            1: [0, 3, 9, 27],
            2: [0, 3, 9, 27],
            3: [0, 3, 9, 27],
            4: [0, 3, 9, 27],
            "final": [0, 9, 27, 81, 162],
        },
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "W43-MM2_B3_12M_robust0": {
        "threshold": {0: "0.2mJy", 1: "0.5mJy", 2: "0.1mJy", 3: "0.1mJy", 4: "0.1mJy", "final": "0.12mJy",},
        "niter": {0: 9000, 1: 10000, 2: 16000, 3: 16000, 4: 18000, "final": 25000},
        "scales": {
            0: [0, 3, 9, 27],
            1: [0, 3, 9, 27],
            2: [0, 3, 9, 27],
            3: [0, 3, 9, 27],
            4: [0, 3, 9, 27],
            "final": [0, 9, 27, 81, 162],
        },
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "W43-MM2_B3_7M12M_robust0": {
        "threshold": {0: "0.5mJy", 1: "1.0mJy", 2: "0.5mJy", 3: "0.2mJy", 4: "0.08mJy", "final": "0.06mJy",},
        "niter": {0: 9000, 1: 10000, 2: 12000, 3: 15000, 4: 20000, 5: 25000},
        "scales": {
            0: [0, 3, 9, 27],
            1: [0, 3, 9, 27],
            2: [0, 3, 9, 27],
            3: [0, 3, 9, 27],
            4: [0, 3, 9, 27],
            "final": [0, 9, 27, 81, 162],
        },
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "W43-MM3_B3_12M_robust0": {
        "threshold": {0: "1.0mJy", 1: "0.75mJy", 2: "0.15mJy", 3: "0.1mJy", 4: "0.1mJy", "final": "0.11mJy",},
        "niter": {0: 1000, 1: 6000, 2: 12000, 3: 15000, 4: 15000, "final": 24000},
        "scales": {
            0: [0, 3, 9, 27],
            1: [0, 3, 9, 27],
            2: [0, 3, 9, 27],
            3: [0, 3, 9, 27],
            4: [0, 3, 9, 27],
            "final": [0, 3, 9, 27, 81],
        },
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "W43-MM3_B3_7M12M_robust0": {
        "threshold": {0: "1.0mJy", 1: "1.0mJy", 2: "0.5mJy", 3: "0.2mJy", 4: "0.1mJy", "final": "0.04mJy",},
        "niter": {0: 3000, 1: 8000, 2: 15000, 3: 17000, 4: 20000, "final": 25000},
        "scales": {
            0: [0, 3, 9, 27],
            1: [0, 3, 9, 27],
            2: [0, 3, 9, 27],
            3: [0, 3, 9, 27],
            4: [0, 3, 9, 27],
            "final": [0, 9, 27, 81, 162],
        },
        "maskname": {"final": ""},
        "usemask": {"final": "pb"},
    },
    "G353.41_B3_12M_robust-2": {"threshold": "0.5mJy", "scales": [0, 3, 9, 27]},
    "G353.41_B3_12M_robust0": {"threshold": "0.36mJy", "scales": [0, 3, 9, 27]},
    "G353.41_B3_12M_robust2": {"threshold": "0.28mJy", "scales": [0, 3, 9, 27]},
    "G353.41_B3_7M12M_robust-2": {"threshold": "0.52mJy", "scales": [0, 3, 9, 27]},
    "G353.41_B3_7M12M_robust0": {"threshold": "0.4mJy", "scales": [0, 3, 9, 27]},
    "G353.41_B3_7M12M_robust2": {"threshold": "0.42mJy", "scales": [0, 3, 9, 27]},
    "G353.41_B6_12M_robust-2": {"threshold": "1.4mJy", "scales": [0, 3, 9]},
    "G353.41_B6_12M_robust0": {"threshold": "1.04mJy", "scales": [0, 3, 9]},
    "G353.41_B6_12M_robust2": {"threshold": "0.74mJy", "scales": [0, 3, 9]},
    "G353.41_B6_7M12M_robust-2": {"threshold": "1.4mJy", "scales": [0, 3, 9]},
    "G353.41_B6_7M12M_robust0": {"threshold": "1.06mJy", "scales": [0, 3, 9]},
    "G353.41_B6_7M12M_robust2": {"threshold": "0.82mJy", "scales": [0, 3, 9]},
    "G327.29_B3_12M_robust0": {
        "threshold": {0: "1.5mJy", 1: "0.6mJy", 2: "0.5mJy", "final": "0.4mJy"},
        "niter": {0: 1000, 1: 2000, 2: 5000, "final": 200000},
        "scales": [0, 3, 9, 27],
    },
    "G327.29_B3_12M_robust-2": {"threshold": {"final": "0.4mJy"}, "niter": {"final": 200000}, "scales": [0, 3, 9, 27],},
    "G327.29_B3_12M_robust2": {"threshold": {"final": "0.4mJy"}, "niter": {"final": 200000}, "scales": [0, 3, 9, 27],},
    "G327.29_B3_7M12M_robust0": {
        "threshold": {0: "2.0mJy", 1: "1.8mJy", "final": "1.5mJy"},
        "niter": {0: 5000, 1: 5000, "final": 200000},
        "scales": [0, 3, 9, 27],
    },
    "G327.29_B3_7M12M_robust-2": {
        "threshold": {"final": "0.5mJy"},
        "niter": {"final": 200000},
        "scales": [0, 3, 9, 27],
    },
    "G327.29_B3_7M12M_robust2": {
        "threshold": {"final": "0.5mJy"},
        "niter": {"final": 100000},
        "scales": [0, 3, 9, 27],
    },
    "G327.29_B6_12M_robust0": {
        "threshold": {0: "2.0mJy", 1: "1.5mJy", 2: "1.0mJy", 3: "1.0mJy", 4: "0.8mJy", 5: "0.5mJy", "final": "0.5mJy",},
        "niter": {0: 1000, 1: 1000, 2: 5000, 3: 8000, 4: 10000, 5: 10000, "final": 20000,},
        "scales": [0, 3, 9, 27],
    },
    "G327.29_B6_12M_robust2": {"threshold": {"final": "1.0mJy"}, "niter": {"final": 20000},},
    "G327.29_B6_12M_robust-2": {"threshold": {"final": "1.0mJy"}, "niter": {"final": 20000},},
    "G327.29_B6_7M12M_robust0": {
        "threshold": {0: "2.0mJy", 1: "1.5mJy", 2: "1.0mJy", 3: "0.8mJy", 4: "0.8mJy", 5: "0.5mJy",},
        "niter": {0: 1000, 1: 1000, 2: 5000, 3: 8000, 4: 10000, 5: 200000},
        "scales": [0, 3, 9, 27],
    },
    "G327.29_B6_7M12M_robust2": {"threshold": {5: "1.0mJy"}, "niter": {5: 20000}},
    "G327.29_B6_7M12M_robust-2": {"threshold": {5: "1.0mJy"}, "niter": {5: 20000}},
    "G010.62_B3_12M_robust0": {
        "threshold": {0: "10mJy", 1: "5mJy", 2: "2.5 mJy", 3: "1.0mJy", 4: "0.5mJy", 5: "0.3mJy",},
        "niter": {0: 700, 1: 1300, 2: 2500, 3: 5000, 4: 10000, 5: 10000},
        "maskname": {
            0: "G010.62_centralBox_50_30.crtf",
            1: "G010.62_B3_50mJy.crtf",
            2: "G010.62_B3_15mJy.crtf",
            3: "G010.62_B3_05mJy.crtf",
            4: "G010.62_B3_03mJy.crtf",
            5: "G010.62_B3_01mJy.crtf",
        },
    },
    "G010.62_B6_12M_robust0": {
        "threshold": {0: "10mJy", 1: "5mJy", 2: "2.5 mJy", 3: "1.0mJy", 4: "0.5mJy", 5: "0.3mJy",},
        "niter": {0: 700, 1: 1300, 2: 2500, 3: 5000, 4: 10000, 5: 10000},
        "maskname": {
            0: "G010.62_centralBox_50_30.crtf",
            1: "G010.62_B3_50mJy.crtf",
            2: "G010.62_B3_15mJy.crtf",
            3: "G010.62_B3_05mJy.crtf",
            4: "G010.62_B3_03mJy.crtf",
            5: "G010.62_B3_01mJy.crtf",
        },
    },
    "G351.77_B6_7M_robust0": {
        "threshold": {0: "12.0mJy", 1: "12mJy", 2: "3mJy", 3: "0.25mJy", 4: "0.25mJy"},
        "niter": {0: 1000, 1: 3000, 2: 9000, 3: 18000, 4: 25000},
        "scales": [0, 3],
        "maskname": {
            0: "G351.77_B6_7M12M_iter1.crtf",
            1: "G351.77_B6_7M_iter1.crtf",
            2: "G351.77_B6_7M_iter1.crtf",
            3: "G351.77_B6_7M_iter1.crtf",
            4: "G351.77_B6_7M_iter1.crtf",
        },
    },
    "G351.77_B6_7M12M_robust0": {
        "threshold": {0: "10.0mJy", 1: "10.0mJy", 2: "5.0mJy", 3: "1.0mJy", 4: "1.0mJy", "final": "1.0mJy",},
        "niter": {0: 1000, 1: 3000, 2: 9000, 3: 18000, 4: 25000},
        "scales": [0, 3],
        "maskname": {
            0: "G351.77_B6_7M12M_iter1.crtf",
            1: "G351.77_B6_7M_iter1.crtf",
            2: "G351.77_B6_7M_iter1.crtf",
            3: "G351.77_B6_7M_iter1.crtf",
            4: "G351.77_B6_7M_iter1.crtf",
            "final": "G351.77_B6_7M12M_finaliter.crtf",
        },
    },
    "G351.77_B6_7M12M_robust2": {
        "threshold": {"final": "1.0mJy"},
        "niter": {"final": 25000},
        "scales": [0, 3],
        "maskname": {"final": "G351.77_B6_7M12M_finaliter.crtf"},
    },
    "G351.77_B6_7M12M_robust-2": {
        "threshold": {"final": "1.0mJy"},
        "niter": {"final": 18000},
        "scales": [0, 3],
        "maskname": {"final": "G351.77_B6_7M12M_finaliter.crtf"},
    },
    "G351.77_B6_12M_robust0": {
        "threshold": {0: "12e-4Jy", 1: "12e-4Jy", 2: "12e-4Jy", 3: "12e-4Jy", 4: "12e-4Jy",},
        "niter": {0: 1000, 1: 3000, 2: 9000, 3: 18000, 4: 18000},
        "maskname": {
            0: "G351.77_B6_12M.crtf",
            1: "G351.77_B6_12M.crtf",
            2: "G351.77_B6_12M.crtf",
            3: "G351.77_B6_12M.crtf",
            4: "G351.77_B6_12M.crtf",
            "final": "G351.77_B6_12M_final.crtf",
        },
    },
    "G351.77_B6_12M_robust2": {
        "threshold": {4: "10e-4Jy"},
        "niter": {4: 18000},
        "maskname": {4: "G351.77_B6_12M_final.crtf"},
    },
    "G351.77_B6_12M_robust-2": {
        "threshold": {0: "14.4e-4Jy", 1: "14.4e-4Jy", 2: "14.4e-4Jy", 3: "14.4e-4Jy", 4: "14.4e-4Jy",},
        "niter": {4: 18000},
        "maskname": {4: "G351.77_B6_12M_final.crtf"},
    },
    "G351.77_B3_12M_robust-2": {
        "threshold": {4: "8e-4Jy"},
        "niter": {4: 18000},
        "maskname": {4: "G351.77_B3_12M_robust2_bsens.crtf"},
    },
    "G351.77_B3_12M_robust2": {
        "threshold": {4: "3e-4Jy"},
        "niter": {4: 18000},
        "maskname": {4: "G351.77_B3_12M_robust2_bsens.crtf"},
    },
    "G351.77_B3_12M_robust0": {
        "threshold": {0: "3e-4Jy", 1: "3e-4Jy", 2: "3e-4Jy", 3: "3e-4Jy", 4: "3e-4Jy"},
        "niter": {0: 1000, 1: 3000, 2: 9000, 3: 18000, 4: 18000},
        "maskname": {
            0: "G351.77_B3_12M_robust2_bsens.crtf",
            1: "G351.77_B3_12M_robust2_bsens.crtf",
            2: "G351.77_B3_12M_robust2_bsens.crtf",
            3: "G351.77_B3_12M_robust2_bsens.crtf",
            4: "G351.77_B3_12M_robust2_bsens.crtf",
        },
    },
    "G351.77_B3_7M12M_robust-2": {
        "threshold": {4: "3.2e-4Jy"},
        "niter": {4: 18000},
        "scales": [0, 3],
        "maskname": {4: "G351.77_B3_7M12M_robust2_bsens.crtf"},
    },
    "G351.77_B3_7M12M_robust2": {
        "threshold": {4: "1.8e-4Jy"},
        "niter": {4: 18000},
        "scales": [0, 3],
        "maskname": {4: "G351.77_B3_7M12M_robust2_bsens.crtf"},
    },
    "G351.77_B3_7M12M_robust0": {
        "threshold": {0: "2e-4Jy", 1: "2e-4Jy", 2: "2e-4Jy", 3: "2e-4Jy", 4: "2e-4Jy"},
        "niter": {0: 1000, 1: 3000, 2: 9000, 3: 9000, 4: 9000},
        "scales": [0, 3],
        "maskname": {
            0: "G351.77_B3_7M12M_robust2_bsens.crtf",
            1: "G351.77_B3_7M12M_robust2_bsens.crtf",
            2: "G351.77_B3_7M12M_robust2_bsens.crtf",
            3: "G351.77_B3_7M12M_robust2_bsens.crtf",
            4: "G351.77_B3_7M12M_robust2_bsens.crtf",
        },
    },
    "G338.93_B6_12M_robust0": {
        "threshold": {
            0: "1.2mJy",
            1: "1.2mJy",
            2: "0.9mJy",
            3: "0.8mJy",
            4: "0.7mJy",
            5: "0.5mJy",
            6: "0.35mJy",
            "final": "0.35mJy",
        },
        "niter": {0: 1000, 1: 1000, 2: 2000, 3: 3000, 4: 4000, 5: 5000, 6: 6000, "final": 50000,},
        "scales": [0, 3, 9, 27],
    },
    "G338.93_B6_12M_robust2": {"threshold": {"final": "0.25mJy"}, "niter": {"final": 20000}, "scales": [0, 3, 9, 27],},
    "G338.93_B6_12M_robust-2": {"threshold": {"final": "0.50mJy"}, "niter": {"final": 20000}, "scales": [0, 3, 9],},
    "G338.93_B6_12M_robust0_bsens": {
        "threshold": {
            0: "1.2mJy",
            1: "1.2mJy",
            2: "0.9mJy",
            3: "0.8mJy",
            4: "0.7mJy",
            5: "0.5mJy",
            6: "0.30mJy",
            "final": "0.35mJy",
        },
        "niter": {0: 1000, 1: 1000, 2: 2000, 3: 3000, 4: 4000, 5: 5000, 6: 6000, "final": 50000,},
        "scales": [0, 3, 9, 27],
    },
    "G338.93_B6_12M_robust2_bsens": {
        "threshold": {"final": "0.20mJy"},
        "niter": {"final": 20000},
        "scales": [0, 3, 9, 27],
    },
    "G338.93_B6_12M_robust-2_bsens": {
        "threshold": {"final": "0.45mJy"},
        "niter": {"final": 20000},
        "scales": [0, 3, 9],
    },
    "G328.25_B6_7M12M_robust0": {
        "threshold": {0: "6mJy", 1: "4mJy", 2: "4mJy", 3: "4mJy", 4: "1.5mJy"},
        "niter": {0: 1000, 1: 3000, 2: 9000, 3: 18000, 4: 18000},
        "scales": [0, 3],
        "maskname": {
            0: "G328_B6_7M12M_iter2_n2.crtf",
            1: "G328_B6_7M12M_iter2_n2.crtf",
            2: "G328_B6_7M12M_iter2_n2.crtf",
            3: "G328_B6_7M12M_iter4_n.crtf",
            4: "G328_B6_clean_robust0.crtf",
        },
    },
    "G328.25_B6_7M12M_robust2": {
        "threshold": {4: "1.5mJy"},
        "niter": {4: 18000},
        "scales": [0, 3],
        "maskname": {4: "G328_B6_clean_robust0.crtf"},
    },
    "G328.25_B6_7M12M_robust-2": {
        "threshold": {4: "2mJy"},
        "niter": {4: 18000},
        "scales": [0, 3],
        "maskname": {4: "G328_B6_clean_robust0.crtf"},
    },
    "G328.25_B6_12M_robust0": {
        "threshold": {0: "1e-3Jy", 1: "2mJy", 2: "1mJy", 3: "0.5mJy", 4: "0.5mJy", 5: "0.5mJy",},
        "niter": {0: 3000, 1: 3000, 2: 9000, 3: 18000, 4: 18000, 5: 18000},
        "maskname": {
            0: "G328_B6_clean_12M_robust0_3sigma.crtf",
            1: "G328_B6_clean_robust0.crtf",
            2: "G328_B6_clean_robust0.crtf",
            3: "G328_B6_clean_robust0.crtf",
            4: "G328_B6_clean_robust0.crtf",
            5: "G328_B6_clean_robust0.crtf",
        },
    },
    "G328.25_B6_12M_robust-2": {
        "threshold": {0: "16e-4Jy", 1: "2mJy", 2: "1mJy", 3: "0.5mJy", 4: "0.5mJy", 5: "0.5mJy",},
        "niter": {0: 3000, 1: 3000, 2: 9000, 3: 18000, 4: 18000, 5: 18000},
        "maskname": {
            0: "G328_B6_clean_12M_robust0_3sigma.crtf",
            1: "G328_B6_clean_robust0.crtf",
            2: "G328_B6_clean_robust0.crtf",
            3: "G328_B6_clean_robust0.crtf",
            4: "G328_B6_clean_robust0.crtf",
            5: "G328_B6_clean_robust0.crtf",
        },
    },
    "G328.25_B6_12M_robust2": {
        "threshold": {0: "8e-4Jy", 1: "2mJy", 2: "1mJy", 3: "0.5mJy", 4: "0.5mJy", 5: "0.5mJy",},
        "niter": {0: 3000, 1: 3000, 2: 9000, 3: 18000, 4: 18000, 5: 18000},
        "maskname": {
            0: "G328_B6_clean_12M_robust0_3sigma.crtf",
            1: "G328_B6_clean_robust0.crtf",
            2: "G328_B6_clean_robust0.crtf",
            3: "G328_B6_clean_robust0.crtf",
            4: "G328_B6_clean_robust0.crtf",
            5: "G328_B6_clean_robust0.crtf",
        },
    },
    "G328.25_B3_7M12M_robust0": {
        "threshold": {0: "0.6mJy", 1: "0.3mJy", 2: "0.3mJy", 3: "0.3mJy", 4: "0.2mJy",},  # rms = 3e-4 Jy/beam
        "niter": {0: 1000, 1: 3000, 2: 9000, 3: 18000, 4: 18000},
        "maskname": {
            0: "G328.25_B3_12M_clean_robust2_1stiter_3sigma.crtf",
            1: "G328.25_B3_7M12M_clean_robust0_1stiter_3sigma.crtf",
            2: "G328_B3_mask.crtf",
            3: "G328_B3_mask.crtf",
            4: "G328_B3_mask.crtf",
        },
    },
    "G328.25_B3_7M12M_robust-2": {"threshold": {4: "1mJy"}, "niter": {4: 25000}, "maskname": {4: "G328_B3_mask.crtf"},},
    "G328.25_B3_7M12M_robust2": {"threshold": {4: "1mJy"}, "niter": {4: 25000}, "maskname": {4: "G328_B3_mask.crtf"},},
    "G328.25_B3_12M_robust0": {
        "threshold": {0: "0.30mJy", 1: "0.3mJy", 2: "0.3mJy", 3: "0.3mJy", 4: "0.2mJy",},  # rms = 1e-4 Jy/beam
        "niter": {0: 5000, 1: 9000, 2: 10000, 3: 15000, 4: 20000},
        "maskname": {
            0: "G328.25_B3_12M_clean_robust0_1stiter_3sigma.crtf",
            1: "G328.25_B3_12M_clean_robust0_2nditer_3sigma.crtf",
            2: "G328.25_B3_12M_clean_robust0_2nditer_3sigma.crtf",
            3: "G328.25_B3_12M.crtf",
            4: "G328.25_B3_12M.crtf",
        },
    },
    "G328.25_B3_12M_robust-2": {
        "threshold": {4: "3.2e-4Jy"},  # 2*RMS, RMS =1.6e-4 Jy/beam
        "niter": {4: 15000},
        "maskname": {4: "G328.25_B3_12M.crtf"},
    },  # RMS ~ 1e-4 Jy/beam for BSENS
    "G328.25_B3_12M_robust2": {
        "threshold": {4: "1.9e-4Jy"},  # RMS = 0.95e-4 Jy/beam
        "niter": {4: 15000},
        "maskname": {4: "G328.25_B3_12M.crtf"},
    },  # RMS ~ 1e-4 Jy/beam for BSENS
    "G328.25_B6_7M_robust0": {
        "threshold": {0: "10mJy", 1: "5mJy", 2: "5mJy", 3: "5mJy", 4: "5mJy"},
        "niter": {0: 1000, 1: 3000, 2: 9000, 3: 18000, 4: 18000},
        "scales": [0, 3],
        "maskname": {
            0: "G328_B6_clean_robust0.crtf",
            1: "G328_B6_clean_robust0.crtf",
            2: "G328_B6_clean_robust0.crtf",
            3: "G328_B6_clean_robust0.crtf",
            4: "G328_B6_clean_robust0.crtf",
        },
    },
    "G328.25_B6_7M12M_robust0": {
        "threshold": {0: "6mJy", 1: "4mJy", 2: "4mJy", 3: "4mJy", 4: "1.5mJy"},
        "niter": {0: 1000, 1: 3000, 2: 9000, 3: 18000, 4: 18000},
        "scales": [0, 3],
        "maskname": {
            0: "G328_B6_7M12M_iter2_n2.crtf",  # G328_B6_7M12M_iter1_n.crtf
            1: "G328_B6_7M12M_iter2_n2.crtf",  # G328_B6_7M12M_iter2_n.crtf
            2: "G328_B6_7M12M_iter2_n2.crtf",  # G328_B6_7M12M_iter2_n.crtf
            3: "G328_B6_7M12M_iter4_n.crtf",
            4: "G328_B6_clean_robust0.crtf",
        },
    },
    "G328.25_B6_7M12M_robust2": {
        "threshold": {4: "1.5mJy"},  # 5 for cleanest
        "niter": {4: 18000},
        "scales": [0, 3],
        "maskname": {4: "G328_B6_clean_robust0.crtf"},
    },
    "G328.25_B6_7M12M_robust-2": {
        "threshold": {4: "2mJy"},
        "niter": {4: 18000},
        "scales": [0, 3],
        "maskname": {4: "G328_B6_clean_robust0.crtf"},
    },
    "G328.25_B6_12M_robust0": {
        "threshold": {0: "1e-3Jy", 1: "2mJy", 2: "1mJy", 3: "0.5mJy", 4: "0.5mJy", 5: "0.5mJy",},
        "niter": {0: 3000, 1: 3000, 2: 9000, 3: 18000, 4: 18000, 5: 18000},
        "maskname": {
            0: "G328_B6_clean_12M_robust0_3sigma.crtf",
            1: "G328_B6_clean_robust0.crtf",
            2: "G328_B6_clean_robust0.crtf",
            3: "G328_B6_clean_robust0.crtf",
            4: "G328_B6_clean_robust0.crtf",
            5: "G328_B6_clean_robust0.crtf",
        },
    },
    "G328.25_B6_12M_robust-2": {
        "threshold": {5: "0.5mJy"},
        "niter": {5: 18000},
        "maskname": {5: "G328_B6_clean_robust0.crtf"},
    },
    "G328.25_B6_12M_robust2": {
        "threshold": {5: "0.5mJy"},
        "niter": {5: 18000},
        "maskname": {5: "G328_B6_clean_robust0.crtf"},
    },
}


for key in imaging_parameters_nondefault:
    if "bsens" in key:
        check_key = "_".join(key.split("_")[:-1])
        assert check_key in imaging_parameters, "key {0} not in impars!".format(check_key)
        imaging_parameters[key] = copy.deepcopy(imaging_parameters[check_key])
    else:
        assert key in imaging_parameters, "key {0} was not in impars".format(key)
    imaging_parameters[key].update(imaging_parameters_nondefault[key])


"""
Self-calibration parameters are defined here
"""

default_selfcal_pars = {
    ii: {
        "solint": "inf",
        "gaintype": "T",
        "solnorm": True,
        # 'combine': 'spw', # consider combining across spw bounds
        "calmode": "p",
    }
    for ii in range(1, 5)
}

selfcal_pars_default = {key: copy.deepcopy(default_selfcal_pars) for key in imaging_parameters}

selfcal_pars_custom = {
    "G008.67_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "1200s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "600s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "300s", "solnorm": False},
        5: {"calmode": "p", "gaintype": "T", "solint": "200s", "solnorm": False},
    },
    "G008.67_B3_12M_robust0_bsens": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "1200s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "600s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "300s", "solnorm": False},
        5: {"calmode": "p", "gaintype": "T", "solint": "200s", "solnorm": False},
    },
    "G008.67_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "1200s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "600s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "300s", "solnorm": False},
        5: {"calmode": "p", "gaintype": "T", "solint": "200s", "solnorm": False},
    },
    "G008.67_B6_12M_robust0_bsens": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "1200s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "600s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "300s", "solnorm": False},
        5: {"calmode": "p", "gaintype": "T", "solint": "200s", "solnorm": False},
    },
    "G008.67_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G008.67_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "40s", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "25s", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "10s", "solnorm": True},
        5: {"calmode": "ap", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
    },
    "G010.62_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "45s", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "30s", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "15s", "solnorm": True},
    },
    "G010.62_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "40s", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "25s", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "10s", "solnorm": True},
        5: {"calmode": "ap", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
    },
    "G010.62_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "45s", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "30s", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "15s", "solnorm": True},
    },
    "G010.62_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G010.62_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "1200s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "300s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "300s", "solnorm": False},
        5: {"calmode": "a", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
    },
    "G012.80_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "minsnr": 5, "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "G", "minsnr": 5, "solint": "inf", "solnorm": False},
        3: {"calmode": "p", "gaintype": "G", "minsnr": 5, "solint": "1200s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "G", "minsnr": 4, "solint": "600s", "solnorm": False},
        5: {"calmode": "a", "gaintype": "G", "minsnr": 5, "solint": "inf", "solnorm": False},
    },
    "G012.80_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G012.80_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "60s", "solnorm": True},
    },
    "G327.29_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B3_7M12M_robust0": {1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True}},
    "G327.29_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "G", "solint": "60s", "solnorm": True},
        3: {"calmode": "p", "gaintype": "G", "solint": "20s", "solnorm": True},
        4: {"calmode": "p", "gaintype": "G", "solint": "10s", "solnorm": True},
        5: {"calmode": "p", "gaintype": "G", "solint": "5s", "solnorm": True},
    },
    "G327.29_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "G", "solint": "60s", "solnorm": True},
        3: {"calmode": "p", "gaintype": "G", "solint": "20s", "solnorm": True},
        4: {"calmode": "p", "gaintype": "G", "solint": "10s", "solnorm": True},
        5: {"calmode": "p", "gaintype": "G", "solint": "5s", "solnorm": True},
    },
    "G327.29_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G327.29_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B3_12M_robust0": {
        1: {
            "calmode": "p",
            "combine": "scan",
            "gaintype": "T",
            "minblperant": 3,
            "minsnr": 2,
            "refant": "DV01",
            "solint": "inf",
            "solnorm": False,
        },
        2: {
            "calmode": "p",
            "combine": "scan",
            "gaintype": "T",
            "minblperant": 3,
            "minsnr": 2,
            "refant": "DV01",
            "solint": "int",
            "solnorm": False,
        },
        3: {
            "calmode": "p",
            "combine": "spw",
            "gaintype": "T",
            "minblperant": 3,
            "minsnr": 2,
            "refant": "DV01",
            "solint": "60s",
            "solnorm": False,
        },
        4: {
            "calmode": "p",
            "combine": "spw",
            "gaintype": "T",
            "minblperant": 3,
            "minsnr": 2,
            "refant": "DV01",
            "solint": "30s",
            "solnorm": False,
        },
    },
    "G328.25_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B3_7M12M_robust0": {
        1: {
            "calmode": "p",
            "combine": "scan",
            "gaintype": "T",
            "minblperant": 3,
            "minsnr": 2,
            "refant": "DV01",
            "solint": "inf",
            "solnorm": False,
        },
        2: {
            "calmode": "p",
            "combine": "scan",
            "gaintype": "T",
            "minblperant": 3,
            "minsnr": 2,
            "refant": "DV01",
            "solint": "inf",
            "solnorm": False,
        },
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B6_12M_robust0": {
        1: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "300s", "solnorm": False},
        3: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "90s", "solnorm": False},
        4: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "60s", "solnorm": False},
    },
    "G328.25_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B6_7M12M_robust0": {
        1: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "300s", "solnorm": False},
        3: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "200s", "solnorm": False},
        4: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "90s", "solnorm": False},
    },
    "G328.25_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G328.25_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "inf", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "100s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "60s", "solnorm": False},
    },
    "G328.25_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "15s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "5s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
        5: {"calmode": "ap", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "15s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "5s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
        5: {"calmode": "ap", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B6_12M_robust0": {
        1: {"calmode": "p", "combine": "spw", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "combine": "spw", "gaintype": "T", "solint": "15s", "solnorm": False},
        3: {"calmode": "p", "combine": "spw", "gaintype": "T", "solint": "5s", "solnorm": False},
        4: {"calmode": "p", "combine": "spw", "gaintype": "T", "solint": "int", "solnorm": False},
        5: {"calmode": "ap", "combine": "spw", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B6_7M12M_robust0": {
        1: {"calmode": "p", "combine": "spw", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "combine": "spw", "gaintype": "T", "solint": "15s", "solnorm": False},
        3: {"calmode": "p", "combine": "spw", "gaintype": "T", "solint": "5s", "solnorm": False},
        4: {"calmode": "p", "combine": "spw", "gaintype": "T", "solint": "int", "solnorm": False},
        5: {"calmode": "ap", "combine": "spw", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G333.60_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B3_12M_robust0": {
        1: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "300s", "solnorm": False},
        3: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "60s", "solnorm": False},
        4: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "30s", "solnorm": False},
    },
    "G337.92_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B3_7M12M_robust0": {
        1: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "int", "solnorm": False},
        3: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "90s", "solnorm": False},
        4: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "60s", "solnorm": False},
    },
    "G337.92_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G337.92_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_12M_robust-2_bsens": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_12M_robust0": {
        1: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "60s", "solnorm": True},
    },
    "G338.93_B3_12M_robust0_bsens": {
        1: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "60s", "solnorm": True},
        3: {"calmode": "ap", "combine": "scan", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_12M_robust2_bsens": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "combine": "scan", "gaintype": "T", "solint": "60s", "solnorm": True},
    },
    "G338.93_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_12M_robust-2_bsens": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "G", "solint": "60s", "solnorm": True},
        3: {"calmode": "p", "gaintype": "G", "solint": "30s", "solnorm": True},
        4: {"calmode": "p", "gaintype": "G", "solint": "20s", "solnorm": True},
        5: {"calmode": "p", "gaintype": "G", "solint": "10s", "solnorm": True},
        6: {"calmode": "p", "gaintype": "G", "solint": "5s", "solnorm": True},
    },
    "G338.93_B6_12M_robust0_bsens": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_12M_robust2_bsens": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G338.93_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "90s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "60s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "30s", "solnorm": False},
    },
    "G351.77_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "90s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "60s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "30s", "solnorm": False},
    },
    "G351.77_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "150s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "60s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 2, "solint": "30s", "solnorm": False},
    },
    "G351.77_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "300s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "150s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "60s", "solnorm": False},
    },
    "G351.77_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G351.77_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "inf", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "100s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 3, "solint": "60s", "solnorm": False},
    },
    "G351.77_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        5: {"calmode": "ap", "gaintype": "G", "solint": "inf", "solnorm": False},
        6: {"calmode": "ap", "gaintype": "G", "solint": "inf", "solnorm": False},
    },
    "G353.41_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        5: {"calmode": "ap", "gaintype": "G", "solint": "inf", "solnorm": False},
        6: {"calmode": "ap", "gaintype": "G", "solint": "inf", "solnorm": False},
    },
    "G353.41_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        5: {"calmode": "ap", "gaintype": "G", "solint": "inf", "solnorm": False},
        6: {"calmode": "ap", "gaintype": "G", "solint": "inf", "solnorm": False},
    },
    "G353.41_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        5: {"calmode": "ap", "gaintype": "G", "solint": "inf", "solnorm": False},
        6: {"calmode": "ap", "gaintype": "G", "solint": "inf", "solnorm": False},
    },
    "G353.41_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "G353.41_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "solint": "300s", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "300s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
    },
    "W43-MM1_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM1_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "300s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
    },
    "W43-MM2_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "300s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
    },
    "W43-MM2_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "G", "solint": "1200s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "G", "solint": "600s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "G", "solint": "300s", "solnorm": False},
        5: {"calmode": "p", "gaintype": "G", "solint": "int", "solnorm": False},
    },
    "W43-MM2_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "G", "solint": "500s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "G", "solint": "int", "solnorm": False},
        4: {"calmode": "p", "gaintype": "G", "solint": "int", "solnorm": False},
    },
    "W43-MM2_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM2_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "600s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "200s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
    },
    "W43-MM3_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "T", "solint": "300s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
        4: {"calmode": "p", "gaintype": "T", "solint": "int", "solnorm": False},
    },
    "W43-MM3_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "G", "solint": "1200s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "G", "solint": "600s", "solnorm": False},
        4: {"calmode": "p", "gaintype": "G", "solint": "300s", "solnorm": False},
        5: {"calmode": "p", "gaintype": "G", "solint": "int", "solnorm": False},
    },
    "W43-MM3_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "G", "solint": "inf", "solnorm": False},
        2: {"calmode": "p", "gaintype": "G", "solint": "500s", "solnorm": False},
        3: {"calmode": "p", "gaintype": "G", "solint": "int", "solnorm": False},
        4: {"calmode": "p", "gaintype": "G", "solint": "int", "solnorm": False},
    },
    "W43-MM3_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W43-MM3_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        5: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        6: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
    },
    "W51-E_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
    },
    "W51-E_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B6_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        5: {"calmode": "ap", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
        6: {"calmode": "ap", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
    },
    "W51-E_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B6_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        5: {"calmode": "p", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        6: {"calmode": "ap", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
        7: {"calmode": "ap", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
    },
    "W51-E_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-E_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B3_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B3_12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B3_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B3_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B3_7M12M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B3_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B3_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B3_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B3_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B6_12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B6_12M_robust0": {
        1: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "60s", "solnorm": True},
        2: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "60s", "solnorm": True},
        3: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "60s", "solnorm": True},
        4: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "60s", "solnorm": True},
        5: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "60s", "solnorm": False},
        6: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "60s", "solnorm": False},
        7: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "60s", "solnorm": False},
        8: {"calmode": "ap", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
    },
    "W51-IRS2_B6_12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B6_7M12M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B6_7M12M_robust0": {
        1: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": True},
        5: {"calmode": "ap", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
        6: {"calmode": "ap", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
        7: {"calmode": "ap", "combine": "", "gaintype": "T", "minsnr": 5, "solint": "inf", "solnorm": False},
    },
    "W51-IRS2_B6_7M12M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B6_7M_robust-2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B6_7M_robust0": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
    "W51-IRS2_B6_7M_robust2": {
        1: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        2: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        3: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
        4: {"calmode": "p", "gaintype": "T", "solint": "inf", "solnorm": True},
    },
}


selfcal_pars = selfcal_pars_default.copy()
for key in selfcal_pars_custom:
    for iternum in selfcal_pars_custom[key]:
        if iternum in selfcal_pars[key]:
            selfcal_pars[key][iternum].update(selfcal_pars_custom[key][iternum])
        else:
            selfcal_pars[key][iternum] = selfcal_pars_custom[key][iternum]

del selfcal_pars["G338.93_B3_12M_robust0"][3]
del selfcal_pars["G338.93_B3_12M_robust0"][4]
del selfcal_pars["G338.93_B3_12M_robust0_bsens"][4]
del selfcal_pars["G338.93_B3_7M12M_robust0"][3]
del selfcal_pars["G338.93_B3_7M12M_robust0"][4]
del selfcal_pars["G327.29_B3_12M_robust0"][3]
del selfcal_pars["G327.29_B3_12M_robust0"][4]
del selfcal_pars["G327.29_B3_7M12M_robust0"][2]
del selfcal_pars["G327.29_B3_7M12M_robust0"][3]
del selfcal_pars["G327.29_B3_7M12M_robust0"][4]


line_imaging_parameters_default = {
    "{0}_{1}_{2}_robust{3}{4}".format(field, band, array, robust, contsub): {
        "niter": 5000000,
        "threshold": "5sigma", # Aug 7, 2020: drop it back to 5-sigma
        "robust": robust,
        "weighting": "briggs",
        "deconvolver": "hogbom",
        # "scales": [0, 3, 9, 27, 81],
        # "nterms": 1,
        "gridder": "mosaic",
        "specmode": "cube",
        "outframe": "LSRK",
        "veltype": "radio",
        "usemask": "auto-multithresh",
        "sidelobethreshold": 2.0,
        "noisethreshold": 4.2,
        "lownoisethreshold": 1.5,
        "minbeamfrac": 0.3,
        "negativethreshold": 15.0,
        "pblimit": 0.0,
        "pbmask": 0.2,
        "pbcor": True,
        "perchanweightdensity": False,
        "interactive": False,
    }
    for field in allfields
    for band in ("B3", "B6")
    for array in ("12M", "7M12M", "7M")
    # for robust in (0,)
    for robust in (-2, 0, 2)
    for contsub in ("", "_contsub")
}

line_imaging_parameters = copy.deepcopy(line_imaging_parameters_default)

line_imaging_parameters_custom = {
    "G337.92_B3_12M_robust0": {"usemask": "auto-multithresh"},
    "G337.92_B3_12M_robust0_contsub": {"usemask": "auto-multithresh"},
    "G333.60_B3_12M_robust0": {"niter": 500000, "scales": [0, 3, 9, 27]},
    "G333.60_B3_12M_robust0_contsub": {"niter": 500000, "scales": [0, 3, 9, 27]},
    "W51-E_B6_12M_robust0": {"usemask": "auto-multithresh", "sidelobethreshold": 1.0, "threshold": "5sigma"},
}

for key in line_imaging_parameters_custom:
    line_imaging_parameters[key].update(line_imaging_parameters_custom[key])

default_lines = {
    "n2hp": "93.173700GHz",
    "sio": "217.104984GHz",
    "h2co303": "218.222195GHz",
    "12co": "230.538GHz",
    "h30a": "231.900928GHz",
    "h41a": "92.034434GHz",
    "c18o": "219.560358GHz",
    "ch3cn": "92.26144GHz",
    "ch3cch": "102.547983GHz",
}
field_vlsr = {
    "W51-E": "55km/s",
    "W51-IRS2": "55km/s",
    "G010.62": "-2km/s",
    "G353.41": "-18km/s",
    "W43-MM1": "97km/s",
    "W43-MM2": "97km/s",
    "W43-MM3": "97km/s",
    "G337.92": "-40km/s",
    "G338.93": "-62km/s",
    "G328.25": "-43km/s",
    "G327.29": "-45km/s",
    "G333.60": "-47km/s",
    "G008.67": "37.60km/s",
    "G012.80": "37.00km/s",
    "G351.77": "-3.00km/s",
}
# line parameters are converted by line_imaging.py into tclean parameters
line_parameters_default = {
    field: {
        line: {"restfreq": freq, "vlsr": field_vlsr[field], "cubewidth": "50km/s"}
        for line, freq in default_lines.items()
    }
    for field in allfields
}
for field in allfields:
    line_parameters_default[field]["12co"]["cubewidth"] = "150km/s"
    line_parameters_default[field]["ch3cn"]["cubewidth"] = "150km/s"  # is 150 wide enough?
line_parameters = copy.deepcopy(line_parameters_default)

line_parameters_custom = {
    "G008.67": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "100km/s", "vlsr": "44km/s"},
    },
    "G010.62": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "100km/s", "vlsr": "0km/s"},
        "n2hp": {"cubewidth": "60km/s"},
    },
    "G012.80": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "100km/s", "vlsr": "32km/s"},
    },
    "G327.29": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "60km/s", "vlsr": "-42km/s"},
    },
    "G328.25": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "60km/s", "vlsr": "-37km/s"},
    },
    "G333.60": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "100km/s", "vlsr": "-44km/s", "width": "2km/s"},
    },
    "G337.92": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "80km/s", "vlsr": "-36km/s"},
    },
    "G338.93": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "60km/s", "vlsr": "-63km/s"},
        "sio": {"cubewidth": "120km/s"},
    },
    "G351.77": {"12co": {"cubewidth": "150km/s"}, "ch3cn": {"cubewidth": "150km/s"}},
    "G353.41": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "80km/s", "vlsr": "-17km/s"},
        "n2hp": {"cubewidth": "32km/s"},
    },
    "W43-MM1": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "80km/s", "vlsr": "100km/s"},
    },
    "W43-MM2": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "60km/s", "vlsr": "103km/s"},
    },
    "W43-MM3": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "100km/s", "vlsr": "90km/s"},
    },
    "W51-E": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "100km/s", "vlsr": "59km/s"},
        "n2hp": {"cubewidth": "60km/s"},
        "sio": {"cubewidth": "120km/s"},
    },
    "W51-IRS2": {
        "12co": {"cubewidth": "150km/s"},
        "ch3cn": {"cubewidth": "150km/s"},
        "h41a": {"cubewidth": "100km/s", "vlsr": "56km/s"},
        "sio": {"cubewidth": "120km/s"},
    },
}

for field in line_parameters_custom:
    for line in line_parameters_custom[field]:
        line_parameters[field][line].update(line_parameters_custom[field][line])

# use the continuum image as the startmodel for the non-contsub'd data
# (nice idea, didn't work)
# line_imaging_parameters['W51-E_B6_12M_robust0']['startmodel'] = 'imaging_results/W51-E_B6_uid___A001_X1296_X215_continuum_merged_12M_robust0_selfcal7.model.tt0'
# line_imaging_parameters['W51-E_B3_12M_robust0']['startmodel'] = 'imaging_results/W51-E_B3_uid___A001_X1296_X10b_continuum_merged_12M_robust0_selfcal7.model.tt0'
