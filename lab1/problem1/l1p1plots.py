import numpy as npimport matplotlib.pyplot as pltfilenameReptran = "vertTransReptranFine.out"filenameLowtran = "vertTransLowtran.out"dataReptran = np.loadtxt(filenameReptran)dataLowtran = np.loadtxt(filenameLowtran)dataReptran[:,0] = dataReptran[:,0] * 10**-3 #convert nm -> umdataLowtran[:,0] = dataLowtran[:,0] * 10**-3 #convert nm -> umfig = plt.figure(figsize=(7,5))ax = fig.add_subplot(1, 1, 1)plt.plot(dataLowtran[:,0], dataLowtran[:,1], label='Direct')# plt.plot(dataLowtran[:,0], dataLowtran[:,2], label='Global')plt.legend()plt.xlabel(r"Wavelength ($\mu$m)")plt.ylabel('Transmittance')plt.title('Transmittance Lowtran\nSource: solar, rte_solver: disort, effects from aerosols')plt.tight_layout()fmt = "png"plt.savefig("vertTransLowtran." + fmt, format=fmt, bbox_inches='tight')plt.show(block=False)fig = plt.figure(figsize=(7,5))ax = fig.add_subplot(1, 1, 1)plt.plot(dataReptran[:,0], dataReptran[:,1], label='Direct')# plt.plot(dataReptran[:,0], dataReptran[:,2], label='Global')plt.legend()plt.xlabel(r"Wavelength ($\mu$m)")plt.ylabel('Transmittance')plt.title('Transmittance Reptran (fine)\nSource: solar, rte_solver: disort, effects from aerosols')plt.tight_layout()fmt = "png"plt.savefig("vertTransReptranFine." + fmt, format=fmt, bbox_inches='tight')plt.show(block=False)