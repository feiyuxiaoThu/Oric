traj = nlread('device_out_1.nc', Trajectory)[0]
number_of_steps = len(traj)
z_coordinates = []

for i in range(number_of_steps):
    coordinates = traj.image(i).cartesianCoordinates().inUnitsOf(Angstrom)
    # Append all z-coordinates, apart from the fixed bottom layer.
    z_coordinates.append(coordinates[:16, 2].tolist())

# Convert to numpy array.
z_coordinates = numpy.array(z_coordinates)
# Plot the z-coordinates using pylab.
import pylab

pylab.figure()
# Loop over all unconstrained atoms.
for i in range(16):
    pylab.plot(range(number_of_steps), z_coordinates[:, i], '--*')
pylab.xlabel('Optimization step')
pylab.ylabel('Z-coordinates (Ang)')
pylab.grid(True)

pylab.show()