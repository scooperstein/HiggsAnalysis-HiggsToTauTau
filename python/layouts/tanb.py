import FWCore.ParameterSet.Config as cms

layout = cms.PSet(
    ## dataset
    dataset = cms.string("CMS Preliminary,  H#rightarrow#tau#tau,  4.9 fb^{-1} at 7 TeV, 19.4 fb^{-1} at 8 TeV"),
    ## x-axis title
    xaxis = cms.string("m_{A} [GeV]"),
    ## x-axis title
    yaxis = cms.string("#bf{tan#beta}"),
    ## min for plotting
    min = cms.double(0.),
    ## max for plotting
    max = cms.double(50.),
    ## min for plotting
    log = cms.int32(0),
    ## print to png
    png = cms.bool(True),
    ## print to pdf
    pdf = cms.bool(True),
    ## print to txt
    txt = cms.bool(True),
    ## print to root
    root = cms.bool(True),
    ## define verbosity level
    verbosity = cms.uint32(0),
    ## define output label
    outputLabel = cms.string("mA-tanb"),
    ## define masspoints for limit plot
    masspoints = cms.vdouble(
     90.
   ,100.
   ,120.
   ,130.
   ,140.
   ,160.
   ,180.
   ,200.
   ,250.  
   ,300.
   ,350.
   ,400.
   ,450.
   ,500.
   ,600.
   ,700.
   ,800.
   #,900.
   #,1000.
     ),
    ## is this mssm?
    mssm = cms.bool(True),
    ## print the 2-sigma band
    outerband = cms.bool(True),
    ## plot expected only
    #expectedOnly = cms.bool(True),
    ## print constraints from mH=125GeV
    higgs125 = cms.bool(False),

)
