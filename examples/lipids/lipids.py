from ..sphericalHarmonicsDecomposition import SHD

sph = SHD(name="lipids",
          Lmin=2,Lmax=10,debug=True)

sph.loadSPtraj("lipids.sp")

sph.generateIcosahedralGrid(2)
sph.distributeTrajPointsAlongGrid()

sph.sphericalHarmonicExpansion()
sph.compute()
