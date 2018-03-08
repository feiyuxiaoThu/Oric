# Read the phonon transmission spectrum from file cnt_phonons.nc
phonon_transmission_spectrum = nlread("cnt_phonons.nc",PhononTransmissionSpectrum)[0]
# Define a temperature range
temp = numpy.linspace(10,2000,21)
# Calculate the phonon thermal conductance at each temperature 
conductances = []
for t in temp:
    conductance = phonon_transmission_spectrum.thermalConductance(
        phonon_temperature=[t]*Kelvin)
    conductance = conductance*10**9
    conductances.append(conductance)

# Now read the phonon transmission spectrum from file cntc14_phonons.nc ...
phonon_transmission_spectrum_c14 = nlread("cntc14_phonons.nc",PhononTransmissionSpectrum)[0]
# ... and calculate the relative phonon thermal conductance
conductances_c14 = []
for t in temp:
    conductance_c14 = phonon_transmission_spectrum_c14.thermalConductance(
        phonon_temperature=[t]*Kelvin)
    conductance_c14 = conductance_c14*10**9
    conductances_c14.append(conductance_c14)

# Plot the phonon thermal conductances as function of temperature
import pylab
pylab.figure()
pylab.plot(temp,conductances,label='CNT',linewidth=2.0)
pylab.plot(temp,conductances_c14,label='14C-CNT',linewidth=2.0)
pylab.xlabel("Temperature (K)")
pylab.ylabel("Phonon Thermal Conductance (nW/K)")
pylab.legend(loc="lower right")
pylab.show()