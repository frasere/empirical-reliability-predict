##### Class and Function store for Empirical Reliability Predict ####################

# main libraries
import scipy.stats as ss


################################################################################################################
class bearing:
    # bearing class

    def __init__(self, design_params, influence_factors, inf_factor_uncertainty):
        # attributes
        for (
            k,
            v,
        ) in (
            design_params.items()
        ):  # key,values in design_param dict used to set class attributes
            setattr(self, k, v)
        for (
            k,
            v,
        ) in (
            influence_factors.items()
        ):  # key,values in influence_factors dict used to set class attributes
            setattr(self, k, v)
        for (
            k,
            v,
        ) in (
            inf_factor_uncertainty.items()
        ):  # key,values in influence_factors dict used to set class attributes
            setattr(self, k, v)

    def v1(self):
        # calculate rated lubricant velocity
        return 4500 * (self.n ** (-0.83)) * (0.5 * ((self.d + self.d1) ** (-0.5)))

    def Cv(self):
        # calculate lubrication deviation influence factor
        return (self.v1() / self.v0) ** 0.54

    def Ccw(self):
        # calculate lubricant water contamination influence factor
        return 1.176 * (0.21 ** (0.01 - self.cw)) * (self.FR ** 0.25)

    def __brg_random_variates(self):
        # generate lognormal random variates for each inf factor and then combine for complete brg
        Cr_rvs = ss.lognorm.rvs(scale=self.Cr, s=self.Cr_unc, loc=0)
        Cv_rvs = ss.lognorm.rvs(scale=self.Cv(), s=self.Cv_unc, loc=0)
        Ccw_rvs = ss.lognorm.rvs(scale=self.Ccw(), s=self.Ccw_unc, loc=0)
        Ct_rvs = ss.lognorm.rvs(scale=self.Ct, s=self.Ct_unc, loc=0)
        Csf_rvs = ss.lognorm.rvs(scale=self.Csf, s=self.Csf_unc, loc=0)
        Cc_rvs = ss.lognorm.rvs(scale=self.Cc, s=self.Cc_unc, loc=0)
        lamb_b_rvs = ss.lognorm.rvs(
            scale=self.lambda_base, s=self.lambda_base_unc, loc=0
        )
        return lamb_b_rvs * Cr_rvs * Cv_rvs * Ccw_rvs * Ct_rvs * Csf_rvs * Cc_rvs

    def random_variates(self, number_samples):
        # generate defined number of random variates
        return [self.__brg_random_variates() for i in range(0, number_samples)]


##########################################################################################################################


class seal:
    # seal class

    def __init__(self, design_params, influence_factors, inf_factor_uncertainty):
        # attributes
        for (
            k,
            v,
        ) in (
            design_params.items()
        ):  # key,values in design_param dict used to set class attributes
            setattr(self, k, v)
        for (
            k,
            v,
        ) in (
            influence_factors.items()
        ):  # key,values in influence_factors dict used to set class attributes
            setattr(self, k, v)
        for (
            k,
            v,
        ) in (
            inf_factor_uncertainty.items()
        ):  # key,values in influence_factors dict used to set class attributes
            setattr(self, k, v)

    def Cf(self):
        # calculate surface finish factor
        return 2 ** ((self.f - 10) / 38)

    def Ct(self):
        # calculate temperature influence factor influence factor
        return 1 / (2 ** ((self.Tr - self.To) / 18))

    def Ch(self):
        # calculate material hardness influence factor
        return ((self.E / self.C) / 0.55) ** 4.3

    def __seal_random_variates(self):
        # generate lognormal random variates for each inf factor and then combine for complete brg
        Cq_samp = ss.lognorm.rvs(scale=self.Cq, s=self.Cq_unc, loc=0)
        Cv_samp = ss.lognorm.rvs(scale=self.Cv, s=self.Cv_unc, loc=0)
        Cp_samp = ss.lognorm.rvs(scale=self.Cp, s=self.Cp_unc, loc=0)
        Ct_samp = ss.lognorm.rvs(scale=self.Ct(), s=self.Ct_unc, loc=0)
        Ch_samp = ss.lognorm.rvs(scale=self.Ch(), s=self.Ch_unc, loc=0)
        Cf_samp = ss.lognorm.rvs(scale=self.Cf(), s=self.Cf_unc, loc=0)
        Cn_samp = ss.lognorm.rvs(scale=self.Cn, s=self.Cn_unc, loc=0)
        Cpv_samp = ss.lognorm.rvs(scale=self.Cpv, s=self.Cpv_unc, loc=0)
        lambda_base_samp = ss.lognorm.rvs(
            scale=self.lambda_base, s=self.lambda_base_unc, loc=0
        )
        return (
            lambda_base_samp
            * Cp_samp
            * Cq_samp
            * Cv_samp
            * Ch_samp
            * Cf_samp
            * Ct_samp
            * Cn_samp
            * Cpv_samp
        )

    def random_variates(self, number_samples):
        # generate defined number of random variates
        return [self.__seal_random_variates() for i in range(0, number_samples)]


