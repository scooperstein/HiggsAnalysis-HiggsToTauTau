from optparse import OptionParser, OptionGroup

## set up the option parser
parser = OptionParser(usage="usage: %prog [options]",
                      description="Script to combine 2011+2012 and high and low pt event categories. This script requires that the script run_macros.py has been executed beforehand and produced resultrs w/o issues.")
## direct options
parser.add_option("-a", "--analysis", dest="analysis", default="sm", type="choice", help="Type of analysis (sm or mssm). Lower case is required. [Default: sm]", choices=["sm", "mssm"])
parser.add_option("-t", "--type", dest="type", default="rescaled", type="string", help="Type of plots, unscaled or rescaled. [Default: \"rescaled\"]")
parser.add_option("--mA", dest="mA", default="160", type="float", help="Mass of pseudoscalar mA only needed for mssm. [Default: '160']")
parser.add_option("--tanb", dest="tanb", default="20", type="float", help="Tanb only needed for mssm. [Default: '20']")
## check number of arguments; in case print usage
(options, args) = parser.parse_args()


## a set of pre-defined lists
channels   = [
    "emu",
    "eleTau",
    "muTau",
    #"mumu",
    ]

categories_sm = [
    "0jet_low",
    "0jet_high",
    "0jet",
    "1jet_low",
    "1jet_high",
    #"1jet",  ## these are not combined at the moment due to different binning in low and high pt
    "vbf",
    ]

categories_mssm = [
    #"0jet_low",
    #"0jet_high",
    #"0jet",
    "1jet_low",
    "1jet_high",
    #"1jet",
    "btag_low",
    "btag_high",
    #"nobtag",
    #"btag",
    ] 

extra = {
    "ee"      : "ee",
    "emu"     : "e#mu",
    "eleTau"  : "e#tau_{h}",
    "muTau"   : "#mu#tau_{h}",
    "mumu"    : "#mu#mu",
    }

log = {
    ("emu"    , "0jet_low"  ) : ["false",],
    ("emu"    , "0jet_high" ) : ["false",],
    ("emu"    , "0jet"      ) : ["false",],
    ("emu"    , "1jet_low"  ) : ["false",],
    ("emu"    , "1jet_high" ) : ["false",],
    ("emu"    , "1jet"      ) : ["false",],
    ("emu"    , "btag_low"  ) : ["false",],
    ("emu"    , "btag_high" ) : ["false",],
    ("emu"    , "nobtag"    ) : ["false", "true"],
    ("emu"    , "btag"      ) : ["false", "true"],
    ("emu"    , "vbf"       ) : ["false",],
    ("muTau"  , "0jet_low"  ) : ["false",],
    ("muTau"  , "0jet_high" ) : ["false",],
    ("muTau"  , "0jet"      ) : ["false",],
    ("muTau"  , "1jet_low"  ) : ["false",],
    ("muTau"  , "1jet_high" ) : ["false",],
    ("muTau"  , "1jet"      ) : ["false",],
    ("muTau"  , "btag_low"  ) : ["false",],
    ("muTau"  , "btag_high" ) : ["false",],
    ("muTau"  , "nobtag"    ) : ["false", "true"],
    ("muTau"  , "btag"      ) : ["false", "true"],
    ("muTau"  , "vbf"       ) : ["false",],
    ("eleTau" , "0jet_low"  ) : ["false",],
    ("eleTau" , "0jet_high" ) : ["false",],
    ("eleTau" , "0jet"      ) : ["false",],
    ("eleTau" , "1jet_low"  ) : ["false",],
    ("eleTau" , "1jet_high" ) : ["false",],
    ("eleTau" , "1jet"      ) : ["false",],
    ("eleTau" , "btag_low"  ) : ["false",],
    ("eleTau" , "btag_high" ) : ["false",],
    ("eleTau" , "nobtag"    ) : ["false", "true"],
    ("eleTau" , "btag"      ) : ["false", "true"],
    ("eleTau" , "vbf"       ) : ["false",],
    ("mumu"   , "0jet_low"  ) : ["false", ],
    ("mumu"   , "0jet_high" ) : ["false", ],
    ("mumu"   , "0jet"      ) : ["false", ],
    ("mumu"   , "1jet_low"  ) : ["false", ],
    ("mumu"   , "1jet_high" ) : ["false", ],
    ("mumu"   , "1jet"      ) : ["false", ],
    ("mumu"   , "btag_low"  ) : ["false", ],
    ("mumu"   , "btag_high" ) : ["false", ],
    ("mumu"   , "nobtag"    ) : ["false", "true"],
    ("mumu"   , "btag"      ) : ["false", "true"],
    ("mumu"   , "vbf"       ) : ["false",],
    }

