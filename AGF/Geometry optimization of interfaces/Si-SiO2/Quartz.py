# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
lattice = Hexagonal(4.916*Angstrom, 5.4054*Angstrom)

# Define elements
elements = [Silicon, Silicon, Silicon, Oxygen, Oxygen, Oxygen, Oxygen, Oxygen,
            Oxygen]

# Define coordinates
fractional_coordinates = [[ 0.4697        ,  0.            ,  0.            ],
                          [ 0.            ,  0.4697        ,  0.666666666667],
                          [ 0.5303        ,  0.5303        ,  0.333333333333],
                          [ 0.4135        ,  0.2669        ,  0.1191        ],
                          [ 0.2669        ,  0.4135        ,  0.547567      ],
                          [ 0.7331        ,  0.1466        ,  0.785767      ],
                          [ 0.5865        ,  0.8534        ,  0.214233      ],
                          [ 0.8534        ,  0.5865        ,  0.452433      ],
                          [ 0.1466        ,  0.7331        ,  0.8809        ]]

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
    density_mesh_cutoff=140.0*Hartree,
    )

calculator = LCAOCalculator(
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    )

bulk_configuration.setCalculator(calculator)
bulk_configuration.update()
nlsave('Quartz.nc', bulk_configuration)

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
nlsave('Quartz.nc', bulk_configuration)
