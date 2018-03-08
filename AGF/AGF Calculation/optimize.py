from NanoLanguage import nlread, nlprint, nlsave
from NanoLanguage import eV, Angstrom, UnitCell, BulkConfiguration, DeviceConfiguration
from NanoLanguage import TotalEnergy, OptimizeGeometry, LBFGS
from NL.ComputerScienceUtilities.Exceptions import NLValueError
from NLEngine import myRank

import numpy
import os


def adjustDevice(device_configuration,
                 length,
                 left_atoms=[],
                 right_atoms=[]):
    """
    Routine for extending or extracting the central region of a device.
    """
    # Get the new central cell.
    u1, u2, u3 = device_configuration.bravaisLattice().primitiveVectors()
    z = u3[2].inUnitsOf(Angstrom)

    # Get the required displacement.
    tmp_length = length.inUnitsOf(Angstrom)
    tmp_displacement = tmp_length - z

    # Get the length of the left and right electrode.
    N1 = len(device_configuration.electrodes()[0])
    N2 = len(device_configuration.electrodes()[1])

    # Determine the path of the system that should be shifted
    # by the fixed displacement.
    fixed_move = range(len(device_configuration))[-N2:]
    fixed_move = list(set(fixed_move + right_atoms))

    # Determine of the path of system that should be constrainted.
    no_move = range(N1)
    no_move = list(set(no_move + left_atoms))

    # Scaled movement.
    scaled_move = set(range(len(device_configuration)))
    scaled_move = scaled_move.difference(fixed_move)
    scaled_move = list(scaled_move.difference(no_move))

    # Calculate the new third lattice vector for the third cell.
    v3 = u3 + [0.0, 0.0, tmp_displacement]*Angstrom
    # Create new cell.
    new_cell = UnitCell(u1, u2, v3)

    # Get all the new coordinates.
    xyz = numpy.array(device_configuration.cartesianCoordinates().inUnitsOf(Angstrom))
    for index in fixed_move:
        xyz[index] += numpy.array([0.0, 0.0, tmp_displacement])

    # Get the scale factor.
    scale_factor = (v3[2].inUnitsOf(Angstrom)/u3[2].inUnitsOf(Angstrom) - 1)

    # Scaled move.
    for index in scaled_move:
        xyz[index] += numpy.array([0.0, 0.0, xyz[index][2]*scale_factor])

    # Collect into a new central region.
    new_central_region = BulkConfiguration(new_cell,
                                           elements=device_configuration.elements(),
                                           cartesian_coordinates=xyz*Angstrom)
    # Collect a new device configuration.
    new_device_configuration = DeviceConfiguration(new_central_region, device_configuration.electrodes())

    # Transfer the calculator is such exist.
    if device_configuration.calculator() is not None:
        # Set it.
        new_device_configuration.setCalculator(device_configuration.calculator(), initial_state=device_configuration)
        # Remove the initial state for the central region.
        new_device_configuration._initial_state = None

    # Return the new device configuration.
    return new_device_configuration

def readDeviceConfiguration(nc):
    """
    Reads and returns a device_configuration from nc-file. 
    """    
    if not os.path.isfile(nc):
        raise NLValueError('nc file %s not found!' % nc)
    device = nlread(nc, DeviceConfiguration)[-1]
    nlprint(device)

    return device

def doRelax(device, nc, force):
    """
    Performs relaxation of internal coordinates using forces only,
    and returns the final device and total energy
    """    
    # -------------------------------------------------------------
    # Geometry Optimization
    # -------------------------------------------------------------
    max_forces = force # eV/Ang
    device = OptimizeGeometry(
        device,
        max_forces=max_forces,
        disable_stress=True,
        trajectory_filename=nc,
        optimizer_method=LBFGS())
    
    # -------------------------------------------------------------
    # Total energy
    # -------------------------------------------------------------
    total_energy = TotalEnergy(device)
    nlsave(nc, total_energy)
    nlprint(total_energy)
    e = total_energy.evaluate().inUnitsOf(eV)

    return device, e


