# -*- encoding: utf-8 -*-
from abjad import *


def test_Chord___init___01():
    r'''Init empty chord.
    '''

    chord = Chord([], (1, 4))
    assert chord.lilypond_format == "<>4"


def test_Chord___init___02():
    r'''Init chord with numbers.
    '''

    chord = Chord([2, 4, 5], (1, 4))
    assert chord.lilypond_format == "<d' e' f'>4"


def test_Chord___init___03():
    r'''Init chord with pitch tokens.
    '''

    chord = Chord([('ds', 4), ('ef', 4)], (1, 4))
    assert chord.lilypond_format == "<ds' ef'>4"


def test_Chord___init___04():
    r'''Init chord with pitches.
    '''

    chord = Chord([pitchtools.NamedChromaticPitch('ds', 4), pitchtools.NamedChromaticPitch('ef', 4)], (1, 4))
    assert chord.lilypond_format == "<ds' ef'>4"


def test_Chord___init___05():
    r'''Init chord with pitch token and pitch together.
    '''

    chord = Chord([2, ('ef', 4), pitchtools.NamedChromaticPitch(4)], (1, 4))
    assert chord.lilypond_format == "<d' ef' e'>4"


def test_Chord___init___06():
    r'''Init chord with list of pitch names.
    '''

    chord = Chord(["d'", "ef'", "e'"], (1, 4))
    assert chord.lilypond_format == "<d' ef' e'>4"


def test_Chord___init___07():
    r'''Init chord with LilyPond input string.
    '''

    chord = Chord("<d' ef' e'>4")
    assert chord.lilypond_format == "<d' ef' e'>4"


def test_Chord___init___08():
    r'''Init chord from skip.
    '''

    s = skiptools.Skip((1, 8))
    d = s.written_duration
    c = Chord(s)
    assert isinstance(c, Chord)
    assert dir(s) == dir(skiptools.Skip((1, 4)))
    assert dir(c) == dir(Chord([2, 3, 4], (1, 4)))
    assert c._parent is None
    assert c.written_duration == d


def test_Chord___init___09():
    r'''Init chord from skip.
    '''

    tuplet = tuplettools.FixedDurationTuplet(Duration(2, 8), skiptools.Skip((1, 8)) * 3)
    d = tuplet[0].written_duration
    chord = Chord(tuplet[0])
    assert isinstance(tuplet[0], skiptools.Skip)
    assert isinstance(chord, Chord)
    assert tuplet[0]._parent is tuplet
    assert tuplet[0].written_duration == d
    assert chord._parent is None


def test_Chord___init___10():
    r'''Init chord from containerized skip.
    '''

    voice = Voice(skiptools.Skip((1, 8)) * 3)
    d = voice[0].written_duration
    chord = Chord(voice[0])
    assert isinstance(voice[0], skiptools.Skip)
    assert isinstance(chord, Chord)
    assert voice[0]._parent is voice
    assert voice[0].written_duration == d
    assert chord._parent is None


def test_Chord___init___11():
    r'''Init chord from beamed skip.
    '''

    staff = Staff([Note(0, (1, 8)), skiptools.Skip((1, 8)), Note(0, (1, 8))])
    spannertools.BeamSpanner(staff[:])
    chord = Chord(staff[1])
    assert isinstance(staff[1], skiptools.Skip)
    assert isinstance(chord, Chord)
    assert staff[1]._parent is staff


def test_Chord___init___12():
    r'''Init chord from rest.
    '''

    r = Rest((1, 8))
    d = r.written_duration
    c = Chord(r)
    assert isinstance(c, Chord)
    assert dir(r) == dir(Rest((1, 4)))
    assert dir(c) == dir(Chord([2, 3, 4], (1, 4)))
    assert c._parent is None
    assert c.written_duration == d


def test_Chord___init___13():
    r'''Init chord from tupletized rest.
    '''

    tuplet = tuplettools.FixedDurationTuplet(Duration(2, 8), Rest((1, 8)) * 3)
    d = tuplet[0].written_duration
    chord = Chord(tuplet[0])
    assert isinstance(tuplet[0], Rest)
    assert isinstance(chord, Chord)
    assert tuplet[0]._parent is tuplet
    assert tuplet[0].written_duration == d
    assert chord._parent is None


def test_Chord___init___14():
    r'''Init chord from rest.
    '''

    staff = Staff([Note(0, (1, 8)), Rest((1, 8)), Note(0, (1, 8))])
    spannertools.BeamSpanner(staff[:])
    chord = Chord(staff[1])
    assert isinstance(staff[1], Rest)
    assert isinstance(chord, Chord)
    assert staff[1]._parent is staff
    assert chord._parent is None


def test_Chord___init___15():
    r'''Init chord from note.
    '''

    n = Note(2, (1, 8))
    h, p, d = n.note_head, n.written_pitch, n.written_duration
    c = Chord(n)
    assert isinstance(c, Chord)
    assert dir(n) == dir(Note("c'4"))
    assert dir(c) == dir(Chord([2, 3, 4], (1, 4)))
    assert c.lilypond_format == "<d'>8"
    assert c._parent is None
    assert c.note_heads[0] is not h
    assert c.written_pitches[0] == p
    assert c.written_duration == d


def test_Chord___init___16():
    r'''Init chord from tupletized note.
    '''

    tuplet = tuplettools.FixedDurationTuplet(Duration(2, 8), Note(0, (1, 8)) * 3)
    h, p, d = tuplet[0].note_head, tuplet[0].written_pitch, tuplet[0].written_duration
    chord = Chord(tuplet[0])
    assert isinstance(tuplet[0], Note)
    assert isinstance(chord, Chord)
    assert chord.lilypond_format == "<c'>8"
    assert tuplet[0]._parent is tuplet
    assert chord.note_heads[0] is not h
    assert chord.written_pitches[0] == p
    assert chord.written_duration == d


def test_Chord___init___17():
    r'''Init chord from beamed note.
    '''

    staff = Staff(Note(0, (1, 8)) * 3)
    spannertools.BeamSpanner(staff[:])
    chord = Chord(staff[0])
    assert isinstance(staff[0], Note)
    assert isinstance(chord, Chord)
    assert staff[0]._parent is staff


def test_Chord___init___18():
    r'''Init empty chord from LilyPond input string.
    '''

    chord = Chord('<>8.')
    assert isinstance(chord, Chord)
    assert len(chord) == 0


def test_Chord___init___19():
    r'''Init with forced and cautionary accidentals.
    '''

    chord = Chord('<c!? e? g! b>4')
    assert chord.lilypond_format == '<c!? e? g! b>4'


def test_Chord___init___20():
    r'''Init from Note with forced and cautionary accidentals.
    '''

    note = Note("c'!?4")
    chord = Chord(note)
    assert chord.lilypond_format == "<c'!?>4"
