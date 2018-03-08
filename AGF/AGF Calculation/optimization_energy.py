traj = nlread('device_out_1.nc', Trajectory)[0]
energies = []
max_forces = []
for i in range(len(traj)):
    energies.append(traj.imageEnergy(i).inUnitsOf(eV))
    forces = traj.imageForces(i).inUnitsOf(eV/Angstrom)
    force_magnitude = (forces**2).sum(axis=1)**0.5
    max_forces.append(numpy.max(forces))

# Plot the energy and max. force curve using pylab.
import pylab

pylab.figure()
pylab.subplot(2, 1, 1)
pylab.plot(range(len(traj)), energies)
pylab.xlabel('Optimization step')
pylab.ylabel('Energy (eV)')
pylab.grid(True)

pylab.subplot(2, 1, 2)
pylab.plot(range(len(traj)), max_forces)
pylab.xlabel('Optimization step')
pylab.ylabel('Maximum Forces (eV/Ang)')
pylab.grid(True)

pylab.show()