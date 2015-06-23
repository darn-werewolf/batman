from __future__ import print_function
import numpy as np
import math
import matplotlib.pyplot as plt
from .transitmodel import *

def test():
	#print("Starting tests...")
	failures = 0

	params = TransitParams()
	params.t0 = 0.
	params.per = 1.0
	params.rp = 0.115
	params.a = 15.23
	params.inc = 1.555*180./math.pi
	params.ecc = 0.
	params.w = 90. 
	params.u = np.array([0.0, 0.7, 0.0, -0.3])
	params.limb_dark = "nonlinear"

	#t = np.linspace(0.01, 0.02, 1000)
	t  = np.linspace(-params.per/100., params.per/100., 1000)
	err_max = 0.5
	
	"""m = TransitModel(params, t, err_max)
	nonlinear_lc = m.LightCurve(params)
	err = m.calc_err()
	if err > err_max: failures += 1"""

	params.limb_dark = "quadratic"
	params.u = [0.1,0.3]
	m = TransitModel(params, t, err_max)
	for i in range(10000): 
		quadratic_lc = m.LightCurve(params)
	#	plt.plot(quadratic_lc)
	#	plt.show()

	#if np.max(np.abs(quadratic_lc-nonlinear_lc))*1.0e6 > err_max: failures += 1

	#print("Tests finished with " + "{0}".format(failures) + " failures")

	

