import typing
from abjad.tools import mathtools
from abjad.tools.datastructuretools import Center
from abjad.tools.datastructuretools import Down
from abjad.tools.datastructuretools import Left
from abjad.tools.datastructuretools import Right
from abjad.tools.datastructuretools import Up
from abjad.tools.datastructuretools.Duration import Duration
from abjad.tools.datastructuretools.OrdinalConstant import OrdinalConstant
from abjad.tools.datastructuretools.String import String
from abjad.tools.lilypondnametools.LilyPondContextSetting import \
    LilyPondContextSetting
from abjad.tools.scoretools.Chord import Chord
from abjad.tools.scoretools.Leaf import Leaf
from abjad.tools.scoretools.Note import Note
from abjad.tools.scoretools.Rest import Rest
from abjad.tools.scoretools.Skip import Skip
from .Spanner import Spanner


class GeneralizedBeam(Spanner):
    r'''
    Generalized beam.

    ..  container:: example::

        >>> staff = abjad.Staff("r4 c'8 d'16 e'16 r8 fs'8 g'4")
        >>> abjad.setting(staff).auto_beaming = False
        >>> abjad.show(staff) # doctest: +SKIP

        >>> beam = abjad.GeneralizedBeam()
        >>> abjad.attach(beam, staff[:])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            \with
            {
                autoBeaming = ##f
            }
            {
                r4
                c'8
                [
                \set stemLeftBeamCount = 1
                \set stemRightBeamCount = 2
                d'16
                e'16
                ]
                r8
                fs'8
                g'4
            }

    ..  container:: example

        >>> staff = abjad.Staff("r4 c'8 d'16 e'16 r8 fs'8 g'4")
        >>> abjad.setting(staff).auto_beaming = False
        >>> abjad.show(staff) # doctest: +SKIP

        >>> beam = abjad.GeneralizedBeam(
        ...     isolated_nib_direction=abjad.Right,
        ...     )
        >>> abjad.attach(beam, staff[:])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            \with
            {
                autoBeaming = ##f
            }
            {
                r4
                c'8
                [
                \set stemLeftBeamCount = 1
                \set stemRightBeamCount = 2
                d'16
                e'16
                ]
                r8
                fs'8
                [
                ]
                g'4
            }

    ..  container:: example::

        >>> staff = abjad.Staff("r4 c'8 d'16 e'16 r8 fs'8 g'4")
        >>> abjad.setting(staff).auto_beaming = False
        >>> abjad.show(staff) # doctest: +SKIP

        >>> beam = abjad.GeneralizedBeam(use_stemlets=True)
        >>> abjad.attach(beam, staff[:])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            \with
            {
                autoBeaming = ##f
            }
            {
                r4
                c'8
                [
                \set stemLeftBeamCount = 1
                \set stemRightBeamCount = 2
                d'16
                \set stemLeftBeamCount = 2
                \set stemRightBeamCount = 1
                e'16
                \set stemLeftBeamCount = 1
                \set stemRightBeamCount = 1
                r8
                fs'8
                ]
                g'4
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_durations',
        '_include_long_duration_notes',
        '_include_long_duration_rests',
        '_isolated_nib_direction',
        '_span_points',
        '_use_stemlets',
        '_vertical_direction',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        durations: typing.Iterable[Duration] = None,
        include_long_duration_notes: bool = False,
        include_long_duration_rests: bool = False,
        isolated_nib_direction: OrdinalConstant = None,
        use_stemlets: bool = False,
        vertical_direction: OrdinalConstant = None,
        ) -> None:
        Spanner.__init__(self)
        durations_ = None
        if durations:
            durations_ = tuple(Duration(_) for _ in durations)
        self._durations = durations_
        self._include_long_duration_notes = bool(include_long_duration_notes)
        self._include_long_duration_rests = bool(include_long_duration_rests)
        assert isolated_nib_direction in (Left, Right, None)
        self._isolated_nib_direction = isolated_nib_direction
        if self._durations is not None:
            self._span_points = mathtools.cumulative_sums(self.durations)[1:]
        else:
            self._span_points = [self._get_duration()]
        self._use_stemlets = bool(use_stemlets)
        assert vertical_direction in (Up, Down, Center, None)
        self._vertical_direction = vertical_direction

    ### PRIVATE METHODS ###

    def _get_beam_counts(
        self,
        leaf,
        previous_leaf,
        previous_leaf_is_joinable,
        next_leaf,
        next_leaf_is_joinable,
        ):

        start_offset = self._start_offset_in_me(leaf)
        stop_offset = self._stop_offset_in_me(leaf)
        left, right = None, None

        previous_flag_count = 0
        if previous_leaf is not None:
            previous_flag_count = previous_leaf.written_duration.flag_count
        next_flag_count = 0
        if next_leaf is not None:
            next_flag_count = next_leaf.written_duration.flag_count
        current_flag_count = leaf.written_duration.flag_count

        if previous_leaf_is_joinable and next_leaf_is_joinable:
            if self._is_only_leaf_in_group(start_offset, stop_offset):
                left = 1
                right = current_flag_count
            elif self._is_first_leaf_in_group(start_offset):
                left = 1
                right = current_flag_count
            elif self._is_last_leaf_in_group(stop_offset):
                left = current_flag_count
                right = 1
            else:
                left = min(previous_flag_count, current_flag_count) or 1
                right = min(current_flag_count, next_flag_count) or 1
                if left != current_flag_count and right != current_flag_count:
                    right = current_flag_count

        elif previous_leaf_is_joinable:
            if self._is_first_leaf_in_group(start_offset):
                left = 1
                right = current_flag_count
            elif leaf is self[-1]:
                right = None
                left = current_flag_count

        elif next_leaf_is_joinable:
            if self._is_last_leaf_in_group(stop_offset):
                right = 1
                if leaf is self[0]:
                    left = current_flag_count

        return left, right

    def _get_lilypond_format_bundle(self, leaf):
        bundle = self._get_basic_lilypond_format_bundle(leaf)
        if not self._is_beamable(leaf):
            return bundle
        elif not self.use_stemlets and (
            not isinstance(leaf, Note) and
            not isinstance(leaf, Chord)
            ):
            return bundle
        leaf_ids = [id(_) for _ in self.leaves]
        previous_leaf = leaf._get_leaf(-1)
        previous_leaf_is_joinable = self._leaf_is_joinable(
            previous_leaf, leaf_ids)
        next_leaf = leaf._get_leaf(1)
        next_leaf_is_joinable = self._leaf_is_joinable(next_leaf, leaf_ids)
        left_beam_count, right_beam_count = self._get_beam_counts(
            leaf,
            previous_leaf,
            previous_leaf_is_joinable,
            next_leaf,
            next_leaf_is_joinable,
            )
        if left_beam_count is not None:
            context_setting = LilyPondContextSetting(
                context_property='stemLeftBeamCount',
                value=left_beam_count,
                )
            bundle.update(context_setting)
        if right_beam_count is not None:
            context_setting = LilyPondContextSetting(
                context_property='stemRightBeamCount',
                value=right_beam_count,
                )
            bundle.update(context_setting)
        start_piece, stop_piece = self._get_start_and_stop_pieces(
            leaf,
            previous_leaf,
            next_leaf,
            leaf_ids,
            )
        if start_piece and stop_piece:
            bundle.right.spanner_starts.extend([
                start_piece, stop_piece])
        elif start_piece:
            bundle.right.spanner_starts.append(start_piece)
        elif stop_piece:
            bundle.right.spanner_stops.append(stop_piece)
        return bundle

    def _get_start_and_stop_pieces(
        self,
        leaf,
        previous_leaf,
        next_leaf,
        leaf_ids,
        ):
        start_piece = None
        stop_piece = None
        direction_string = ''
        if self.vertical_direction is not None:
            direction_string = String.to_tridirectional_lilypond_symbol(
                    self.vertical_direction)
        previous_leaf_is_beamable = (
            self._is_beamable(previous_leaf) and
            id(previous_leaf) in leaf_ids
            )
        next_leaf_is_beamable = (
            self._is_beamable(next_leaf) and
            id(next_leaf) in leaf_ids
            )
        if not previous_leaf_is_beamable:
            if not next_leaf_is_beamable:
                if self.isolated_nib_direction is not None:
                    start_piece = f'{direction_string}['
                    stop_piece = ']'
            else:
                start_piece = f'{direction_string}['
        elif not next_leaf_is_beamable:
            stop_piece = ']'
        return start_piece, stop_piece

    def _is_beamable(self, argument, beam_rests=False):
        prototype = (Rest, Skip)
        if beam_rests and isinstance(argument, prototype):
            return True
        if isinstance(argument, Leaf):
            if 0 < argument.written_duration.flag_count:
                if isinstance(argument, (Note, Chord)):
                    return True
                elif self.use_stemlets:
                    return True
        return False

    def _is_first_leaf_in_group(self, start_offset):
        if start_offset in self._span_points:
            return True
        return False

    def _is_last_leaf_in_group(self, stop_offset):
        if stop_offset in self._span_points:
            return True
        return False

    def _is_only_leaf_in_group(self, start_offset, stop_offset):
        if self._is_first_leaf_in_group(start_offset):
            if self._is_last_leaf_in_group(stop_offset):
                return True
        return False

    def _leaf_is_joinable(self, leaf, leaf_ids):
        if id(leaf) not in leaf_ids:
            return False
        if isinstance(leaf, (Note, Chord)):
            if self._is_beamable(leaf):
                return True
            elif self.include_long_duration_notes:
                return True
        else:
            if self._is_beamable(leaf) and self.use_stemlets:
                return True
            elif self.include_long_duration_rests:
                return True
        return False

    ### PUBLIC PROPERTIES ###

    @property
    def durations(self) -> typing.Optional[typing.Tuple[Duration, ...]]:
        '''
        Gets durations for span-beam groupings.
        '''
        return self._durations

    @property
    def include_long_duration_notes(self) -> typing.Optional[bool]:
        '''
        Is true when beam includes long duration notes.
        '''
        return self._include_long_duration_notes

    @property
    def include_long_duration_rests(self) -> typing.Optional[bool]:
        '''
        Is true when beam includes long duration rests.
        '''
        return self._include_long_duration_rests

    @property
    def isolated_nib_direction(self) -> typing.Optional[OrdinalConstant]:
        '''
        Gets direction of isolated nibs.
        '''
        return self._isolated_nib_direction

    @property
    def use_stemlets(self) -> typing.Optional[bool]:
        '''
        Is true when beam uses stemlets.
        '''
        return self._use_stemlets

    @property
    def vertical_direction(self) -> typing.Optional[OrdinalConstant]:
        '''
        Gets vertical direction of beam.
        '''
        return self._vertical_direction
