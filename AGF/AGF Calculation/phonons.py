# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Two-probe Configuration
# -------------------------------------------------------------

# -------------------------------------------------------------
# Left Electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [3.97394011027, 0.0, 0.0]*Angstrom
vector_b = [0.0, 3.97394011027, 0.0]*Angstrom
vector_c = [0.0, 0.0, 11.2620095523]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Arsenic, Aluminium, Arsenic, Aluminium, Arsenic, Aluminium, Arsenic,
                           Aluminium]

# Define coordinates
left_electrode_coordinates = [[  1.986970055135,   0.            ,   0.713504776191],
                              [  1.986970055135,   1.986970055135,   2.118504776226],
                              [  0.            ,   1.986970055135,   3.523504776261],
                              [  0.            ,   0.            ,   4.928504776149],
                              [  1.986970055135,   0.            ,   6.333504776183],
                              [  1.986970055135,   1.986970055135,   7.738504776218],
                              [  0.            ,   1.986970055135,   9.143504776252],
                              [  0.            ,   0.            ,  10.54850477614 ]]*Angstrom

# Set up configuration
left_electrode = BulkConfiguration(
    bravais_lattice=left_electrode_lattice,
    elements=left_electrode_elements,
    cartesian_coordinates=left_electrode_coordinates
    )

# -------------------------------------------------------------
# Right Electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [3.97394011027, 0.0, 0.0]*Angstrom
vector_b = [0.0, 3.97394011027, 0.0]*Angstrom
vector_c = [0.0, 0.0, 11.3169202169]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Arsenic, Gallium, Arsenic, Gallium, Arsenic, Gallium, Arsenic,
                            Gallium]

# Define coordinates
right_electrode_coordinates = [[  1.986970055135,   0.            ,   0.708248765164],
                               [  1.986970055135,   1.986970055135,   2.124857276681],
                               [  0.            ,   1.986970055135,   3.541546451662],
                               [  0.            ,   0.            ,   4.954971451636],
                               [  1.986970055135,   0.            ,   6.368396451611],
                               [  1.986970055135,   1.986970055135,   7.781821451732],
                               [  0.            ,   1.986970055135,   9.195246451706],
                               [  0.            ,   0.            ,  10.60867145168 ]]*Angstrom

# Set up configuration
right_electrode = BulkConfiguration(
    bravais_lattice=right_electrode_lattice,
    elements=right_electrode_elements,
    cartesian_coordinates=right_electrode_coordinates
    )

# -------------------------------------------------------------
# Central Region
# -------------------------------------------------------------

# Set up lattice
vector_a = [3.97394011027, 0.0, 0.0]*Angstrom
vector_b = [0.0, 3.97394011027, 0.0]*Angstrom
vector_c = [0.0, 0.0, 113.526163964]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Arsenic, Aluminium, Arsenic, Aluminium, Arsenic, Aluminium, Arsenic,
                           Aluminium, Arsenic, Aluminium, Arsenic, Aluminium, Arsenic,
                           Aluminium, Arsenic, Aluminium, Arsenic, Aluminium, Arsenic,
                           Aluminium, Arsenic, Aluminium, Arsenic, Aluminium, Arsenic,
                           Aluminium, Arsenic, Aluminium, Arsenic, Aluminium, Arsenic,
                           Aluminium, Arsenic, Aluminium, Arsenic, Aluminium, Arsenic,
                           Aluminium, Arsenic, Aluminium, Arsenic, Gallium, Arsenic, Gallium,
                           Arsenic, Gallium, Arsenic, Gallium, Arsenic, Gallium, Arsenic,
                           Gallium, Arsenic, Gallium, Arsenic, Gallium, Arsenic, Gallium,
                           Arsenic, Gallium, Arsenic, Gallium, Arsenic, Gallium, Arsenic,
                           Gallium, Arsenic, Gallium, Arsenic, Gallium, Arsenic, Gallium,
                           Arsenic, Gallium, Arsenic, Gallium, Arsenic, Gallium, Arsenic,
                           Gallium]

