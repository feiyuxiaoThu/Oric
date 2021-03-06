# -*- coding: utf-8 -*-
# -------------------------------------------------------------
# Bulk Configuration
# -------------------------------------------------------------

# Set up lattice
vector_a = [8.61799719338, 0.0, 0.0]*Angstrom
vector_b = [0.0, 8.61799719338, 0.0]*Angstrom
vector_c = [0.0, 0.0, 38.73374375]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Phosphorus, Phosphorus, Phosphorus, Phosphorus, Phosphorus, Gallium,
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
fractional_coordinates = [[ 0.55          ,  0.05          ,  0.131472816257],
                          [ 0.95          ,  0.25          ,  0.131472816257],
                          [ 0.35          ,  0.45          ,  0.131472816257],
                          [ 0.75          ,  0.65          ,  0.131472816257],
                          [ 0.15          ,  0.85          ,  0.131472816257],
                          [ 0.75          ,  0.15          ,  0.166652090659],
                          [ 0.15          ,  0.35          ,  0.166652090659],
                          [ 0.55          ,  0.55          ,  0.166652090659],
                          [ 0.95          ,  0.75          ,  0.166652090659],
                          [ 0.35          ,  0.95          ,  0.166652090659],
                          [ 0.25          ,  0.15          ,  0.201831365061],
                          [ 0.65          ,  0.35          ,  0.201831365061],
                          [ 0.05          ,  0.55          ,  0.201831365061],
                          [ 0.45          ,  0.75          ,  0.201831365061],
                          [ 0.85          ,  0.95          ,  0.201831365061],
                          [ 0.05          ,  0.05          ,  0.237010639463],
                          [ 0.45          ,  0.25          ,  0.237010639463],
                          [ 0.85          ,  0.45          ,  0.237010639463],
                          [ 0.25          ,  0.65          ,  0.237010639463],
                          [ 0.65          ,  0.85          ,  0.237010639463],
                          [ 0.55          ,  0.05          ,  0.272189913865],
                          [ 0.95          ,  0.25          ,  0.272189913865],
                          [ 0.35          ,  0.45          ,  0.272189913865],
                          [ 0.75          ,  0.65          ,  0.272189913865],
                          [ 0.15          ,  0.85          ,  0.272189913865],
                          [ 0.75          ,  0.15          ,  0.307369188268],
                          [ 0.15          ,  0.35          ,  0.307369188268],
                          [ 0.55          ,  0.55          ,  0.307369188268],
                          [ 0.95          ,  0.75          ,  0.307369188268],
                          [ 0.35          ,  0.95          ,  0.307369188268],
                          [ 0.25          ,  0.15          ,  0.34254846267 ],
                          [ 0.65          ,  0.35          ,  0.34254846267 ],
                          [ 0.05          ,  0.55          ,  0.34254846267 ],
                          [ 0.45          ,  0.75          ,  0.34254846267 ],
                          [ 0.85          ,  0.95          ,  0.34254846267 ],
                          [ 0.05          ,  0.05          ,  0.377727737072],
                          [ 0.45          ,  0.25          ,  0.377727737072],
                          [ 0.85          ,  0.45          ,  0.377727737072],
                          [ 0.25          ,  0.65          ,  0.377727737072],
                          [ 0.65          ,  0.85          ,  0.377727737072],
                          [ 0.542619535875,  0.048804616488,  0.411700010109],
                          [ 0.954911716749,  0.248143043506,  0.413415478704],
                          [ 0.346603953976,  0.449459260981,  0.4115826037  ],
                          [ 0.756671594659,  0.641220098622,  0.412578891575],
                          [ 0.148280499829,  0.850961243726,  0.41124686875 ],
                          [ 0.75101561887 ,  0.156749959223,  0.446661163659],
                          [ 0.150933753358,  0.346525418469,  0.448097938908],
                          [ 0.549026411332,  0.543164664297,  0.44824707783 ],
                          [ 0.949076912231,  0.753027475586,  0.450115843321],
                          [ 0.338739737768,  0.941179804061,  0.446058720873],
                          [ 0.247786262647,  0.146886521317,  0.48271786995 ],
                          [ 0.640259716366,  0.342918207082,  0.481011154986],
                          [ 0.038526741415,  0.555215832599,  0.482770032796],
                          [ 0.454210089822,  0.750262288454,  0.483227930189],
                          [ 0.847617667678,  0.961592918323,  0.481320976793],
                          [ 0.046790345122,  0.062035439989,  0.516837117424],
                          [ 0.443478387275,  0.25093790246 ,  0.51910021967 ],
                          [ 0.842061207748,  0.450969455793,  0.516567127537],
                          [ 0.254456918176,  0.644350968314,  0.517679284104],
                          [ 0.641800004119,  0.85557288746 ,  0.518444014984],
                          [ 0.431119966735,  0.17631222882 ,  0.54616766501 ],
                          [ 0.924651022013,  0.166984767693,  0.545465046892],
                          [ 0.177716888836,  0.431837856812,  0.546838786758],
                          [ 0.677287000668,  0.417134627689,  0.548965634637],
                          [ 0.420527392878,  0.668380360706,  0.54735121444 ],
                          [ 0.924532022362,  0.674411027726,  0.547589873057],
                          [ 0.177220436658,  0.928225059144,  0.550050507209],
                          [ 0.675521413859,  0.912261810345,  0.547514050152],
                          [ 0.291554867553,  0.041945696176,  0.575774512293],
                          [ 0.799795214018,  0.056154032279,  0.576674693529],
                          [ 0.050881906379,  0.29933144422 ,  0.574885357119],
                          [ 0.550634092083,  0.304693401085,  0.575968215995],
                          [ 0.295392795904,  0.550990598552,  0.578645204868],
                          [ 0.802060008293,  0.554355343641,  0.57655945649 ],
                          [ 0.046464098417,  0.79523183959 ,  0.576747978637],
                          [ 0.55148643266 ,  0.799907178127,  0.577129693013],
                          [ 0.182967244031,  0.176440134849,  0.603768714627],
                          [ 0.676750431092,  0.17026047189 ,  0.607674984338],
                          [ 0.425931700389,  0.420865537321,  0.607153701055],
                          [ 0.913545165871,  0.417623691857,  0.607842494796],
                          [ 0.172400105802,  0.673733902396,  0.608346338011],
                          [ 0.671699730209,  0.66704625542 ,  0.603350664507],
                          [ 0.428504312016,  0.92700860074 ,  0.605831948277],
                          [ 0.92057480629 ,  0.92237761559 ,  0.604881066677],
                          [ 0.048742168434,  0.047181039491,  0.634813519679],
                          [ 0.539744538474,  0.046080919547,  0.633918577008],
                          [ 0.300073970676,  0.294675553172,  0.634988176298],
                          [ 0.805723036189,  0.311593359506,  0.633461782512],
                          [ 0.052685434286,  0.539370459381,  0.635623227958],
                          [ 0.549638775381,  0.547524142442,  0.636383542952],
                          [ 0.290416193569,  0.804769199705,  0.634739346241],
                          [ 0.795606857018,  0.793089762985,  0.635148010624],
                          [ 0.425         ,  0.175         ,  0.664312480123],
                          [ 0.925         ,  0.175         ,  0.664312480123],
                          [ 0.175         ,  0.425         ,  0.664312480123],
                          [ 0.675         ,  0.425         ,  0.664312480123],
                          [ 0.425         ,  0.675         ,  0.664312480123],
                          [ 0.925         ,  0.675         ,  0.664312480123],
                          [ 0.175         ,  0.925         ,  0.664312480123],
                          [ 0.675         ,  0.925         ,  0.664312480123],
                          [ 0.3           ,  0.05          ,  0.693486009211],
                          [ 0.8           ,  0.05          ,  0.693486009211],
                          [ 0.05          ,  0.3           ,  0.693486009211],
                          [ 0.55          ,  0.3           ,  0.693486009211],
                          [ 0.3           ,  0.55          ,  0.693486009211],
                          [ 0.8           ,  0.55          ,  0.693486009211],
                          [ 0.05          ,  0.8           ,  0.693486009211],
                          [ 0.55          ,  0.8           ,  0.693486009211],
                          [ 0.175         ,  0.175         ,  0.7226595383  ],
                          [ 0.675         ,  0.175         ,  0.7226595383  ],
                          [ 0.425         ,  0.425         ,  0.7226595383  ],
                          [ 0.925         ,  0.425         ,  0.7226595383  ],
                          [ 0.175         ,  0.675         ,  0.7226595383  ],
                          [ 0.675         ,  0.675         ,  0.7226595383  ],
                          [ 0.425         ,  0.925         ,  0.7226595383  ],
                          [ 0.925         ,  0.925         ,  0.7226595383  ],
                          [ 0.05          ,  0.05          ,  0.751833067388],
                          [ 0.55          ,  0.05          ,  0.751833067388],
                          [ 0.3           ,  0.3           ,  0.751833067388],
                          [ 0.8           ,  0.3           ,  0.751833067388],
                          [ 0.05          ,  0.55          ,  0.751833067388],
                          [ 0.55          ,  0.55          ,  0.751833067388],
                          [ 0.3           ,  0.8           ,  0.751833067388],
                          [ 0.8           ,  0.8           ,  0.751833067388],
                          [ 0.425         ,  0.175         ,  0.781006596477],
                          [ 0.925         ,  0.175         ,  0.781006596477],
                          [ 0.175         ,  0.425         ,  0.781006596477],
                          [ 0.675         ,  0.425         ,  0.781006596477],
                          [ 0.425         ,  0.675         ,  0.781006596477],
                          [ 0.925         ,  0.675         ,  0.781006596477],
                          [ 0.175         ,  0.925         ,  0.781006596477],
                          [ 0.675         ,  0.925         ,  0.781006596477],
                          [ 0.3           ,  0.05          ,  0.810180125566],
                          [ 0.8           ,  0.05          ,  0.810180125566],
                          [ 0.05          ,  0.3           ,  0.810180125566],
                          [ 0.55          ,  0.3           ,  0.810180125566],
                          [ 0.3           ,  0.55          ,  0.810180125566],
                          [ 0.8           ,  0.55          ,  0.810180125566],
                          [ 0.05          ,  0.8           ,  0.810180125566],
                          [ 0.55          ,  0.8           ,  0.810180125566],
                          [ 0.175         ,  0.175         ,  0.839353654654],
                          [ 0.675         ,  0.175         ,  0.839353654654],
                          [ 0.425         ,  0.425         ,  0.839353654654],
                          [ 0.925         ,  0.425         ,  0.839353654654],
                          [ 0.175         ,  0.675         ,  0.839353654654],
                          [ 0.675         ,  0.675         ,  0.839353654654],
                          [ 0.425         ,  0.925         ,  0.839353654654],
                          [ 0.925         ,  0.925         ,  0.839353654654],
                          [ 0.05          ,  0.05          ,  0.868527183743],
                          [ 0.55          ,  0.05          ,  0.868527183743],
                          [ 0.3           ,  0.3           ,  0.868527183743],
                          [ 0.8           ,  0.3           ,  0.868527183743],
                          [ 0.05          ,  0.55          ,  0.868527183743],
                          [ 0.55          ,  0.55          ,  0.868527183743],
                          [ 0.3           ,  0.8           ,  0.868527183743],
                          [ 0.8           ,  0.8           ,  0.868527183743]]

