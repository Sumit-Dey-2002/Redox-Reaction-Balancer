import unittest
import half_cell_reaction as hcr


class TestBalanceAcidic(unittest.TestCase):
    # 1: ClO3¯ + SO2 ---> SO42¯ + Cl¯
    def test_1(self):
        # Reduction Half Reaction
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': -1}}
        # 6H+ + ClO(3-) + 6e- ---> Cl- + 3H2O
        output_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 6, 'charge': +5},
                                'product': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 6, 'charge': -1}}

        # Oxidation Half Reaction
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 2, 'hydrogen': 0, 'charge': 0},
                               'product': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -2}}
        # 2H2O + SO2(+1) ---> SO4(2-) + 4H+ + e-
        output_oxidation_rxn = {'reagent': {'central_atom': 3, 'oxygen': 12, 'hydrogen': 12, 'charge': 0},
                                'product': {'central_atom': 3, 'oxygen': 12, 'hydrogen': 12, 'charge': 6}}

        input_reduction_rxn = hcr.balance_acid(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_acid(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in acidic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in acidic medium')

    # 2: H2S + NO3¯ ---> S8 + NO
    def test_2(self):
        # Reduction Half Reaction
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 1, 'hydrogen': 0, 'charge': 0}}
        # TODO: Reduction Half reaction equation
        output_reduction_rxn = {'reagent': {'central_atom': 16, 'oxygen': 48, 'hydrogen': 64, 'charge': +48},
                                'product': {'central_atom': 16, 'oxygen': 48, 'hydrogen': 64, 'charge': 0}}

        # Oxidation Half Reaction
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 2, 'charge': 0},
                               'product': {'central_atom': 8, 'oxygen': 0, 'hydrogen': 0, 'charge': 0}}
        # TODO: oxidation Half reaction equation
        output_oxidation_rxn = {'reagent': {'central_atom': 24, 'oxygen': 0, 'hydrogen': 48, 'charge': 0},
                                'product': {'central_atom': 24, 'oxygen': 0, 'hydrogen': 48, 'charge': +48}}

        input_reduction_rxn = hcr.balance_acid(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_acid(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in acidic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in acidic medium')

    # 3: MnO4¯ + H2S ---> Mn2+ + S8
    def test_3(self):
        # Reduction Half Reaction
        # TODO: Reduction Half reaction equation
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}
        output_reduction_rxn = {'reagent': {'central_atom': 16, 'oxygen': 64, 'hydrogen': 128, 'charge': +112},
                                'product': {'central_atom': 16, 'oxygen': 64, 'hydrogen': 128, 'charge': +32}}

        # Oxidation Half Reaction
        # TODO: oxidation Half reaction equation
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 2, 'charge': 0},
                               'product': {'central_atom': 8, 'oxygen': 0, 'hydrogen': 0, 'charge': 0}}
        output_oxidation_rxn = {'reagent': {'central_atom': 40, 'oxygen': 0, 'hydrogen': 80, 'charge': 0},
                                'product': {'central_atom': 40, 'oxygen': 0, 'hydrogen': 80, 'charge': +80}}

        input_reduction_rxn = hcr.balance_acid(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_acid(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in acidic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in acidic medium')

    # 4: Cu + SO42¯ ---> Cu2+ + SO2
    def test_4(self):
        # Reduction Half Reaction
        # TODO: Reduction Half reaction equation
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -2},
                               'product': {'central_atom': 1, 'oxygen': 2, 'hydrogen': 0, 'charge': 0}}
        output_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 4, 'charge': +2},
                                'product': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 4, 'charge': 0}}

        # Oxidation Half Reaction
        # TODO: oxidation Half reaction equation
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': 0},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}
        output_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': 0},
                                'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}

        input_reduction_rxn = hcr.balance_acid(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_acid(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in acidic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in acidic medium')

    # 5: MnO4¯ + CH3OH ---> CH3COOH + Mn2+
    def test_5(self):
        # Reduction Half Reaction
        # TODO: Reduction Half reaction equation
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}
        output_reduction_rxn = {'reagent': {'central_atom': 4, 'oxygen': 16, 'hydrogen': 0, 'charge': 28},
                                'product': {'central_atom': 4, 'oxygen': 8, 'hydrogen': 0, 'charge': +8}}

        # Oxidation Half Reaction
        # TODO: oxidation Half reaction equation
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 1, 'hydrogen': 4, 'charge': 0},
                               'product': {'central_atom': 2, 'oxygen': 2, 'hydrogen': 4, 'charge': 0}}
        output_oxidation_rxn = {'reagent': {'central_atom': 10, 'oxygen': 10, 'hydrogen': 40, 'charge': 0},
                                'product': {'central_atom': 10, 'oxygen': 10, 'hydrogen': 40, 'charge': +20}}

        input_reduction_rxn = hcr.balance_acid(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_acid(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in acidic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in acidic medium')

    # 6: MnO4¯ + H2O2 ---> Mn2+ + O2
    def test_6(self):
        # Reduction Half Reaction
        # TODO: Reduction Half reaction equation
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}
        output_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1},
                                'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}

        # Oxidation Half Reaction
        # TODO: oxidation Half reaction equation
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': 0},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}
        output_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': 0},
                                'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}

        input_reduction_rxn = hcr.balance_acid(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_acid(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in acidic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in acidic medium')

    # 7: VO2+ + MnO4¯ ---> V(OH)4+ + Mn2+
    def test_7(self):
        # Reduction Half Reaction
        # TODO: Reduction Half reaction equation
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}
        output_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': +7},
                                'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +2}}

        # Oxidation Half Reaction
        # TODO: oxidation Half reaction equation
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 1, 'hydrogen': 0, 'charge': +2},
                               'product': {'central_atom': 1, 'oxygen': 1, 'hydrogen': 1, 'charge': +4}}
        output_oxidation_rxn = {'reagent': {'central_atom': 5, 'oxygen': 5, 'hydrogen': 0, 'charge': +15},
                                'product': {'central_atom': 5, 'oxygen': 5, 'hydrogen': 5, 'charge': +20}}

        input_reduction_rxn = hcr.balance_acid(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_acid(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in acidic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in acidic medium')

    # 8: Cr2O72¯ + Cl¯ ---> Cr3+ + Cl2
    def test_8(self):
        # Reduction Half Reaction
        # TODO: Reduction Half reaction equation
        input_reduction_rxn = {'reagent': {'central_atom': 2, 'oxygen': 7, 'hydrogen': 0, 'charge': -2},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': +3}}
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 2, 'oxygen': 0, 'hydrogen': 0, 'charge': 0}}

        # Oxidation Half Reaction
        # TODO: oxidation Half reaction equation
        output_reduction_rxn = {'reagent': {'central_atom': 2, 'oxygen': 7, 'hydrogen': 14, 'charge': +12},
                                'product': {'central_atom': 2, 'oxygen': 7, 'hydrogen': 14, 'charge': +6}}
        output_oxidation_rxn = {'reagent': {'central_atom': 6, 'oxygen': 0, 'hydrogen': 0, 'charge': -6},
                                'product': {'central_atom': 6, 'oxygen': 0, 'hydrogen': 0, 'charge': 0}}

        input_reduction_rxn = hcr.balance_acid(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_acid(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in acidic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in acidic medium')


class TestBalanceBasic(unittest.TestCase):
    # 1: NH3 + ClO¯ ---> N2H4 + Cl¯
    def test_1(self):
        # Reduction Half Reaction
        # 2H2O + ClO¯ ---> Cl¯ + H2O + 2OH¯
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 1, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': -1}}
        output_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 4, 'charge': -1},
                                'product': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 4, 'charge': -3}}

        # Oxidation Half Reaction
        # 2OH¯ + 2NH3 ---> N2H4 + 2H2O
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 3, 'charge': 0},
                               'product': {'central_atom': 2, 'oxygen': 0, 'hydrogen': 4, 'charge': 0}}
        output_oxidation_rxn = {'reagent': {'central_atom': 2, 'oxygen': 2, 'hydrogen': 8, 'charge': -2},
                                'product': {'central_atom': 2, 'oxygen': 2, 'hydrogen': 8, 'charge': 0}}

        input_reduction_rxn = hcr.balance_base(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_base(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in basic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in basic medium')

    # 2: Br¯ + MnO4¯ ---> MnO2 + BrO3¯
    def test_2(self):
        # Reduction Half Reaction
        # 6OH¯ + Br¯ ---> BrO3¯ + 3H2O
        input_reduction_rxn = {'reagent': {'central_atom': 1, 'oxygen': 4, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 2, 'hydrogen': 0, 'charge': 0}}
        output_reduction_rxn = {'reagent': {'central_atom': 2, 'oxygen': 12, 'hydrogen': 8, 'charge': -2},
                                'product': {'central_atom': 2, 'oxygen': 12, 'hydrogen': 8, 'charge': -8}}
        # Oxidation Half Reaction
        # 4H2O + 2MnO4¯ ---> 2MnO2 + 8OH¯
        input_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 0, 'hydrogen': 0, 'charge': -1},
                               'product': {'central_atom': 1, 'oxygen': 3, 'hydrogen': 0, 'charge': -1}}
        output_oxidation_rxn = {'reagent': {'central_atom': 1, 'oxygen': 6, 'hydrogen': 6, 'charge': -7},
                                'product': {'central_atom': 1, 'oxygen': 6, 'hydrogen': 6, 'charge': -1}}

        input_reduction_rxn = hcr.balance_base(input_reduction_rxn)
        input_oxidation_rxn = hcr.balance_base(input_oxidation_rxn)

        (input_reduction_rxn, input_oxidation_rxn) = hcr.balance_electron(input_reduction_rxn, input_oxidation_rxn)

        self.assertDictEqual(input_reduction_rxn, output_reduction_rxn, 'Reduction in basic medium')
        self.assertDictEqual(input_oxidation_rxn, output_oxidation_rxn, 'Oxidation in basic medium')
