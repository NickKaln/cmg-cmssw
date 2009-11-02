import FWCore.ParameterSet.Config as cms


from DQMOffline.PFTau.pfCandidateManager_cfi import pfCandidateManager


# could create one benchmark / particle type

pfCandidateBenchmarkSequence = cms.Sequence(
    pfCandidateManager
    )
