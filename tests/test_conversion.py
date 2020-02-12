# coding: utf-8
from typing import Optional
import unicodedata
import unittest
from uyghur.conversion import uey2uly, presentation2basic


class UEY2ULYTestCase(unittest.TestCase):
    def assertConvertTo(self, uey: str, uly: str):
        self.assertEqual(uey2uly(uey), uly)

    def test_qol(self):
        # \u0642\u0648\u0644
        self.assertConvertTo("قول", "qol")
        # \uFED7\uFEEE\uFEDD
        self.assertConvertTo("ﻗﻮﻝ", "qol")

    def test_bash(self):
        # \u0628\u0627\u0634
        self.assertConvertTo("باش", "bash")
        # \uFE91\uFE8E\uFEB5
        self.assertConvertTo("ﺑﺎﺵ", "bash")

    def test_put(self):
        self.assertConvertTo("پۇت", "put")
    
    def test_köz(self):
        self.assertConvertTo("كۆز", "köz")

    def test_kitab(self):
        # \u0643\u0649\u062A\u0627\u0628
        self.assertConvertTo("كىتاب", "kitab")
        # \uFEDB\uFBE9\uFE98\uFE8E\FE8F
        self.assertConvertTo("ﻛﯩﺘﺎﺏ", "kitab")

    def test_weten(self):
        # \u06CB\u06D5\u062A\u06D5\u0646
        self.assertConvertTo("ۋەتەن", "weten")
        # \uFBDE\uFEE9\uFE97\uFEEA\uFEE5
        self.assertConvertTo("ﯞﻩﺗﻪﻥ", "weten")

    def test_tomur(self):
        self.assertConvertTo("تومۇر", "tomur")

    def test_kömür(self):
        self.assertConvertTo("كۆمۈر", "kömür")

    def test_ëlëktir(self):
        # \u0626\u06D0\u0644\u06D0\u0643\u062A\u0649\u0631
        self.assertConvertTo("ئېلېكتىر", "ëlëktir")
        # \uFBF8\uFEE0\uFBE7\uFEDC\uFE98\uFBE9\uFEAE
        self.assertConvertTo("ﯸﻠﯧﻜﺘﯩﺮ", "ëlëktir")

    def test_chaydan(self):
        self.assertConvertTo("چايدان", "chaydan")

    def test_zhurnal(self):
        self.assertConvertTo("ژۇرنال", "zhurnal")

    def test_Shinjang(self):
        self.assertConvertTo("شىنجاڭ", "Shinjang")

    def test_ghelibe(self):
        self.assertConvertTo("غەلىبە", "ghelibe")

    def test_anar(self):
        self.assertConvertTo("ئانار", "anar")

    def test_enjür(self):
        self.assertConvertTo("ئەنجۈر", "enjür")

    def test_orda(self):
        self.assertConvertTo("ئوردا", "orda")

    def test_urush(self):
        self.assertConvertTo("ئۇرۇش", "urush")

    def test_ördek(self):
        self.assertConvertTo("ئۆردەك", "ördek")

    def test_üzüm(self):
        self.assertConvertTo("ئۈزۈم", "üzüm")

    def test_ëlan(self):
        self.assertConvertTo("ئېلان", "ëlan")

    def test_inkas(self):
        self.assertConvertTo("ئىنكاس", "inkas")

    def test_inik_u0027ana(self):
        self.assertConvertTo("ئىنىكئانا", "inik'ana")

    def test_Es_u0027et(self):
        self.assertConvertTo("ئەسئەت", "Es'et")

    def test_radi_u0027o(self):
        self.assertConvertTo("رادىئو", "radi'o")

    def test_mes_u0027ul(self):
        self.assertConvertTo("مەسئۇل", "mes'ul")

    def test_qari_u0027örük(self):
        self.assertConvertTo("قارىئۆرۈك", "qari'örük")

    def test_na_u0027ümid(self):
        self.assertConvertTo("نائۈمىد", "na'ümid")

    def test_it_u0027ëyiq(self):
        self.assertConvertTo("ئىتئېيىق", "it'ëyiq")

    def test_jem_u0027iy(self):
        self.assertConvertTo("جەمئىي", "jem'iy")

    def test_Ez_u0027her(self):
        self.assertConvertTo("ئەزھەر", "Ez'her")

    def test_Is_u0027haq(self):
        self.assertConvertTo("ئىسھاق", "Is'haq")

    def test_Nemen_u0027gan(self):
        self.assertConvertTo("نەمەنگان", "Nemen'gan")

    def test_JKP(self):
        self.assertConvertTo("ج ك پ", "JKP")

    def test_JX(self):
        self.assertConvertTo("ج خ", "JX")

    def test_ShUAR(self):
        self.assertConvertTo("ش ئۇ ئا ر", "ShUAR")

    def test_bu_nëme_u003F(self):
        self.assertConvertTo("بۇ نېمە؟", "bu nëme?")

    def test_men_u002C_sen(self):
        self.assertConvertTo("مەن، سەن", "men, sen")

    def test_adem_u003B_haywan(self):
        self.assertConvertTo("ئادەم؛ ھايۋان", "adem; haywan")

    def test_latin_in_uyghur(self):
        self.assertConvertTo("ABC", unicodedata.lookup('ZERO WIDTH SPACE')+"ABC"+unicodedata.lookup('ZERO WIDTH NO-BREAK SPACE'))

    def test_zero_width_space_and_zero_width_no_break_space(self):
        self.assertConvertTo(unicodedata.lookup('ZERO WIDTH SPACE')+"شىنجاڭ"+unicodedata.lookup('ZERO WIDTH NO-BREAK SPACE'), "شىنجاڭ")

    def test_tatweel(self):
        self.assertConvertTo('\u0626\u0640\u0627', "A")
        self.assertConvertTo('\u0640', "\u0640")

if __name__ == "__main__":
    unittest.main()
