def getCalculator(kpts):
    # -------------------------------------------------------------
    # Calculator
    # -------------------------------------------------------------
	potentialSet = TremoloXPotentialSet(name = 'Tersoff_Powell_2007')
	potentialSet.addParticleType(ParticleType(
		symbol='Al', 
		mass=26.9815 * atomic_mass_unit, 
		charge=None, 
		sigma=None, 
		sigma14=None, 
		epsilon=None, 
		epsilon14=None, 
		atomicNumber=13
	))
	potentialSet.addParticleType(ParticleType(
		symbol='N', 
		mass=14.0067 * atomic_mass_unit,
		charge=None, 
		sigma=None, 
		sigma14=None, 
		epsilon=None, 
		epsilon14=None,
		atomicNumber=7
	))
	potentialSet.addParticleType(ParticleType(
		symbol='P',
		mass=30.9738 * atomic_mass_unit, 
		charge=None,
		sigma=None, 
		sigma14=None, 
		epsilon=None, 
		epsilon14=None,
		atomicNumber=15
	))
	potentialSet.addParticleType(ParticleType(
		symbol='As', 
		mass=74.9216 * atomic_mass_unit, 
		charge=None, 
		sigma=None, 
		sigma14=None,
		epsilon=None, 
		epsilon14=None, 
		atomicNumber=33
	))
	potentialSet.addParticleType(ParticleType(
		symbol='Ga', 
		mass=69.723 * atomic_mass_unit,
		charge=None, 
		sigma=None, 
		sigma14=None, 
		epsilon=None, 
		epsilon14=None,
		atomicNumber=31))
	potentialSet.addParticleType(ParticleType(
		symbol='In', 
		mass=114.818 * atomic_mass_unit,
		charge=None,
		sigma=None, 
		sigma14=None, 
		epsilon=None,
		epsilon14=None,
		atomicNumber=49
	))
	potentialSet.addParticleType(ParticleType(
		symbol='Sb', 
		mass=121.76 * atomic_mass_unit,
		charge=None,
		sigma=None, 
		sigma14=None,
		epsilon=None, 
		epsilon14=None,
		atomicNumber=51
	))


	potential = TersoffSingleTypePotential(
		particleType = 'Al', 
		A = 0.0*eV, 
		B = 0.0*eV, 
		R = 0.0*Angstrom,
		S = 0.0*Angstrom,
		l = 0.0*1/Angstrom,
		mu = 0.0*1/Angstrom, 
		alpha = 0.0*1/Angstrom,
		beta = 1.0, 
		omega = 0.0, 
		chi = 1.0, 
		chiR = 1.0,
		m = 0, 
		n = 1.0,
		c = 0.0,
		d = 1, 
		h = 0.0
	)
	potentialSet.addPotential(potential)
	potential = TersoffSingleTypePotential(
		particleType = 'N',
		A = 0.0*eV, 
		B = 0.0*eV, 
		R = 0.0*Angstrom,
		S = 0.0*Angstrom,
		l = 0.0*1/Angstrom,
		mu = 0.0*1/Angstrom, 
		alpha = 0.0*1/Angstrom, 
		beta = 1.0,
		omega = 0.0,
		chi = 1.0, 
		chiR = 1.0,
		m = 0, 
		n = 1.0,
		c = 0.0,
		d = 1,
		h = 0.0
	)
	potentialSet.addPotential(potential)
	potential = TersoffSingleTypePotential(
		particleType = 'P', 
		A = 0.0*eV,
		B = 0.0*eV,
		R = 0.0*Angstrom,
		S = 0.0*Angstrom,
		l = 0.0*1/Angstrom,
		mu = 0.0*1/Angstrom,
		alpha = 0.0*1/Angstrom,
		beta = 1.0, 
		omega = 0.0,
		chi = 1.0, 
		chiR = 1.0,
		m = 0, 
		n = 1.0,
		c = 0.0, 
		d = 1,
		h = 0.0
	)
	potentialSet.addPotential(potential)
	potential = TersoffSingleTypePotential(
		particleType = 'As',
		A = 0.0*eV, 
		B = 0.0*eV,
		R = 0.0*Angstrom,
		S = 0.0*Angstrom, 
		l = 0.0*1/Angstrom,
		mu = 0.0*1/Angstrom,
		alpha = 0.0*1/Angstrom,
		beta = 1.0, 
		omega = 0.0,
		chi = 1.0,
		chiR = 1.0,
		m = 0, 
		n = 1.0,
		c = 0.0, 
		d = 1,
		h = 0.0
	)
	potentialSet.addPotential(potential)
	potential = TersoffSingleTypePotential(
		particleType = 'Ga'
		, A = 0.0*eV, 
		B = 0.0*eV,
		R = 0.0*Angstrom, 
		S = 0.0*Angstrom, 
		l = 0.0*1/Angstrom,
		mu = 0.0*1/Angstrom,
		alpha = 0.0*1/Angstrom,
		beta = 1.0, 
		omega = 0.0, 
		chi = 1.0, 
		chiR = 1.0, 
		m = 0,
		n = 1.0,
		c = 0.0, 
		d = 1, 
		h = 0.0
	)
	potentialSet.addPotential(potential)
	potential = TersoffSingleTypePotential(
		particleType = 'In',
		A = 0.0*eV,
		B = 0.0*eV, 
		R = 0.0*Angstrom,
		S = 0.0*Angstrom,
		l = 0.0*1/Angstrom,
		mu = 0.0*1/Angstrom,
		alpha = 0.0*1/Angstrom,
		beta = 1.0, 
		omega = 0.0, 
		chi = 1.0, 
		chiR = 1.0,
		m = 0, 
		n = 1.0,
		c = 0.0,
		d = 1,
		h = 0.0
	)
	potentialSet.addPotential(potential)
	potential = TersoffSingleTypePotential(
		particleType = 'Sb', 
		A = 0.0*eV,
		B = 0.0*eV,
		R = 0.0*Angstrom,
		S = 0.0*Angstrom,
		l = 0.0*1/Angstrom,
		mu = 0.0*1/Angstrom,
		alpha = 0.0*1/Angstrom,
		beta = 1.0,
		omega = 0.0, 
		chi = 1.0,
		chiR = 1.0, 
		m = 0, 
		n = 1.0,
		c = 0.0,
		d = 1, 
		h = 0.0
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'Ga',
		particleType2 = 'As',
		A = 446079.331668*eV,
		B = 16.0304697869*eV, 
		R = 3.4*Angstrom, 
		S = 3.6*Angstrom,
		l = 5.84464068024*1/Angstrom,
		mu = 0.839717061922*1/Angstrom,
		alpha = 0.244341*1/Angstrom,
		beta = 0.257183, 
		omega = 1.0, 
		chi = 1.0, 
		chiR = 1.0, 
		m = 3, 
		n = 3.55586,
		c = 2.16345,
		d = 0.750147,
		h = -0.448899
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'In',
		particleType2 = 'As',
		A = 2866.66092152*eV, 
		B = 809.217955972*eV, 
		R = 3.6*Angstrom,
		S = 3.8*Angstrom, 
		l = 2.44216741807*1/Angstrom,
		mu = 1.83960484959*1/Angstrom,
		alpha = 0.140874*1/Angstrom,
		beta = 0.139688, 
		omega = 1.0,
		chi = 1.0, 
		chiR = 1.0,
		m = 3, 
		n = 2.35072,
		c = 2.10031, 
		d = 0.827636,
		h = -0.442115
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'Al', 
		particleType2 = 'As',
		A = 1780.77119387*eV,
		B = 330.992213383*eV,
		R = 3.6*Angstrom, 
		S = 3.8*Angstrom,
		l = 2.54310038714*1/Angstrom,
		mu = 1.64996035006*1/Angstrom, 
		alpha = 1.38402*1/Angstrom,
		beta = 0.359702, 
		omega = 1.0, 
		chi = 1.0,
		chiR = 1.0,
		m = 3, 
		n = 8.36992,
		c = 1.05025,
		d = 0.850097,
		h = -0.458041
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'Ga',
		particleType2 = 'P', 
		A = 2806.02777654*eV,
		B = 378.063510794*eV,
		R = 3.0*Angstrom, 
		S = 3.2*Angstrom, 
		l = 2.89912244184*1/Angstrom,
		mu = 1.81864641828*1/Angstrom,
		alpha = 1.81771*1/Angstrom,
		beta = 0.339811,
		omega = 1.0, 
		chi = 1.0, 
		chiR = 1.0, 
		m = 3, 
		n = 5.42195,
		c = 1.26417,
		d = 0.799535,
		h = -0.433247
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'In', 
		particleType2 = 'P',
		A = 2979.85908544*eV, 
		B = 404.713322979*eV,
		R = 3.2*Angstrom, 
		S = 3.3*Angstrom,
		l = 2.71648405284*1/Angstrom, 
		mu = 1.71809756046*1/Angstrom,
		alpha = 1.89106*1/Angstrom,
		beta = 0.338811,
		omega = 1.0, 
		chi = 1.0, 
		chiR = 1.0,
		m = 3, 
		n = 5.3449,
		c = 1.2179,
		d = 0.831026,
		h = -0.461576
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'Al',
		particleType2 = 'P',
		A = 706.748753819*eV,
		B = 143.092861484*eV, 
		R = 3.2*Angstrom, 
		S = 3.4*Angstrom, 
		l = 2.66302685677*1/Angstrom,
		mu = 1.59490381969*1/Angstrom,
		alpha = 1.89106*1/Angstrom, 
		beta = 0.180382,
		omega = 1.0, 
		chi = 1.0, 
		chiR = 1.0, 
		m = 3, 
		n = 5.3449,
		c = 1.2179,
		d = 0.831026,
		h = -0.461576
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'Ga', 
		particleType2 = 'N',
		A = 8476.21720773*eV, 
		B = 120.071835377*eV, 
		R = 2.4*Angstrom, 
		S = 2.6*Angstrom,
		l = 4.44279446732*1/Angstrom,
		mu = 1.7635875433*1/Angstrom,
		alpha = 1.80993*1/Angstrom, 
		beta = 0.24139, 
		omega = 1.0, 
		chi = 1.0, 
		chiR = 1.0,
		m = 3, 
		n = 6.15189, 
		c = 2.59473, 
		d = 0.891376,
		h = -0.505871
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'In',
		particleType2 = 'N', 
		A = 5089.68130469*eV,
		B = 419.19142688*eV,
		R = 2.55*Angstrom, 
		S = 2.75*Angstrom, 
		l = 3.48292127513*1/Angstrom,
		mu = 2.05590031056*1/Angstrom,
		alpha = 1.59607*1/Angstrom,
		beta = 0.30813, 
		omega = 1.0, 
		chi = 1.0, 
		chiR = 1.0, 
		m = 3, 
		n = 9.74096, 
		c = 1.07074,
		d = 0.725308,
		h = -0.533599
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'Al',
		particleType2 = 'N', 
		A = 2014.4712286*eV,
		B = 143.507300765*eV, 
		R = 2.185*Angstrom,
		S = 2.485*Angstrom, 
		l = 3.52685578566*1/Angstrom,
		mu = 1.6405506492*1/Angstrom,
		alpha = 1.99072*1/Angstrom, 
		beta = 0.19987, 
		omega = 1.0,
		chi = 1.0, 
		chiR = 1.0,
		m = 3, 
		n = 2.66213,
		c = 2.33154,
		d = 0.831225,
		h = -0.638531
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'Ga', 
		particleType2 = 'Sb',
		A = 2521.75690165*eV, 
		B = 544.903920313*eV,
		R = 3.4*Angstrom,
		S = 3.6*Angstrom,
		l = 2.50244906524*1/Angstrom,
		mu = 1.74516821967*1/Angstrom,
		alpha = 0.968688*1/Angstrom,
		beta = 0.363018, 
		omega = 1.0, 
		chi = 1.0,
		chiR = 1.0,
		m = 3,
		n = 4.60221,
		c = 1.20875,
		d = 0.839761,
		h = -0.427706
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'In', 
		particleType2 = 'Sb',
		A = 14105.2788772*eV,
		B = 67.9591739905*eV, 
		R = 3.6*Angstrom, 
		S = 3.7*Angstrom,
		l = 3.53729436171*1/Angstrom,
		mu = 1.16887436611*1/Angstrom, 
		alpha = 2.47677*1/Angstrom,
		beta = 0.304347, 
		omega = 1.0, 
		chi = 1.0, 
		chiR = 1.0,
		m = 3, 
		n = 1.8926,
		c = 5.32122, 
		d = 1.39907, 
		h = -0.489527
	)
	potentialSet.addPotential(potential)
	potential = TersoffDiag2Potential(
		particleType1 = 'Al', 
		particleType2 = 'Sb',
		A = 42112.5615678*eV, 
		B = 198.131664381*eV, 
		R = 3.6*Angstrom, 
		S = 3.8*Angstrom, 
		l = 4.01872266622*1/Angstrom,
		mu = 1.50451410321*1/Angstrom,
		alpha = 2.47677*1/Angstrom,
		beta = 0.604408, 
		omega = 1.0,
		chi = 1.0,
		chiR = 1.0,
		m = 3, 
		n = 1.8926, 
		c = 5.32122,
		d = 1.39907,
		h = -0.489527
	)
	potentialSet.addPotential(potential)
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