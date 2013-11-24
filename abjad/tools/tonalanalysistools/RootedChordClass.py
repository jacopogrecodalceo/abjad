# -*- encoding: utf-8 -*-
from abjad.tools import markuptools
from abjad.tools import pitchtools
from abjad.tools.pitchtools import PitchClassSet


class RootedChordClass(PitchClassSet):
    '''A rooted chord class.

    ..  container:: example

        G major triad in root position:

        ::

            >>> tonalanalysistools.RootedChordClass('g', 'major')
            GMajorTriadInRootPosition

    ..  container:: example

        G dominant seventh in root position:

        ::

            >>> tonalanalysistools.RootedChordClass('g', 'dominant', 7)
            GDominantSeventhInRootPosition

    Note that notions like a G dominant seventh represent an entire class of
    chords because there are many different spacings and registrations of a G
    dominant seventh.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_bass',
        '_chord_quality',
        '_root',
        )

    _cardinality_to_extent = {
        3: 5,
        4: 7,
        5: 9,
        6: 11,
        7: 13,
        }

    _extent_to_cardinality = {
        5: 3,
        7: 4,
        9: 5,
        11: 6,
        13: 7,
        }

    _extent_to_extent_name = {
        5: 'triad',
        7: 'seventh',
        9: 'ninth',
        11: 'eleventh',
        13: 'thirteenth',
        }

    ### CONSTRUCTOR ###

    def __init__(self, root, *args):
        from abjad.tools import tonalanalysistools
        root = pitchtools.NamedPitchClass(root)
        chord_quality = tonalanalysistools.RootlessChordClass(*args)
        npcs = []
        for hdi in chord_quality:
            mdi = pitchtools.NamedInterval(hdi)
            npc = root + mdi
            npcs.append(npc)
        bass = npcs[0]
        PitchClassSet.__init__(
            self,
            tokens=npcs,
            item_class=pitchtools.NamedPitchClass,
            )
        self._root = root
        self._chord_quality = chord_quality
        self._bass = bass

    ### SPECIAL METHODS ###

    def __eq__(self, arg):
        if isinstance(arg, type(self)):
            if self.root == arg.root:
                if self.chord_quality == arg.chord_quality:
                    if self.inversion == arg.inversion:
                        return True
        return False

    def __ne__(self, arg):
        return not self == arg

    def __repr__(self):
        root = str(self.root).title()
        quality = self.chord_quality._title_case_name
        return root + quality

    ### PRIVATE PROPERTIES ###

    @property
    def _markup_root(self):
        if self.chord_quality._quality_string in (
            'major', 'augmented', 'dominant'):
            root = str(self.root).upper()
        else:
            root = str(self.root).lower()
        if len(root) == 2:
            adjustment = r'\hspace #-0.5 \raise #1 \fontsize #-3'
            if root[-1].lower() == 's':
                root = root[0] + r'{} \sharp'.format(adjustment)
            elif root[-1].lower() == 'f':
                root = root[0] + r'{} \flat'.format(adjustment)
            else:
                print self
                raise ValueError('unknown note name: {}'.format(root))
        return root

    @property
    def _markup_symbol(self):
        circle = r'\draw-circle #0.35 #0 ##f'
        if self.chord_quality._quality_string == 'augmented':
            return '+'
        elif self.chord_quality._quality_string == 'diminished':
            return circle
        elif self.chord_quality._quality_string == 'half diminished':
            line = r"\draw-line #'(1 . 1)"
            markup = r'\concat {{ {} \hspace #-0.85 \raise #-0.5 {} }}'.format(
                circle, line)
            return markup
        elif self.chord_quality._quality_string == 'major' and \
            5 < self.extent.number:
            return 'M'
        elif self.chord_quality._quality_string == 'minor' and \
            5 < self.extent.number:
            return 'm'
        else:
            return ''

    ### PUBLIC PROPERTIES ###

    @property
    def bass(self):
        return self._bass

    @property
    def cardinality(self):
        return len(self)

    @property
    def extent(self):
        from abjad.tools import tonalanalysistools
        extent = self.cardinality_to_extent(self.cardinality)
        return tonalanalysistools.ChordExtent(extent)

    @property
    def figured_bass(self):
        extent, inversion = self.extent, self.inversion
        if extent.number == 5:
            if inversion == 0:
                return ''
            elif inversion == 1:
                return '6/3'
            elif inversion == 2:
                return '6/4'
        elif extent.number == 7:
            if inversion == 0:
                return '7'
            elif inversion == 1:
                return '6/5'
            elif inversion == 2:
                return '4/3'
            elif inversion == 3:
                return '4/2'
        elif extent.number == 9:
            if inversion == 0:
                return ''
            elif inversion == 1:
                raise NotImplementedError
            elif inversion == 2:
                raise NotImplementedError
            elif inversion == 3:
                raise NotImplementedError
            elif inversion == 4:
                raise NotImplementedError

    @property
    def inversion(self):
        return self._chord_quality.inversion

    @property
    def markup(self):
        markup = [self._markup_root, self._markup_symbol, self.figured_bass]
        markup = ''.join(markup)
        markup = r'\fontsize #1 {} \hspace #-0.5'.format(self._markup_root)
        symbol = self._markup_symbol
        if symbol:
            markup += r' \hspace #0.5 \raise #1 \fontsize #-3 {}'.format(
                symbol)
            if 'circle' in symbol:
                if 'sharp' in self._markup_root:
                    markup += r' \hspace #0'
                else:
                    markup += r' \hspace #-1.2'
        inversion = self.figured_bass
        if inversion:
            inv = r" \raise #1 \fontsize #-3 \override #'(baseline-skip . 1.5)"
            inv += r' \column {{ {} }}'.format(' '.join(inversion.split('/')))
            markup += inv
        return markuptools.Markup(markup, Down)

    @property
    def chord_quality(self):
        return self._chord_quality

    @property
    def quality_pair(self):
        chord_quality = self.chord_quality
        return chord_quality.quality_string, chord_quality.extent_name

    @property
    def root(self):
        return self._root

    @property
    def root_string(self):
        capitalized_qualities = ('major', 'dominant', 'augmented')
        symbolic_name = self.root.pitch_class_label
        letter, accidental = symbolic_name[0], symbolic_name[1:]
        if self.chord_quality.quality_string in capitalized_qualities:
            letter = letter.upper()
        else:
            letter = letter.lower()
        return letter + accidental

    ### PUBLIC METHODS ###

    @staticmethod
    def cardinality_to_extent(cardinality):
        r'''Change `cardinality` to extent.

        ..  container:: example

            **Example:** tertian chord with four pitch classes
            qualifies as a seventh chord:

            ::

                >>> tonalanalysistools.RootedChordClass.cardinality_to_extent(4)
                7

        Returns integer.
        '''
        return RootedChordClass._cardinality_to_extent[cardinality]

    @staticmethod
    def extent_to_cardinality(extent):
        r'''Change `extent` to cardinality.

        ..  container:: example

            **Example:** tertian chord with extent of seven
            comprises four pitch-clases:

            ::

                >>> tonalanalysistools.RootedChordClass.extent_to_cardinality(7)
                4

        Returns integer.
        '''
        return RootedChordClass._extent_to_cardinality[extent]

    @staticmethod
    def extent_to_extent_name(extent):
        r'''Change `extent` to extent name.

        ..  container:: example

            **Example:** extent of seven is a seventh:

            ::

                >>> tonalanalysistools.RootedChordClass.extent_to_extent_name(7)
                'seventh'

        Returns string.
        '''
        return RootedChordClass._extent_to_extent_name[extent]

    def transpose(self):
        raise NotImplementedError
