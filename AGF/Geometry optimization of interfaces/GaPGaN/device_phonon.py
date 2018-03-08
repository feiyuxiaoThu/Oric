# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Two-probe Configuration
# -------------------------------------------------------------

# -------------------------------------------------------------
# Left Electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [8.61799719338, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.61799719338, 0.0]*Angstrom
vector_c = [0.0, 0.0, 5.45049999999]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus, Gallium,
                           Gallium, Gallium, Gallium, Gallium, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Gallium, Gallium, Gallium,
                           Gallium, Gallium]

# Define coordinates
left_electrode_coordinates = [[ 4.696198495919,  0.430292860922,  0.681312499999],
                              [ 8.143397373271,  2.153892299598,  0.681312499999],
                              [ 2.972599057243,  3.877491738274,  0.681312499999],
                              [ 6.419797934595,  5.60109117695 ,  0.681312499999],
                              [ 1.248999618567,  7.324690615626,  0.681312499999],
                              [ 6.419797934595,  1.29209258026 ,  2.043937499997],
                              [ 1.248999618567,  3.015692018936,  2.043937499997],
                              [ 4.696198495919,  4.739291457612,  2.043937499997],
                              [ 8.143397373271,  6.462890896288,  2.043937499997],
                              [ 2.972599057243,  8.186490334964,  2.043937499997],
                              [ 2.110799337905,  1.29209258026 ,  3.406562499995],
                              [ 5.557998215257,  3.015692018936,  3.406562499995],
                              [ 0.387199899229,  4.739291457612,  3.406562499995],
                              [ 3.834398776581,  6.462890896288,  3.406562499995],
                              [ 7.281597653933,  8.186490334964,  3.406562499995],
                              [ 0.387199899229,  0.430292860922,  4.769187499993],
                              [ 3.834398776581,  2.153892299598,  4.769187499993],
                              [ 7.281597653933,  3.877491738274,  4.769187499993],
                              [ 2.110799337905,  5.60109117695 ,  4.769187499993],
                              [ 5.557998215257,  7.324690615626,  4.769187499993]]*Angstrom

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
vector_a = [8.61799719338, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.61799719338, 0.0]*Angstrom
vector_c = [0.0, 0.0, 4.52000000003]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen,
                            Nitrogen, Nitrogen, Gallium, Gallium, Gallium, Gallium, Gallium,
                            Gallium, Gallium, Gallium, Nitrogen, Nitrogen, Nitrogen, Nitrogen,
                            Nitrogen, Nitrogen, Nitrogen, Nitrogen, Gallium, Gallium, Gallium,
                            Gallium, Gallium, Gallium, Gallium, Gallium]

# Define coordinates
right_electrode_coordinates = [[ 3.683064515355,  1.522092391676,  0.565000000007],
                               [ 7.992063112045,  1.522092391676,  0.565000000007],
                               [ 1.52856521701 ,  3.676591690021,  0.565000000007],
                               [ 5.8375638137  ,  3.676591690021,  0.565000000007],
                               [ 3.683064515355,  5.831090988366,  0.565000000007],
                               [ 7.992063112045,  5.831090988366,  0.565000000007],
                               [ 1.52856521701 ,  7.985590286711,  0.565000000007],
                               [ 5.8375638137  ,  7.985590286711,  0.565000000007],
                               [ 2.605814866183,  0.444842742503,  1.695000000023],
                               [ 6.914813462873,  0.444842742503,  1.695000000023],
                               [ 0.451315567838,  2.599342040848,  1.695000000023],
                               [ 4.760314164528,  2.599342040848,  1.695000000023],
                               [ 2.605814866183,  4.753841339193,  1.695000000023],
                               [ 6.914813462873,  4.753841339193,  1.695000000023],
                               [ 0.451315567838,  6.908340637538,  1.695000000023],
                               [ 4.760314164528,  6.908340637538,  1.695000000023],
                               [ 1.52856521701 ,  1.522092391676,  2.825000000001],
                               [ 5.8375638137  ,  1.522092391676,  2.825000000001],
                               [ 3.683064515355,  3.676591690021,  2.825000000001],
                               [ 7.992063112045,  3.676591690021,  2.825000000001],
                               [ 1.52856521701 ,  5.831090988366,  2.825000000001],
                               [ 5.8375638137  ,  5.831090988366,  2.825000000001],
                               [ 3.683064515355,  7.985590286711,  2.825000000001],
                               [ 7.992063112045,  7.985590286711,  2.825000000001],
                               [ 0.451315567838,  0.444842742503,  3.955000000017],
                               [ 4.760314164528,  0.444842742503,  3.955000000017],
                               [ 2.605814866183,  2.599342040848,  3.955000000017],
                               [ 6.914813462873,  2.599342040848,  3.955000000017],
                               [ 0.451315567838,  4.753841339193,  3.955000000017],
                               [ 4.760314164528,  4.753841339193,  3.955000000017],
                               [ 2.605814866183,  6.908340637538,  3.955000000017],
                               [ 6.914813462873,  6.908340637538,  3.955000000017]]*Angstrom

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
vector_a = [8.61799719338, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.61799719338, 0.0]*Angstrom
vector_c = [0.0, 0.0, 30.4694059135]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus, Gallium,
                           Gallium, Gallium, Gallium, Gallium, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Gallium, Gallium, Gallium,
                           Gallium, Gallium, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Gallium, Gallium, Gallium, Gallium, Gallium,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus,
                           Gallium, Gallium, Gallium, Gallium, Gallium, Phosphorus,
                           Phosphorus, Phosphorus, Phosphorus, Phosphorus, Gallium, Gallium,
                           Gallium, Gallium, Gallium, Phosphorus, Phosphorus, Phosphorus,
                           Phosphorus, Phosphorus, Gallium, Gallium, Gallium, Gallium,
                           Gallium, Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen,
                           Nitrogen, Nitrogen, Nitrogen, Gallium, Gallium, Gallium, Gallium,
                           Gallium, Gallium, Gallium, Gallium, Nitrogen, Nitrogen, Nitrogen,
                           Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen, Gallium, Gallium,
                           Gallium, Gallium, Gallium, Gallium, Gallium, Gallium, Nitrogen,
                           Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen,
                           Nitrogen, Gallium, Gallium, Gallium, Gallium, Gallium, Gallium,
                           Gallium, Gallium, Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen,
                           Nitrogen, Nitrogen, Nitrogen, Gallium, Gallium, Gallium, Gallium,
                           Gallium, Gallium, Gallium, Gallium, Nitrogen, Nitrogen, Nitrogen,
                           Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen, Gallium, Gallium,
                           Gallium, Gallium, Gallium, Gallium, Gallium, Gallium, Nitrogen,
                           Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen, Nitrogen,
                           Nitrogen, Gallium, Gallium, Gallium, Gallium, Gallium, Gallium,
                           Gallium, Gallium]

