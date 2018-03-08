# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = FaceCenteredCubic(5.4306*Angstrom)

# Define elements
elements = [Silicon, Silicon]

# Define coordinates
fractional_coordinates = [[ 0.  ,  0.  ,  0.  ],
                          [ 0.25,  0.25,  0.25]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
k_point_sampling = MonkhorstPackGrid(
    na=13,
    nb=13,
    nc=13,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=k_point_sampling,
    density_mesh_cutoff=45.0*Hartree,
    )

calculator = LCAOCalculator(
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('Silicon.nc', bulk_configuration)

# -------------------------------------------------------------
# Optimize Geometry
# -------------------------------------------------------------
bulk_configuration = OptimizeGeometry(
    bulk_configuration,
    max_forces=0.01*eV/Ang,
    max_steps=200,
    max_step_length=0.2*Ang,
    trajectory_filename=None,
    disable_stress=True,
    optimizer_method=LBFGS(),
)
nlsave('Silicon.nc', bulk_configuration)
