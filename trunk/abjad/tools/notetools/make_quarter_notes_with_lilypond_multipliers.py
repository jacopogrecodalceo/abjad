# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import sequencetools


def make_quarter_notes_with_lilypond_multipliers(pitches, multiplied_durations):
    r'''Make quarter notes with `pitches` and `multiplied_durations`:

    ::

        >>> args = [[0, 2, 4, 5], [(1, 4), (1, 5), (1, 6), (1, 7)]]
        >>> notetools.make_quarter_notes_with_lilypond_multipliers(*args)
        [Note("c'4 * 1"), Note("d'4 * 4/5"), Note("e'4 * 2/3"), Note("f'4 * 4/7")]

    Read `pitches` cyclically where the length of `pitches` is
    less than the length of `multiplied_durations`:

    ::

        >>> args = [[0], [(1, 4), (1, 5), (1, 6), (1, 7)]]
        >>> notetools.make_quarter_notes_with_lilypond_multipliers(*args)
        [Note("c'4 * 1"), Note("c'4 * 4/5"), Note("c'4 * 2/3"), Note("c'4 * 4/7")]

    Read `multiplied_durations` cyclically where the length of
    `multiplied_durations` is less than the length of `pitches`:

    ::

        >>> args = [[0, 2, 4, 5], [(1, 5)]]
        >>> notetools.make_quarter_notes_with_lilypond_multipliers(*args)
        [Note("c'4 * 4/5"), Note("d'4 * 4/5"), Note("e'4 * 4/5"), Note("f'4 * 4/5")]

    Return list of zero or more newly constructed notes.
    '''
    from abjad.tools import notetools

    multiplied_durations = [durationtools.Duration(x) for x in multiplied_durations]
    quarter_notes = []

    for pitch, duration in sequencetools.zip_sequences_cyclically(pitches, multiplied_durations):
        quarter_note = notetools.Note(pitch, durationtools.Duration(1, 4))
        duration = durationtools.Duration(duration)
        multiplier = durationtools.Multiplier(duration / durationtools.Duration(1, 4))
        quarter_note.lilypond_duration_multiplier = multiplier
        quarter_notes.append(quarter_note)

    return quarter_notes
