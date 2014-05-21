# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_StylesheetWrangler_repository_status_01():
    r'''Works with stylesheet library.
    '''

    input_ = 'y rst q'
    score_manager._run(pending_input=input_)
    title = 'On branch master'

    assert title in score_manager._transcript.titles


def test_StylesheetWrangler_repository_status_02():
    r'''Works with Git-managed score.
    '''

    input_ = 'red~example~score y rst q'
    score_manager._run(pending_input=input_)
    title = 'On branch master'

    assert title in score_manager._transcript.titles


def test_StylesheetWrangler_repository_status_03():
    r'''Works with Subversion-managed score.
    '''

    score_name = score_manager._score_package_wrangler._find_svn_score_name()
    if not score_name:
        return

    input_ = '{} y rst q'.format(score_name)
    score_manager._run(pending_input=input_)

    assert '> rst' in score_manager._transcript.first_lines