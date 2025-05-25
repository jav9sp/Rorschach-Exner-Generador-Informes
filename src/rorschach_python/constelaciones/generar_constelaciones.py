from constelaciones.cdi import evaluar_cdi
from constelaciones.depi import evaluar_depi
from constelaciones.hvi import evaluar_hvi
from constelaciones.obs import evaluar_obs
from constelaciones.pti import evaluar_pti
from constelaciones.scon import evaluar_scon


def generar_constelaciones(variables, edad):

    constelaciones = {}

    constelaciones.update(evaluar_cdi(variables))
    constelaciones.update(evaluar_depi(variables))
    constelaciones.update(evaluar_hvi(variables))
    constelaciones.update(evaluar_obs(variables))
    constelaciones.update(evaluar_pti(variables))
    constelaciones.update(evaluar_scon(variables, edad))

    return constelaciones
