import abjad


def edit_bass_voice(score, durated_reservoir):
    """
    Edits bass voice.
    """

    voice = score['Bass Voice']

    voice[-3:] = '<e, e>\maxima <d, d>\longa <c, c>\maxima <b,>\longa <a,>\maxima r4 r2.'