max = {
    ("emu"    , "0jet_low"  ) : ["-1",],
    ("emu"    , "0jet_high" ) : ["-1",],
    ("emu"    , "0jet"      ) : ["-1",],
    ("emu"    , "1jet_low"  ) : ["-1",],
    ("emu"    , "1jet_high" ) : ["-1",],
    ("emu"    , "1jet"      ) : ["-1",],
    ("emu"    , "btag_low"  ) : ["-1",],
    ("emu"    , "btag_high" ) : ["-1",],
    ("emu"    , "nobtag"    ) : ["-1",  "-1"], #["3000","2500"],
    ("emu"    , "btag"      ) : ["-1",  "-1"], #["40","45"],
    ("emu"    , "vbf"       ) : ["3.0",], ## temporary fit 24.01.2013
    ("muTau"  , "0jet_low"  ) : ["-1",],
    ("muTau"  , "0jet_high" ) : ["-1",],
    ("muTau"  , "0jet"      ) : ["-1",],
    ("muTau"  , "1jet_low"  ) : ["-1",],
    ("muTau"  , "1jet_high" ) : ["-1",],
    ("muTau"  , "1jet"      ) : ["-1",],
    ("muTau"  , "btag_low"  ) : ["-1",],
    ("muTau"  , "btag_high" ) : ["-1",],
    ("muTau"  , "nobtag"    ) : ["-1",  "-1"], #["8000","5000"],
    ("muTau"  , "btag"      ) : ["-1",  "-1"], #["100","50"],
    ("muTau"  , "vbf"       ) : ["-1",],
    ("eleTau" , "0jet_low"  ) : ["-1",],
    ("eleTau" , "0jet_high" ) : ["-1",],
    ("eleTau" , "0jet"      ) : ["-1",],
    ("eleTau" , "1jet_low"  ) : ["-1",],
    ("eleTau" , "1jet_high" ) : ["-1",],
    ("eleTau" , "1jet"      ) : ["-1",],
    ("eleTau" , "btag_low"  ) : ["-1",],
    ("eleTau" , "btag_high" ) : ["-1",],
    ("eleTau" , "nobtag"    ) : ["-1",  "-1"], #["2000","1500"],
    ("eleTau" , "btag"      ) : ["-1",  "-1"], #["20","20"],
    ("eleTau" , "vbf"       ) : ["-1",],
    ("mumu"   , "0jet_low"  ) : ["-1",],
    ("mumu"   , "0jet_high" ) : ["-1",],
    ("mumu"   , "0jet"      ) : ["-1",],
    ("mumu"   , "1jet_low"  ) : ["-1",],
    ("mumu"   , "1jet_high" ) : ["-1",],
    ("mumu"   , "1jet"      ) : ["-1",],
    ("mumu"   , "btag_low"  ) : ["-1",],
    ("mumu"   , "btag_high" ) : ["-1",],
    ("mumu"   , "nobtag"    ) : ["-1",  "-1"], #["200000","120000"],
    ("mumu"   , "btag"      ) : ["-1",  "-1"], #["500","300"],
    ("mumu"   , "vbf"       ) : ["-1",],
    }

min = {
    ("emu"    , "0jet_low"  ) : ["0",  ],
    ("emu"    , "0jet_high" ) : ["0",  ],
    ("emu"    , "0jet"      ) : ["0",  ],
    ("emu"    , "1jet_low"  ) : ["0",  ],
    ("emu"    , "1jet_high" ) : ["0",  ],
    ("emu"    , "1jet"      ) : ["0",  ],
    ("emu"    , "btag_low"  ) : ["0",  ],
    ("emu"    , "btag_high" ) : ["0",  ],
    ("emu"    , "nobtag"    ) : ["0", "1e-1"],
    ("emu"    , "btag"      ) : ["0", "1e-1"],
    ("emu"    , "vbf"       ) : ["0",  ],
    ("muTau"  , "0jet_low"  ) : ["0",  ],
    ("muTau"  , "0jet_high" ) : ["0",  ],
    ("muTau"  , "0jet"      ) : ["0",  ],
    ("muTau"  , "1jet_low"  ) : ["0",  ],
    ("muTau"  , "1jet_high" ) : ["0",  ],
    ("muTau"  , "1jet"      ) : ["0",  ],
    ("muTau"  , "btag_low"  ) : ["0",  ],
    ("muTau"  , "btag_high" ) : ["0",  ],
    ("muTau"  , "nobtag"    ) : ["0", "1e-2"],
    ("muTau"  , "btag"      ) : ["0", "1e-2"],
    ("muTau"  , "vbf"       ) : ["0",  ],
    ("eleTau" , "0jet_low"  ) : ["0",  ],
    ("eleTau" , "0jet_high" ) : ["0",  ],
    ("eleTau" , "0jet"      ) : ["0",  ],
    ("eleTau" , "1jet_low"  ) : ["0",  ],
    ("eleTau" , "1jet_high" ) : ["0",  ],
    ("eleTau" , "1jet"      ) : ["0",  ],
    ("eleTau" , "btag_low"  ) : ["0",  ],
    ("eleTau" , "btag_high" ) : ["0",  ],
    ("eleTau" , "nobtag"    ) : ["0", "1e-2"],
    ("eleTau" , "btag"      ) : ["0", "1e-2"],
    ("eleTau" , "vbf"       ) : ["0",  ],
    ("mumu"   , "0jet_low"  ) : ["0",  ],
    ("mumu"   , "0jet_high" ) : ["0",  ],
    ("mumu"   , "0jet"      ) : ["0",  ],
    ("mumu"   , "1jet_low"  ) : ["0",  ],
    ("mumu"   , "1jet_high" ) : ["0",  ],
    ("mumu"   , "1jet"      ) : ["0",  ],
    ("mumu"   , "btag_low"  ) : ["0",  ],
    ("mumu"   , "btag_high" ) : ["0",  ],
    ("mumu"   , "nobtag"    ) : ["0", "1e-2"],
    ("mumu"   , "btag"      ) : ["0", "1e-1"],
    ("mumu"   , "vbf"       ) : ["0",  ],  
    }