# Define coordinates
central_region_coordinates = [[   1.986970055135,    0.            ,    0.713504776191],
                              [   1.986970055135,    1.986970055135,    2.118504776226],
                              [   0.            ,    1.986970055135,    3.523504776261],
                              [   0.            ,    0.            ,    4.928504776149],
                              [   1.986970055135,    0.            ,    6.333504776183],
                              [   1.986970055135,    1.986970055135,    7.738504776218],
                              [   0.            ,    1.986970055135,    9.143504776252],
                              [   0.            ,    0.            ,   10.54850477614 ],
                              [   1.986970052625,    0.000000196155,   11.975182324402],
                              [   1.986970065416,    1.986969795367,   13.400717407002],
                              [  -0.000000016901,    1.986970542801,   14.826298915268],
                              [   0.000000030783,   -0.000000597181,   16.25188249461 ],
                              [   1.986970022746,    0.000000915931,   17.677471808386],
                              [   1.986970066992,    1.986969032575,   19.103056542217],
                              [  -0.000000003955,    1.986971323975,   20.528649914921],
                              [  -0.000000040027,   -0.000001348368,   21.954229367969],
                              [   1.986970107432,    0.000001660014,   23.379808841182],
                              [   1.986969946914,    1.986968309468,   24.805392500633],
                              [   0.000000125699,    1.986971976072,   26.230971250019],
                              [  -0.00000018751 ,   -0.000002001329,   27.656555475554],
                              [   1.986970260173,    0.000001991569,   29.082145774205],
                              [   1.986969808942,    1.986968048759,   30.507723023354],
                              [   0.00000025844 ,    1.986971852457,   31.933303342873],
                              [  -0.0000003019  ,   -0.000001684381,   33.358879999833],
                              [   1.986970361673,    0.000001227973,   34.78446942259 ],
                              [   1.986969744185,    1.986969032017,   36.210054840676],
                              [   0.000000303532,    1.986970482383,   37.635659933093],
                              [  -0.000000251142,   -0.000000195486,   39.061250385929],
                              [   1.986970292646,   -0.000000581623,   40.486834564181],
                              [   1.986969874629,    1.986970849563,   41.912412278444],
                              [   0.000000162958,    1.986968565917,   43.337988177114],
                              [  -0.000000101992,    0.000001624302,   44.76355347139 ],
                              [   1.986970131589,   -0.000002019522,   46.18916396467 ],
                              [   1.986970051371,    1.986972134448,   47.614740465916],
                              [  -0.000000020967,    1.986967806146,   49.04035232764 ],
                              [   0.000000074159,    0.000002240514,   50.465942575058],
                              [   1.986969969226,   -0.000002093076,   51.891517645919],
                              [   1.986970155055,    1.986972039361,   53.317101100626],
                              [  -0.000000098956,    1.986968609913,   54.742667386015],
                              [   0.00000008456 ,    0.000001244451,   56.168271836292],
                              [   1.986969978692,   -0.000000489398,   57.593351016183],
                              [   1.986970091119,    1.986970404288,   59.012316332313],
                              [  -0.000000026591,    1.986969905031,   60.428446514889],
                              [   0.000000010908,    0.000000111908,   61.844749298526],
                              [   1.986970047153,   -0.000000047245,   63.261046667149],
                              [   1.986970058352,    1.986970090165,   64.677353790239],
                              [  -0.000000002369,    1.986970040263,   66.093666692979],
                              [   0.000000000899,    0.000000011273,   67.509986322203],
                              [   1.986970054401,   -0.000000004645,   68.926294783143],
                              [   1.986970055331,    1.986970059003,   70.342589821599],
                              [  -0.000000000245,    1.986970053846,   71.758885258889],
                              [   0.000000000015,    0.000000001176,   73.175165653742],
                              [   1.986970055045,   -0.000000000347,   74.591464656946],
                              [   1.986970055128,    1.986970055364,   76.007774891785],
                              [  -0.000000000041,    1.986970054959,   77.424074945435],
                              [  -0.000000000004,    0.000000000027,   78.840395562259],
                              [   1.986970055114,   -0.000000000102,   80.256686287066],
                              [   1.986970055129,    1.986970055171,   81.672979863134],
                              [  -0.000000000013,    1.986970055126,   83.089275294637],
                              [  -0.000000000009,    0.000000000064,   84.505559469157],
                              [   1.986970055123,    0.00000000005 ,   85.921865159506],
                              [   1.986970055124,    1.986970055203,   87.338160291585],
                              [  -0.000000000011,    1.986970055189,   88.754459133579],
                              [  -0.000000000009,    0.000000000049,   90.170749928305],
                              [   1.986970055127,    0.000000000033,   91.587051480578],
                              [   1.986970055129,    1.98697005516 ,   93.003344850062],
                              [  -0.000000000005,    1.986970055148,   94.419653489542],
                              [  -0.000000000003,    0.00000000001 ,   95.835962903661],
                              [   1.986970055133,    0.000000000004,   97.252268490913],
                              [   1.986970055134,    1.986970055138,   98.668578461843],
                              [  -0.000000000001,    1.986970055136,  100.084879562099],
                              [  -0.            ,    0.            ,  101.501198534987],
                              [   1.986970055135,    0.            ,  102.91749251186 ],
                              [   1.986970055135,    1.986970055135,  104.334101023377],
                              [   0.            ,    1.986970055135,  105.750790198358],
                              [   0.            ,    0.            ,  107.164215198332],
                              [   1.986970055135,    0.            ,  108.577640198307],
                              [   1.986970055135,    1.986970055135,  109.991065198428],
                              [   0.            ,    1.986970055135,  111.404490198402],
                              [   0.            ,    0.            ,  112.817915198376]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

device_configuration = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode]
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------