class OptimizeDevice():
    """
    Class for performing the 1DMIN device optimization.
    """    
    def __init__(self, total_energy, x0, dx, tol, plot):
        self.total_energy = total_energy
        self.x0 = x0
        self.dx = dx
        self.tol = tol
        self.plot = plot
        self.xtol = tol/x0
        self.xhist = numpy.array([])
        self.yhist = numpy.array([])
        self.n_calculated = 0
        self.n_reused = 0
        self.conv = False

    def write(self, message):
        """
        Print to stdout, also during parallel execution.
        """    
        if myRank() == 0:
            print message

    def doClosePoints(self):
        """
        Get total energies immediately around the optimum.
        """    
        for k in [-1, 0, 1]:
            x = self.res.x + k*self.tol
            xarr = abs(self.xhist - x)
            args = numpy.where(xarr < self.tol*0.1)[0]
            if len(args) > 0:
                a = args[0]
                x = self.xhist[a]           
            self.f(x)

    def evaluate(self):
        """
        Evaluate if we are sufficiently confident in the position of a minimum.
        """    
        self.doClosePoints()
        self.fitx = self.xhist[-3:]
        self.fity = self.yhist[-3:]
        fit0 = numpy.polyfit(self.fitx, self.fity, 2)
        self.ran  = numpy.linspace(min(self.fitx), max(self.fitx), 100)
        self.vals = numpy.polyval(fit0, self.ran)
        fit1 = numpy.polyder(fit0, 1)
        z = numpy.roots(fit1)
        if not len(z) == 1:
            raise NLValueError("Error in polynomial fit.")
        self.xopt = z[0]
        self.fopt = numpy.polyval(fit0, self.xopt)
        # are we converged?
        ok1 = self.fitx[-3] < self.xopt
        ok2 = self.fitx[-1] > self.xopt
        if ok1 and ok2:
            # yes
            self.conv = True
        else:
            # no: random pertubation from current xopt
            self.x0 = self.xopt + self.dx*numpy.random.randn()

    def f(self, x):
        """
        Objective function that is minimized by SciPy.
        """
        old = numpy.where(self.xhist==x)[0]
        if len(old) > 0:
            y = self.yhist[old[0]]
            self.n_reused += 1
        else:
            y = self.total_energy(x)
            self.n_calculated += 1
        self.write("%.8f %.8f" % (x,y))
        self.xhist = numpy.append(self.xhist, x)
        self.yhist = numpy.append(self.yhist, y)
        return y

    def run(self):
        """
        Run the optimization.
        """
        from scipy.optimize import minimize_scalar
        while not self.conv:
            bracket = [self.x0, self.x0 + self.dx]
            self.res = minimize_scalar(self.f, bracket=bracket, options={'xtol':self.xtol, 'maxiter':50})
            self.error = abs((self.xhist[-1]-self.xhist[-2])/self.xhist[-2])
            # optimization results
            self.evaluate()
        return self.xopt

    def report(self):
        """
        Print optimization report to stdout.
        """
        self.write("")
        self.write("+----------------------------------------------------------+")
        self.write("| Device geometry optimization report                      |")
        self.write("+----------------------------------------------------------+")
        self.write("Tolerance:           %.5f Ang" % self.tol)
        self.write("Calculations done:   %i" % self.n_calculated)
        self.write("Calculations reused: %i" % self.n_reused)
        self.write("xtol = %.2e" % self.xtol)
        self.write("xopt = %.5f Ang" % self.xopt)
        self.write("Eopt = %.5e eV" % self.fopt)
        if self.plot:
            import pylab
            pylab.plot(self.xhist, self.yhist, 'o-', color='b')
            pylab.plot(self.ran, self.vals, '--', color='b')
            pylab.plot(self.xopt, self.fopt, 'o', color='r')
            pylab.xlabel('Center region cell length (Ang)')
            pylab.ylabel('Total energy (eV)')
            pylab.show()


class RunOptimizer():
    """
    Class for running the 1DMIN device optimization given the provided
    getCalculator function and optionally the setInitialState function.
    """    
    def __init__(self, nc1, nc2, txt, dx, tol, kpts, force, getCalculator, setInitialState=None, plot=False):
        self.nc1 = nc1
        self.nc2 = nc2
        self.txtfile = None
        if myRank() == 0:
            self.txtfile = open(txt, 'w')
        self.dx = dx
        self.tol = tol
        self.force = force*eV/Angstrom
        self.getCalculator = getCalculator
        self.setInitialState = setInitialState
        self.plot = plot

        self.device_configuration = readDeviceConfiguration(self.nc1)
        self.left = self.device_configuration.indicesFromTags('Left')
        self.right = self.device_configuration.indicesFromTags('Right')
        calculator = self.getCalculator(kpts)
        self.device_configuration.setCalculator(calculator)
        if self.setInitialState is not None:
            self.device_configuration = self.setInitialState(self.device_configuration, calculator)
        self.x0 = self.getCentralRegionLength()

    def getCentralRegionLength(self):
        """
        Returns the central region unit cell length (C). 
        """
        z = self.device_configuration.bravaisLattice().primitiveVectors()[2,2]
        return z.inUnitsOf(Angstrom)

    def totalEnergy(self, x, final=False):
        """
        Relax device at central cell length x.
        """
        x *= Angstrom
        force = self.force
        if final:
            force = self.force / 2.0
        self.device_configuration = adjustDevice(self.device_configuration,
                                                 x, self.left, self.right)
        self.device_configuration, e = doRelax(self.device_configuration,
                                               self.nc2, force)
        nlsave(self.nc2, self.device_configuration)
        nlprint(self.device_configuration)

        if myRank() == 0:
            print >> self.txtfile, '%.8f %.8f' % (x, e)
            self.txtfile.flush()
        return e

    def run(self):
        """
        Setup optimization, run it, and relax at the optimum geometry.
        """
        opt = OptimizeDevice(self.totalEnergy, self.x0, self.dx, self.tol, self.plot)
        xopt = opt.run()
        self.totalEnergy(xopt, True)
        opt.report()
        return self.device_configuration