# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageManager_go_to_all_scores_01():

    input_ = 'red~example~score m tempo~inventory S q'
    ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores depot',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials directory',
        'Red Example Score (2013) - materials directory - tempo inventory',
        'Abjad IDE - scores depot',
        ]
    assert ide._transcript.titles == titles