potentialSet = TremoloXPotentialSet(name = 'Tersoff_AlGaAs_2000')
potentialSet.addParticleType(ParticleType(
	symbol = 'As', 
	mass = 74.9216 * atomic_mass_unit, 
	charge = 0.0*elementary_charge, 
	sigma = None, 
	sigma14 = None, 
	epsilon = None, 
	epsilon14 = None, 
	atomicNumber = None, 
	tags = []
))
potentialSet.addParticleType(ParticleType(
	symbol = 'Al', 
	mass = 26.9815 * atomic_mass_unit, 
	charge = 0.0*elementary_charge, 
	sigma = None, 
	sigma14 = None, 
	epsilon = None, 
	epsilon14 = None, 
	atomicNumber = None, 
	tags = []
))
potentialSet.addParticleType(ParticleType(
	symbol = 'Ga', 
	mass = 69.723 * atomic_mass_unit, 
	charge = 0.0*elementary_charge, 
	sigma = None, 
	sigma14 = None, 
	epsilon = None, 
	epsilon14 = None, 
	atomicNumber = None, 
	tags = []
))


potential = TersoffSingleTypePotential(
	particleType = ParticleIdentifier('Al', []),
	A = 492.7659*eV,
	B = 23.031117*eV,
	R = 3.4*Angstrom,
	S = 3.6*Angstrom,
	l = 2.585337*1/Angstrom,
	mu = 0.927442*1/Angstrom,
	alpha = 0.0*1/Angstrom,
	beta = 0.316846,
	omega = 1.0,
	chi = 1.0,
	chiR = 1.0,
	m = 1,
	n = 6.086505,
	c = 0.074836,
	d = 19.569127,
	h = -0.659266,
)
potentialSet.addPotential(potential)
potential = TersoffSingleTypePotential(
	particleType = ParticleIdentifier('Ga', []),
	A = 993.888094*eV,
	B = 136.123032*eV,
	R = 3.4*Angstrom,
	S = 3.6*Angstrom,
	l = 2.50842747*1/Angstrom,
	mu = 1.490824*1/Angstrom,
	alpha = 0.0*1/Angstrom,
	beta = 0.23586237,
	omega = 1.0,
	chi = 1.0,
	chiR = 1.0,
	m = 1,
	n = 3.4729041,
	c = 0.07629773,
	d = 19.796474,
	h = 7.1459174,
)
potentialSet.addPotential(potential)
potential = TersoffSingleTypePotential(
	particleType = ParticleIdentifier('As', []),
	A = 1571.86084*eV,
	B = 546.4316579*eV,
	R = 3.4*Angstrom,
	S = 3.6*Angstrom,
	l = 2.384132239*1/Angstrom,
	mu = 1.7287263*1/Angstrom,
	alpha = 0.0*1/Angstrom,
	beta = 0.00748809,
	omega = 1.0,
	chi = 1.0,
	chiR = 1.0,
	m = 1,
	n = 0.60879133,
	c = 5.273131,
	d = 0.75102662,
	h = 0.15292354,
)
potentialSet.addPotential(potential)
potential = TersoffDiag2Potential(
	particleType1 = ParticleIdentifier('Al', []),
	particleType2 = ParticleIdentifier('As', []),
	A = 2307.8794*eV,
	B = 219.1396*eV,
	R = 3.4*Angstrom,
	S = 3.6*Angstrom,
	l = 2.8090295*1/Angstrom,
	mu = 1.5582295*1/Angstrom,
	alpha = 0.0*1/Angstrom,
	beta = 0.330946,
	omega = 1.0,
	chi = 1.0,
	chiR = 1.0,
	m = 1,
	n = 4.047579,
	c = 1.449752,
	d = 0.828713,
	h = -0.520946,
)
potentialSet.addPotential(potential)
potential = TersoffDiag2Potential(
	particleType1 = ParticleIdentifier('Al', []),
	particleType2 = ParticleIdentifier('Ga', []),
	A = 699.824*eV,
	B = 55.9917*eV,
	R = 3.4*Angstrom,
	S = 3.6*Angstrom,
	l = 2.54688*1/Angstrom,
	mu = 1.20913*1/Angstrom,
	alpha = 0.0*1/Angstrom,
	beta = 0.273372,
	omega = 1.0,
	chi = 1.0,
	chiR = 1.0,
	m = 1,
	n = 4.59759,
	c = 0.0755633,
	d = 19.6825,
	h = 3.24333,
)
potentialSet.addPotential(potential)
potential = TersoffDiag2Potential(
	particleType1 = ParticleIdentifier('Ga', []),
	particleType2 = ParticleIdentifier('As', []),
	A = 2543.2972*eV,
	B = 314.45966*eV,
	R = 3.4*Angstrom,
	S = 3.6*Angstrom,
	l = 2.82809263*1/Angstrom,
	mu = 1.72301158*1/Angstrom,
	alpha = 0.0*1/Angstrom,
	beta = 0.357192,
	omega = 1.0,
	chi = 1.0,
	chiR = 1.0,
	m = 1,
	n = 6.31741,
	c = 1.226302,
	d = 0.790396,
	h = -0.518489,
)
potentialSet.addPotential(potential)
calculator = TremoloXCalculator(parameters=potentialSet)
calculator.setInternalOrdering("default")
calculator.setVerletListsDelta(0.25*Angstrom)

