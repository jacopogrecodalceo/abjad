# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_ScorePackageWrangler_go_to_score_stylesheets_01():
    r'''From scores to stylesheets depot.
    '''

    input_ = 'Y q'
    ide._run(input_=input_)
    titles = [
        'Abjad IDE - scores depot',
        'Abjad IDE - stylesheets depot',
        ]
    assert ide._transcript.titles == titles