############################################################################################################


class gearbox:
    # gearbox class

    def __init__(self, design_params, influence_factors, inf_factor_uncertainty):
        # attributes
        for (
            k,
            v,
        ) in (
            design_params.items()
        ):  # key,values in design_param dict used to set class attributes
            setattr(self, k, v)
        for (
            k,
            v,
        ) in (
            influence_factors.items()
        ):  # key,values in influence_factors dict used to set class attributes
            setattr(self, k, v)
        for (
            k,
            v,
        ) in (
            inf_factor_uncertainty.items()
        ):  # key,values in influence_factors dict used to set class attributes
            setattr(self, k, v)

    def Cgs(self):
        # influence factor for speed deviation
        return 1 + ((self.V_ratio) ** 0.7)

    def Cgp(self):
        # loading influence factor
        return ((self.L_ratio) / 0.5) ** 0.54

    def Cga(self):
        # gear misallignment factor
        return 12.44 * (self.Ae ** 2.36)

    def __gb_random_variates(self):
        # generate lognormal random variates for each inf factor and then combine for complete brg
        Cgs_samp = ss.lognorm.rvs(scale=self.Cgs(), s=self.Cgs_unc, loc=0)
        Cgp_samp = ss.lognorm.rvs(scale=self.Cgp(), s=self.Cgp_unc, loc=0)
        Cga_samp = ss.lognorm.rvs(scale=self.Cga(), s=self.Cga_unc, loc=0)
        Cv_samp = ss.lognorm.rvs(scale=self.Cv, s=self.Cv_unc, loc=0)
        Cgt_samp = ss.lognorm.rvs(scale=self.Cgt, s=self.Cgt_unc, loc=0)
        Cgv_samp = ss.lognorm.rvs(scale=self.Cgv, s=self.Cgv_unc, loc=0)
        lamb_b_samp = ss.lognorm.rvs(scale=self.lambda_base_unc, s=0.2, loc=0)
        return (
            lamb_b_samp * Cgs_samp * Cgp_samp * Cga_samp * Cv_samp * Cgt_samp * Cgv_samp
        )

    def random_variates(self, number_samples):
        # generate defined number of random variates
        return [self.__gb_random_variates() for i in range(0, number_samples)]


########################################################################################################


class electric_motor:
    # electric motor class

    def __init__(self, design_params, influence_factors, inf_factor_uncertainty):
        # attributes
        for (
            k,
            v,
        ) in (
            design_params.items()
        ):  # key,values in design_param dict used to set class attributes
            setattr(self, k, v)
        for (
            k,
            v,
        ) in (
            influence_factors.items()
        ):  # key,values in influence_factors dict used to set class attributes
            setattr(self, k, v)
        for (
            k,
            v,
        ) in (
            inf_factor_uncertainty.items()
        ):  # key,values in influence_factors dict used to set class attributes
            setattr(self, k, v)

    def Ct(self):
        # temperature factor for windings (less than 180deg so is 1)
        return 2 ** ((self.temp - 40) / 10)

    def Cv(self):
        # voltage variation factor for the windings
        return 2 ** (self.Vd * 10)  # voltage variation factor for the windings

    def lambda_windings(self):
        # motor windings failure rate calculation
        return self.lambda_win_base * self.Ct() * self.Cv() * self.Calt

    def __em_random_variates(self):
        # generate lognormal random variates for each inf factor and then combine for complete brg
        Csf_samp = self.Csf
        lamb_wi_samp = ss.lognorm.rvs(
            scale=self.lambda_windings() * self.op_time,
            s=self.lambda_win_base_unc,
            loc=0,
        )
        lamb_bs_samp = ss.lognorm.rvs(
            scale=self.lambda_bs * self.op_time, s=self.lambda_bs_unc, loc=0
        )
        lamb_stat_samp = ss.lognorm.rvs(
            scale=self.lambda_stat * self.op_time, s=self.lambda_stat_unc, loc=0
        )
        lamb_arm_samp = ss.lognorm.rvs(
            scale=self.lambda_arm * self.op_time, s=self.lambda_arm_unc, loc=0
        )
        lamb_b_samp = ss.lognorm.rvs(
            scale=self.lambda_base * self.op_time, s=self.lambda_base_unc, loc=0
        )
        return (
            (lamb_b_samp * Csf_samp)
            + lamb_wi_samp
            + lamb_bs_samp
            + lamb_stat_samp
            + lamb_arm_samp
        )

    def random_variates(self, number_samples):
        # generate defined number of random variates
        return [self.__em_random_variates() for i in range(0, number_samples)]