# Define coordinates
central_region_coordinates = [[  4.696198495919,   0.430292860922,   0.681312499999],
                              [  8.143397373271,   2.153892299598,   0.681312499999],
                              [  2.972599057243,   3.877491738274,   0.681312499999],
                              [  6.419797934595,   5.60109117695 ,   0.681312499999],
                              [  1.248999618567,   7.324690615626,   0.681312499999],
                              [  6.419797934595,   1.29209258026 ,   2.043937499997],
                              [  1.248999618567,   3.015692018936,   2.043937499997],
                              [  4.696198495919,   4.739291457612,   2.043937499997],
                              [  8.143397373271,   6.462890896288,   2.043937499997],
                              [  2.972599057243,   8.186490334964,   2.043937499997],
                              [  2.110799337905,   1.29209258026 ,   3.406562499995],
                              [  5.557998215257,   3.015692018936,   3.406562499995],
                              [  0.387199899229,   4.739291457612,   3.406562499995],
                              [  3.834398776581,   6.462890896288,   3.406562499995],
                              [  7.281597653933,   8.186490334964,   3.406562499995],
                              [  0.387199899229,   0.430292860922,   4.769187499993],
                              [  3.834398776581,   2.153892299598,   4.769187499993],
                              [  7.281597653933,   3.877491738274,   4.769187499993],
                              [  2.110799337905,   5.60109117695 ,   4.769187499993],
                              [  5.557998215257,   7.324690615626,   4.769187499993],
                              [  4.70338173054 ,   0.433288103055,   6.133640662428],
                              [  8.147519901074,   2.155262155656,   6.132675374226],
                              [  2.978420576773,   3.879708183928,   6.13022792901 ],
                              [  6.428295538942,   5.604833396115,   6.13018534503 ],
                              [  1.259239042667,   7.329297034138,   6.132607677054],
                              [  6.427445840628,   1.293921772062,   7.499964767292],
                              [  1.257333133354,   3.016397975116,   7.492018842477],
                              [  4.706394173754,   4.741764126326,   7.489104213591],
                              [  8.155499123763,   6.467081432063,   7.491903361844],
                              [  2.985394464316,   8.189644905101,   7.499941457682],
                              [  2.12538021723 ,   1.300593694725,   8.861221421318],
                              [  5.568033331785,   3.026000844366,   8.857059579093],
                              [  0.404738452358,   4.744820411819,   8.850107041729],
                              [  3.859446682365,   6.463620315897,   8.857025604212],
                              [  7.302197344119,   8.188927624634,   8.861074276792],
                              [  0.407815091714,   0.435092172115,  10.228512447969],
                              [  3.841538562289,   2.181457210106,  10.225840273812],
                              [  7.297684911412,   3.889002463398,  10.209919803739],
                              [  2.135853786312,   5.599626056102,  10.209982017678],
                              [  5.592161485692,   7.307178486247,  10.225647628669],
                              [  1.267109551556,   7.296844606079,  11.57308207944 ],
                              [  2.982070892912,   3.91144072834 ,  11.617141452727],
                              [  4.724540988628,   0.438404662164,  11.539484147004],
                              [  6.466149433113,   5.583047499249,  11.616998105673],
                              [  8.181218277226,   2.197873054515,  11.572458476073],
                              [  6.486258236463,   1.246798405927,  12.870920463024],
                              [  2.968502703138,   8.246877668257,  12.870550881543],
                              [  4.727187769331,   4.746916738359,  12.980485427913],
                              [  8.236779467571,   6.360518943962,  13.004143006679],
                              [  1.218217018033,   3.132660379451,  13.003832342875],
                              [  7.468767640583,   8.178351314735,  14.217545523465],
                              [  3.893133482781,   6.601707236982,  14.249986336763],
                              [  2.002905743379,   1.321737416323,  14.217503737162],
                              [  5.577737928194,   2.898197459109,  14.251728558498],
                              [  0.426514623561,   4.750205184552,  14.735653411055],
                              [  5.736391103301,   7.353553367469,  15.391738987017],
                              [  3.735191883096,   2.150883288108,  15.393614569395],
                              [  0.430523149292,   0.439841925863,  15.700977638339],
                              [  7.335420293282,   3.255440357034,  15.833598468591],
                              [  2.145662696913,   6.24185673668 ,  15.836560448605],
                              [  1.441388223023,   7.851928196708,  16.988188591791],
                              [  8.048993706038,   1.651569222418,  16.98883954604 ],
                              [  7.941181080711,   5.837257983028,  17.08974044458 ],
                              [  1.56046887689 ,   3.662358068836,  17.089501987899],
                              [  3.63539725665 ,   5.698367934484,  17.179099810745],
                              [  5.857538397193,   3.806322109994,  17.181009992682],
                              [  3.809508351503,   1.431919498604,  17.194466091973],
                              [  5.685607110976,   8.069983839058,  17.195671370981],
                              [  2.579233888077,   0.35692454391 ,  18.213894749893],
                              [  6.918395412372,   0.526315475691,  18.21461148755 ],
                              [  0.493299674218,   2.613815719225,  18.279943286941],
                              [  0.387535072724,   6.887157083534,  18.282094582847],
                              [  4.796062508135,   2.634731156423,  18.309055854367],
                              [  4.702121786851,   6.866017979413,  18.309011769678],
                              [  6.937758108005,   4.814148787905,  18.357711230294],
                              [  2.562554955546,   4.686986016671,  18.358263907295],
                              [  8.014542042876,   3.679346615038,  19.475509037098],
                              [  1.538622245216,   1.482334817325,  19.424882296433],
                              [  3.641556426429,   7.957843693828,  19.462565008949],
                              [  7.963097730594,   8.021098521791,  19.425612746444],
                              [  5.860035660589,   1.545595027308,  19.462856064438],
                              [  1.488550095447,   5.823677288011,  19.476174584071],
                              [  5.821614407554,   5.851503724454,  19.499460388134],
                              [  3.681118922022,   3.651802814682,  19.49995533323 ],
                              [  6.929225613108,   2.605488677987,  20.646430886337],
                              [  4.752344038822,   0.442254307814,  20.615233294467],
                              [  2.575934583307,   6.89715401756 ,  20.646833624468],
                              [  0.443417088273,   0.442414947634,  20.619269114151],
                              [  2.595948049823,   2.562973470525,  20.637912814463],
                              [  6.908867943046,   6.93945891189 ,  20.638021518022],
                              [  0.443611916287,   4.751087809568,  20.663713784518],
                              [  4.752766760426,   4.751337422757,  20.659544133924],
                              [  3.681580122137,   1.506557142153,  21.811662309428],
                              [  7.996494286216,   1.517937514212,  21.81288326679 ],
                              [  1.527620168677,   3.660513849087,  21.816869926923],
                              [  5.840014414457,   3.674055676674,  21.820729253926],
                              [  3.668732903157,   5.830763599002,  21.820822078868],
                              [  7.980932927105,   5.844121309165,  21.816817734092],
                              [  1.51191325178 ,   7.987043501568,  21.812941086147],
                              [  5.82670965693 ,   7.998253243794,  21.811707673346],
                              [  2.599566216333,   0.438625499901,  22.988646224446],
                              [  6.911600164833,   0.447467509885,  22.988558593552],
                              [  0.449746652074,   2.59233373406 ,  22.993355584819],
                              [  4.757269224827,   2.592248417515,  22.986968561381],
                              [  2.599521262868,   4.746326963208,  22.991600743475],
                              [  6.911772280676,   4.757676131808,  22.991626569483],
                              [  0.443429145826,   6.911686951156,  22.993286802071],
                              [  4.753992321976,   6.911818221666,  22.987095015934],
                              [  1.527844083463,   1.518225455941,  24.166641481638],
                              [  5.835664841764,   1.521509413012,  24.165055276792],
                              [  3.681884895308,   3.672362015082,  24.163428786272],
                              [  7.990525080482,   3.676242342847,  24.163822917314],
                              [  1.524177350544,   5.83005755307 ,  24.163770885483],
                              [  5.83284851395 ,   5.833925661719,  24.163470022441],
                              [  3.678996859898,   7.984829686713,  24.165100390344],
                              [  7.986808790015,   7.988102998641,  24.166592661337],
                              [  0.449688555687,   0.443763355516,  25.340707879825],
                              [  4.758704112548,   0.443784604367,  25.339223968505],
                              [  2.605006491138,   2.597441751829,  25.339613016691],
                              [  6.913762935432,   2.598974965449,  25.339050355672],
                              [  0.449709094888,   4.752776173352,  25.339318374754],
                              [  4.758705508631,   4.752768649933,  25.337949437495],
                              [  2.603623891818,   6.906561096685,  25.339049612152],
                              [  6.91240811089 ,   6.908111346379,  25.3396141755  ],
                              [  3.683064515355,   1.522092391676,  26.514405913482],
                              [  7.992063112045,   1.522092391676,  26.514405913482],
                              [  1.52856521701 ,   3.676591690021,  26.514405913482],
                              [  5.8375638137  ,   3.676591690021,  26.514405913482],
                              [  3.683064515355,   5.831090988366,  26.514405913482],
                              [  7.992063112045,   5.831090988366,  26.514405913482],
                              [  1.52856521701 ,   7.985590286711,  26.514405913482],
                              [  5.8375638137  ,   7.985590286711,  26.514405913482],
                              [  2.605814866183,   0.444842742503,  27.644405913498],
                              [  6.914813462873,   0.444842742503,  27.644405913498],
                              [  0.451315567838,   2.599342040848,  27.644405913498],
                              [  4.760314164528,   2.599342040848,  27.644405913498],
                              [  2.605814866183,   4.753841339193,  27.644405913498],
                              [  6.914813462873,   4.753841339193,  27.644405913498],
                              [  0.451315567838,   6.908340637538,  27.644405913498],
                              [  4.760314164528,   6.908340637538,  27.644405913498],
                              [  1.52856521701 ,   1.522092391676,  28.774405913476],
                              [  5.8375638137  ,   1.522092391676,  28.774405913476],
                              [  3.683064515355,   3.676591690021,  28.774405913476],
                              [  7.992063112045,   3.676591690021,  28.774405913476],
                              [  1.52856521701 ,   5.831090988366,  28.774405913476],
                              [  5.8375638137  ,   5.831090988366,  28.774405913476],
                              [  3.683064515355,   7.985590286711,  28.774405913476],
                              [  7.992063112045,   7.985590286711,  28.774405913476],
                              [  0.451315567838,   0.444842742503,  29.904405913492],
                              [  4.760314164528,   0.444842742503,  29.904405913492],
                              [  2.605814866183,   2.599342040848,  29.904405913492],
                              [  6.914813462873,   2.599342040848,  29.904405913492],
                              [  0.451315567838,   4.753841339193,  29.904405913492],
                              [  4.760314164528,   4.753841339193,  29.904405913492],
                              [  2.605814866183,   6.908340637538,  29.904405913492],
                              [  6.914813462873,   6.908340637538,  29.904405913492]]*Angstrom

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

potentialSet = Tersoff_Powell_2007()
calculator = TremoloXCalculator(parameters=potentialSet)
calculator.setVerletListsDelta(0.25*Angstrom)

device_configuration.setCalculator(calculator)
nlprint(device_configuration)
device_configuration.update()
nlsave('device_phonon.nc', device_configuration)

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
nlsave('device_phonon.nc', dynamical_matrix)

# -------------------------------------------------------------
# Phonon Transmission Spectrum
# -------------------------------------------------------------
qpoint_grid = MonkhorstPackGrid(
    na=6,
    nb=6,
    )

phonon_transmission_spectrum = PhononTransmissionSpectrum(
    configuration=device_configuration,
    dynamical_matrix=dynamical_matrix,
    energies=numpy.linspace(0,0.3,501)*eV,
    qpoints=qpoint_grid,
    infinitesimal=1e-06*eV,
    self_energy_calculator=RecursionSelfEnergy(),
    )
nlsave('device_phonon.nc', phonon_transmission_spectrum)
nlprint(phonon_transmission_spectrum)