import os

type = options.type
categories = categories_sm if options.analysis == "sm" else categories_mssm

print "C R E A T I N G   S U M M A R Y   P L O T S :"
print "CATEGORIES:", categories
print "CHANNELS  :", channels

## combine 2011+2012
for chn in channels :
    for cat in categories :
        ## combine high and low pt categories, make sure in your 
        ## list that {CAT}_low and {CAT}_high are run beforehand
        if cat == "0jet" : ## or cat == "1jet" : ## in 1jet low and high pt have a different binning
            #print "hadd {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_low_{TYPE}_7+8TeV.root {CHN}_{CAT}_high_{TYPE}_7+8TeV.root".format(CHN=chn, CAT=cat, TYPE=type)
            os.system("hadd -f {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_low_{TYPE}_7+8TeV.root {CHN}_{CAT}_high_{TYPE}_7+8TeV.root".format(CHN=chn, CAT=cat, TYPE=type))
        else :
            #print "hadd {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_{TYPE}_7TeV_{LOG}.root {CHN}_{CAT}_{TYPE}_8TeV_{LOG}.root".format(
            #    CHN=chn, CAT=cat, TYPE=type, LOG="LOG" if log[(chn, cat)] else "")
            os.system("hadd -f {CHN}_{CAT}_{TYPE}_7+8TeV.root {CHN}_{CAT}_{TYPE}_7TeV_.root {CHN}_{CAT}_{TYPE}_8TeV_.root".format(
                CHN=chn, CAT=cat, TYPE=type))#, LOG="LOG" if log[(chn, cat)]==True else ""))
            if options.analysis == "mssm" :
                os.system("hadd -f {CHN}_{CAT}_{TYPE}_7+8TeV_LOG.root {CHN}_{CAT}_{TYPE}_7TeV_LOG.root {CHN}_{CAT}_{TYPE}_8TeV_LOG.root".format(
                    CHN=chn, CAT=cat, TYPE=type))#, LOG="LOG" if log[(chn, cat)]==True else ""))

##print in the right Signal label for MSSM
postfit_base = open("{CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit.C".format(CMSSW_BASE=os.environ['CMSSW_BASE']),'r')
postfit_use  = open("{CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit_use.C".format(CMSSW_BASE=os.environ['CMSSW_BASE']),'w')
for line in postfit_base :
    line = line.replace("$CMSSW_BASE", os.environ['CMSSW_BASE'])
    line = line.replace("$MA" , str(int(options.mA)))
    line = line.replace("$TANB", str(int(options.tanb)))
    postfit_use.write(line)
postfit_base.close()
postfit_use.close()
                
## make plots
for chn in channels :
    for cat in categories :
        print chn, cat
        os.system("root -l -q -b {CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit_use.C+\\(\\\"{CHN}_{CAT}_{TYPE}_7+8TeV.root\\\",\\\"{ANA}\\\",\\\"{LABEL}\\\",\\\"{EXTRA}\\\",\\\"{EXTRA2}\\\",{MIN},{MAX},{LOG}\)".format(
            CMSSW_BASE=os.environ['CMSSW_BASE'],
            CHN=chn,
            CAT=cat,
            TYPE=type,
            ANA=options.analysis.upper(),
            LABEL="2011+2012",
            EXTRA=extra[chn],
            EXTRA2=cat,
            MIN=min[chn,cat][0],
            MAX=max[chn,cat][0],
            LOG=log[chn,cat][0]
            ))
        if options.analysis == "mssm" :
            os.system("root -l -q -b {CMSSW_BASE}/src/HiggsAnalysis/HiggsToTauTau/macros/postfit_use.C+\\(\\\"{CHN}_{CAT}_{TYPE}_7+8TeV_LOG.root\\\",\\\"{ANA}\\\",\\\"{LABEL}\\\",\\\"{EXTRA}\\\",\\\"{EXTRA2}\\\",{MIN},{MAX},{LOG}\)".format(
                CMSSW_BASE=os.environ['CMSSW_BASE'],
                CHN=chn,
                CAT=cat,
                TYPE=type,
                ANA=options.analysis.upper(),
                LABEL="2011+2012",
                EXTRA=extra[chn],
                EXTRA2=cat,
                MIN=min[chn,cat][1],
                MAX=max[chn,cat][1],
                LOG=log[chn,cat][1]
                ))
