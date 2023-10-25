from sphericalHarmonicDecomposition import SHD

sph = SHD(name="lipids",
          Lmin=2,Lmax=10,
          expansionMode="abs",
          radiusMode="expansion")

sph.loadSPtraj("lipids.sp")

sph.generateIcosahedralGrid(2)
sph.distributeTrajPointsAlongGrid()

sph.sphericalHarmonicExpansion()
b,k = sph.compute()

print("b = ",b)
print("k = ",k)
