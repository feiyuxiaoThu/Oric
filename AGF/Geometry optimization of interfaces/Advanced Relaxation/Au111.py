# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [20.2231832312, 0.0, 0.0]*Angstrom
vector_b = [0.0, -2.88902617589, 0.0]*Angstrom
vector_c = [0.0, 0.0, 7.06373620597]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold, Gold,
            Gold, Gold]

# Define coordinates
fractional_coordinates = [[ 0.166704890125,  0.            ,  0.166666666666],
                          [ 0.416704890125,  0.            ,  0.166666666666],
                          [ 0.666704890126,  0.            ,  0.166666666666],
                          [ 0.916704890126,  0.            ,  0.166666666666],
                          [ 0.041704890125,  0.5           ,  0.166666666666],
                          [ 0.291704890125,  0.5           ,  0.166666666666],
                          [ 0.541704890126,  0.5           ,  0.166666666666],
                          [ 0.791704890126,  0.5           ,  0.166666666666],
                          [ 0.083371556792, -0.            ,  0.500000000001],
                          [ 0.333371556792, -0.            ,  0.500000000001],
                          [ 0.583371556792, -0.            ,  0.500000000001],
                          [ 0.833371556793, -0.            ,  0.500000000001],
                          [ 0.208371556792,  0.5           ,  0.500000000001],
                          [ 0.458371556792,  0.5           ,  0.500000000001],
                          [ 0.708371556793,  0.5           ,  0.500000000001],
                          [ 0.958371556793,  0.5           ,  0.500000000001],
                          [ 0.000038223458,  0.            ,  0.833333333334],
                          [ 0.250038223459,  0.            ,  0.833333333334],
                          [ 0.500038223459,  0.            ,  0.833333333334],
                          [ 0.750038223459,  0.            ,  0.833333333334],
                          [ 0.125038223458,  0.5           ,  0.833333333334],
                          [ 0.375038223459,  0.5           ,  0.833333333334],
                          [ 0.625038223459,  0.5           ,  0.833333333334],
                          [ 0.87503822346 ,  0.5           ,  0.833333333334]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add tags
bulk_configuration.addTags('Right Interface')

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------

potentialSet = EAM_Zhou_2004()
calculator = TremoloXCalculator(parameters=potentialSet)
calculator.setVerletListsDelta(0.25*Angstrom)

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('Au111.nc', bulk_configuration)

# -------------------------------------------------------------
# Optimize Geometry
# -------------------------------------------------------------
constraints = [FixStrain(x=True, y=True, z=False)]

bulk_configuration = OptimizeGeometry(
    bulk_configuration,
    max_forces=0.01*eV/Ang,
    max_stress=0.001*GPa,
    max_steps=200,
    max_step_length=0.2*Ang,
    constraints=constraints,
    trajectory_filename=None,
    optimizer_method=LBFGS(),
    constrain_bravais_lattice=False,
)
nlsave('Au111.nc', bulk_configuration)
nlprint(bulk_configuration)
