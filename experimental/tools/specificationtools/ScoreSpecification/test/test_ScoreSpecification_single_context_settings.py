from abjad.tools import *
from experimental.tools import specificationtools


def test_ScoreSpecification_single_context_settings_01():

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    assert not score_specification.single_context_settings

    red_segment = score_specification.append_segment(name='red')
    assert not score_specification.single_context_settings
    assert not red_segment.single_context_settings

    red_segment.set_time_signatures([(4, 8), (3, 8)])
    assert not score_specification.single_context_settings
    assert not red_segment.single_context_settings

    score = score_specification.interpret()
    assert len(score_specification.single_context_settings) == 1
    assert len(red_segment.single_context_settings) == 1
