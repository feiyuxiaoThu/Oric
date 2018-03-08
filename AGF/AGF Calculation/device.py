def getCalculator(kpts):
    # -------------------------------------------------------------
    # Calculator
    # -------------------------------------------------------------
    potentialSet = StillingerWeber_Si_1985()
    calculator = TremoloXCalculator(parameters=potentialSet)

    return calculator


from optimize import RunOptimizer
# -------------------------------------------------------------
# Main Settings 
# -------------------------------------------------------------
nc1   = 'device_in.nc'    # input device configuration
nc2   = 'device_out.nc'   # output for device relaxations
txt   = 'device.txt'      # text-file with potential-energy curve
dx    = -0.25         # first step by the optimizer (Angstrom)
tol   = 0.25          # tolerance for stopping the optimizer (Angstrom)
kpts  = None          # no k-points are needed for ATK-Classical calculations
force = 0.001         # maximum force criterion in geometry relaxations
plot  = True          # automatic plotting of the results only work when the job is run in serial!
opt = RunOptimizer(nc1, nc2, txt, dx, tol, kpts, force, getCalculator, None, plot)
device = opt.run()