# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [5.4306, 0.0, 0.0]*Angstrom
vector_b = [0.0, -5.4306, 0.0]*Angstrom
vector_c = [0.0, 0.0, 33.1370363602]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Silicon, Silicon, Silicon,
            Silicon, Silicon, Silicon, Silicon, Oxygen, Oxygen, Oxygen,
            Silicon, Oxygen, Oxygen, Oxygen, Silicon, Silicon, Oxygen, Oxygen,
            Oxygen, Silicon, Oxygen, Oxygen, Oxygen, Silicon, Silicon, Oxygen,
            Oxygen, Oxygen, Silicon, Oxygen, Oxygen, Oxygen, Silicon, Silicon,
            Oxygen, Oxygen, Oxygen, Silicon, Oxygen, Oxygen, Hydrogen,
            Hydrogen, Hydrogen, Hydrogen, Hydrogen]

# Define coordinates
fractional_coordinates = [[ 0.75          ,  0.25          ,  0.020485386581],
                          [ 0.25          ,  0.75          ,  0.020485386581],
                          [ 0.5           ,  0.            ,  0.061456159744],
                          [-0.            ,  0.5           ,  0.061456159744],
                          [ 0.25          ,  0.25          ,  0.102426932907],
                          [ 0.75          ,  0.75          ,  0.102426932907],
                          [ 0.            ,  0.            ,  0.14339770607 ],
                          [ 0.5           ,  0.5           ,  0.14339770607 ],
                          [ 0.75          ,  0.25          ,  0.184368479232],
                          [ 0.25          ,  0.75          ,  0.184368479232],
                          [ 0.5           ,  0.            ,  0.225339252395],
                          [-0.            ,  0.5           ,  0.225339252395],
                          [ 0.25          ,  0.25          ,  0.266310025558],
                          [ 0.75          ,  0.75          ,  0.266310025558],
                          [ 0.            ,  0.            ,  0.30728079872 ],
                          [ 0.5           ,  0.5           ,  0.30728079872 ],
                          [ 0.75          ,  0.25          ,  0.348251571883],
                          [ 0.25          ,  0.75          ,  0.348251571883],
                          [ 0.5           ,  0.            ,  0.389222345046],
                          [-0.            ,  0.5           ,  0.389222345046],
                          [ 0.25          ,  0.25          ,  0.430193118209],
                          [ 0.75          ,  0.75          ,  0.430193118209],
                          [ 0.            ,  0.            ,  0.471163891371],
                          [ 0.5           ,  0.5           ,  0.471163891371],
                          [ 0.334334283005,  0.498518463007,  0.51123310105 ],
                          [ 0.226817175806,  0.80741240873 ,  0.518143275944],
                          [ 0.773175674006,  0.99821215027 ,  0.534485799864],
                          [ 0.437097806232,  0.387970215657,  0.554991716568],
                          [ 0.665661300633,  0.193004081474,  0.570716705737],
                          [ 0.891848016564,  0.389678786638,  0.586500639468],
                          [ 0.562895781465,  0.992839364834,  0.606798396341],
                          [ 0.10816029254 ,  0.808029563356,  0.622333471931],
                          [-0.            ,  0.5           ,  0.629819627142],
                          [ 0.334334283005,  0.998518463007,  0.639711123004],
                          [ 0.226817175806,  0.30741240873 ,  0.646621297899],
                          [ 0.773175674006,  0.498212150269,  0.662963821819],
                          [ 0.437097806232,  0.887970215657,  0.683469738522],
                          [ 0.665661300633,  0.693004081474,  0.699194727692],
                          [ 0.891848016564,  0.889678786638,  0.714978661423],
                          [ 0.562895781465,  0.492839364834,  0.735276418296],
                          [ 0.10816029254 ,  0.308029563356,  0.750811493885],
                          [ 0.            ,  0.            ,  0.758297649097],
                          [ 0.334334283005,  0.498518463007,  0.768189144959],
                          [ 0.226817175806,  0.80741240873 ,  0.775099319854],
                          [ 0.773175674006,  0.99821215027 ,  0.791441843773],
                          [ 0.437097806232,  0.387970215657,  0.811947760477],
                          [ 0.665661300633,  0.193004081474,  0.827672749647],
                          [ 0.891848016564,  0.389678786638,  0.843456683378],
                          [ 0.562895781465,  0.992839364834,  0.86375444025 ],
                          [ 0.10816029254 ,  0.808029563356,  0.87928951584 ],
                          [-0.            ,  0.5           ,  0.886775671052],
                          [ 0.334334283005,  0.998518463007,  0.896667166914],
                          [ 0.226817175806,  0.30741240873 ,  0.903577341808],
                          [ 0.773175674006,  0.498212150269,  0.919919865728],
                          [ 0.437097806232,  0.887970215657,  0.940425782432],
                          [ 0.665661300633,  0.693004081474,  0.956150771601],
                          [ 0.891848016564,  0.889678786638,  0.971934705332],
                          [ 0.562895781465,  0.492839364834,  0.992232462205],
                          [ 0.873844148953,  0.095233165377,  0.992076989474],
                          [ 0.097970606247,  0.902029393753,  0.995570339359],
                          [ 0.402029393753,  0.597970606247,  0.995570339359],
                          [ 0.435455488834,  0.658677130371,  0.979948747914],
                          [ 0.341322869629,  0.502649049931,  0.990092367522]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add tags
bulk_configuration.addTags('Left Interface',  [])
bulk_configuration.addTags('Right Interface', [])

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------
k_point_sampling = MonkhorstPackGrid(
    na=3,
    nb=3,
    )
numerical_accuracy_parameters = NumericalAccuracyParameters(
    k_point_sampling=k_point_sampling,
    density_mesh_cutoff=140.0*Hartree,
    )

calculator = LCAOCalculator(
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    )

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('Cenral.nc', bulk_configuration)

# -------------------------------------------------------------
# Optimize Geometry
# -------------------------------------------------------------
bulk_configuration = OptimizeGeometry(
    bulk_configuration,
    max_forces=0.2*eV/Ang,
    max_steps=200,
    max_step_length=0.2*Ang,
    trajectory_filename=None,
    disable_stress=True,
    optimizer_method=LBFGS(),
)
nlsave('Cenral.nc', bulk_configuration)
nlprint(bulk_configuration)