# Set up configuration
bulk_configuration = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add tags
bulk_configuration.addTags('Left',  [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
                                     13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                                     26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                                     39, 40, 41, 42, 43, 44])
bulk_configuration.addTags('Right', [ 84,  85,  86,  87,  88,  89,  90,  91,  92,  93,
                                      94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
                                     104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
                                     114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
                                     124, 125, 126, 127, 128, 129, 130, 131, 132, 133,
                                     134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
                                     144, 145, 146, 147, 148, 149, 150, 151, 152, 153,
                                     154, 155])

# -------------------------------------------------------------
# Calculator
# -------------------------------------------------------------

potentialSet = Tersoff_Powell_2007()
calculator = TremoloXCalculator(parameters=potentialSet)
calculator.setVerletListsDelta(0.25*Angstrom)

bulk_configuration.setCalculator(calculator)
nlprint(bulk_configuration)
bulk_configuration.update()
nlsave('central.nc', bulk_configuration)

# -------------------------------------------------------------
# Optimize Geometry
# -------------------------------------------------------------
rigid_indices_0 = [ 84,  85,  86,  87,  88,  89,  90,  91,  92,  93,
                    94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
                   104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
                   114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
                   124, 125, 126, 127, 128, 129, 130, 131, 132, 133,
                   134, 135, 136, 137, 138, 139, 140, 141, 142, 143,
                   144, 145, 146, 147, 148, 149, 150, 151, 152, 153,
                   154, 155]
rigid_indices_1 = [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,
                   13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                   39, 40, 41, 42, 43, 44]
constraints = [RigidBody(rigid_indices_0),
               RigidBody(rigid_indices_1)]

bulk_configuration = OptimizeGeometry(
    bulk_configuration,
    max_forces=0.25*eV/Ang,
    max_steps=200,
    max_step_length=0.2*Ang,
    constraints=constraints,
    trajectory_filename='central.nc',
    disable_stress=True,
    optimizer_method=LBFGS(),
)
nlsave('central.nc', bulk_configuration)
nlprint(bulk_configuration)
