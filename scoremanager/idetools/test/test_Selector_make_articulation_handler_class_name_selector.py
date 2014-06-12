# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
session = scoremanager.idetools.Session(is_test=True)


def test_Selector_make_articulation_handler_class_name_selector_01():

    selector = scoremanager.idetools.Selector(session=session)
    selector = selector.make_articulation_handler_class_name_selector()
    selector._session._is_test = True
    input_ = 'reiterated'
    result = selector._run(input_=input_)

    assert result == 'ReiteratedArticulationHandler'