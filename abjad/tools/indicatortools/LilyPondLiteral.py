import typing
from abjad.tools.abctools.AbjadValueObject import AbjadValueObject
from abjad.tools.systemtools.FormatSpecification import FormatSpecification
from abjad.tools.systemtools.LilyPondFormatBundle import LilyPondFormatBundle
from abjad.tools.systemtools.StorageFormatManager import StorageFormatManager


class LilyPondLiteral(AbjadValueObject):
    r'''
    LilyPond literal.

    ..  container:: example

        Dotted slur:

        >>> staff = abjad.Staff("c'8 d'8 e'8 f'8")
        >>> slur = abjad.Slur()
        >>> abjad.attach(slur, staff[:])
        >>> literal = abjad.LilyPondLiteral(r'\slurDotted')
        >>> abjad.attach(literal, staff[0])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
                \slurDotted
                c'8
                (
                d'8
                e'8
                f'8
                )
            }

    ..  container:: example

        Use the absolute before and absolute after format slots like this:

        >>> staff = abjad.Staff("c'8 d'8 e'8 f'8")
        >>> abjad.attach(abjad.Slur(), staff[:])
        >>> literal = abjad.LilyPondLiteral(r'\slurDotted')
        >>> abjad.attach(literal, staff[0])
        >>> literal = abjad.LilyPondLiteral('', format_slot='absolute_before')
        >>> abjad.attach(literal, staff[0])
        >>> literal = abjad.LilyPondLiteral(
        ...     '% before all formatting',
        ...     format_slot='absolute_before',
        ...     )
        >>> abjad.attach(literal, staff[0])
        >>> literal = abjad.LilyPondLiteral('', format_slot='absolute_after')
        >>> abjad.attach(literal, staff[-1])
        >>> abjad.show(staff) # doctest: +SKIP

        ..  docs::

            >>> abjad.f(staff)
            \new Staff
            {
            <BLANKLINE>
                % before all formatting
                \slurDotted
                c'8
                (
                d'8
                e'8
                f'8
                )
            <BLANKLINE>
            }

    ..  container:: example

        LilyPond literals can be tagged:

        >>> staff = abjad.Staff("c'8 d'8 e'8 f'8")
        >>> abjad.attach(abjad.Slur(), staff[:])
        >>> literal = abjad.LilyPondLiteral(r'\slurDotted')
        >>> abjad.attach(literal, staff[0], tag='RED')
        >>> abjad.show(staff) # doctest: +SKIP

        >>> abjad.f(staff)
        \new Staff
        {
            \slurDotted %! RED
            c'8
            (
            d'8
            e'8
            f'8
            )
        }

    ..  container:: example

        Multiline input is allowed:

        >>> staff = abjad.Staff("c'8 d'8 e'8 f'8")
        >>> abjad.attach(abjad.Slur(), staff[:])
        >>> lines = [
        ...     r'\stopStaff',
        ...     r'\startStaff',
        ...     r'\once \override Staff.StaffSymbol.color = #red',
        ...     ]
        >>> literal = abjad.LilyPondLiteral(lines)
        >>> abjad.attach(literal, staff[2], tag='RED')
        >>> abjad.show(staff) # doctest: +SKIP

        >>> abjad.f(staff)
        \new Staff
        {
            c'8
            (
            d'8
            \stopStaff %! RED
            \startStaff %! RED
            \once \override Staff.StaffSymbol.color = #red %! RED
            e'8
            f'8
            )
        }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_argument',
        '_format_slot',
        )

    _allowable_format_slots = (
        'absolute_after',
        'absolute_before',
        'after',
        'before',
        'closing',
        'opening',
        'right',
        )

    _can_attach_to_containers = True

    _format_leaf_children = False

    ### INITIALIZER ###

    def __init__(
        self,
        argument: typing.Union[str, typing.List[str]] = '',
        format_slot: str = 'opening',
        ) -> None:
        self._argument = argument
        assert format_slot in self._allowable_format_slots, repr(format_slot)
        self._format_slot = format_slot

    ### SPECIAL METHODS ###

    def __format__(self, format_specification='') -> str:
        '''
        Formats LilyPond literal.
        '''
        if format_specification in ('', 'storage'):
            return StorageFormatManager(self).get_storage_format()
        assert format_specification == 'lilypond'
        return str(self.argument)

    ### PRIVATE METHODS ###

    def _get_format_pieces(self):
        if isinstance(self.argument, str):
            return [self.argument]
        assert isinstance(self.argument, list)
        return self.argument[:]

    def _get_format_specification(self):
        names = []
        if not self.format_slot == 'opening':
            names.append('format_slot')
        return FormatSpecification(
            client=self,
            storage_format_args_values=[self.argument],
            storage_format_kwargs_names=names,
            storage_format_is_indented=False,
            )

    def _get_lilypond_format_bundle(self, component=None):
        bundle = LilyPondFormatBundle()
        format_slot = bundle.get(self.format_slot)
        pieces = self._get_format_pieces()
        format_slot.commands.extend(pieces)
        return bundle

    ### PUBLIC PROPERTIES ###

    @property
    def argument(self) -> typing.Union[str, typing.List[str]]:
        r'''
        Gets argument of LilyPond literal.

        ..  container:: example

            >>> literal = abjad.LilyPondLiteral(r'\slurDotted')
            >>> literal.argument
            '\\slurDotted'

        '''
        return self._argument

    @property
    def format_slot(self) -> str:
        '''
        Gets format slot of LilyPond literal.

        ..  container:: example

            >>> literal = abjad.LilyPondLiteral(r'\slurDotted')
            >>> literal.format_slot
            'opening'

        '''
        return self._format_slot

    ### PUBLIC METHODS ###

    @staticmethod
    def list_allowable_format_slots() -> typing.Tuple[str, ...]:
        '''
        Lists allowable format slots.

        ..  container:: example

            >>> for slot in abjad.LilyPondLiteral.list_allowable_format_slots():
            ...     slot
            ...
            'absolute_after'
            'absolute_before'
            'after'
            'before'
            'closing'
            'opening'
            'right'

        '''
        return LilyPondLiteral._allowable_format_slots