device_configuration.setCalculator(calculator)
nlprint(device_configuration)
device_configuration.update()
nlsave('phonons1.nc', device_configuration)

# -------------------------------------------------------------
# Dynamical Matrix
# -------------------------------------------------------------
dynamical_matrix = DynamicalMatrix(
    configuration=device_configuration,
    repetitions=(1, 1, 1),
    atomic_displacement=0.01*Angstrom,
    acoustic_sum_rule=True,
    symmetrize=True,
    finite_difference_method=Central,
    force_tolerance=1e-08*Hartree/Bohr**2,
    processes_per_displacement=1,
    log_filename_prefix='displacement_',
    use_wigner_seitz_scheme=False,
    constrain_electrodes=False,
    use_equivalent_bulk=True,
    )
nlsave('phonons1.nc', dynamical_matrix)

# -------------------------------------------------------------
# Phonon Transmission Spectrum
# -------------------------------------------------------------
qpoint_grid = MonkhorstPackGrid(
    na=12,
    nb=12,
    )

phonon_transmission_spectrum = PhononTransmissionSpectrum(
    configuration=device_configuration,
    dynamical_matrix=dynamical_matrix,
    energies=numpy.linspace(0,0.07,501)*eV,
    qpoints=qpoint_grid,
    infinitesimal=1e-06*eV,
    self_energy_calculator=RecursionSelfEnergy(),
    )
nlsave('phonons1.nc', phonon_transmission_spectrum)
nlprint(phonon_transmission_spectrum)
