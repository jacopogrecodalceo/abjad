# -*- encoding: utf-8 -*-
from abjad.tools.abctools import AbjadObject


class SyntaxNode(AbjadObject):
    r'''A node in an abstract syntax tree (AST).

    Not composer-safe.

    Used internally by LilyPondParser.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        'type',
        'value',
        )

    ### INTIAILIZER ###

    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    ### SPECIAL METHODS ###

    def __getitem__(self, item):
        if isinstance(self.value, (list, tuple)):
            return self.value[item]
        message = 'can not get: {!r}.'.format(item)
        raise Exception(message)

    def __len__(self):
        if isinstance(self.value, (list, tuple)):
            return len(self.value)
        message = 'value must be list or tuple.'
        raise Exception(message)

    def __repr__(self):
        return '{}({}, {})'.format(
            type(self).__name__, 
            self.type, 
            type(self.value),
            )

    def __str__(self):
        return '\n'.join(self._format(self))


    def _format(self, obj, indent=0):
        space = '.  ' * indent
        result = []

        if isinstance(obj, type(self)):
            if isinstance(obj.value, (list, tuple)):
                result.append('%s<%s>: [' % (space, obj.type))
                for x in obj.value:
                    result.extend(self._format(x, indent + 1))
                result[-1] += ' ]'
            else:
                result.append('%s<%s>: %r' % (space, obj.type, obj.value))

        elif isinstance(obj, (list, tuple)):
            result.append('%s[' % space)
            for x in obj:
                result.extend(self._format(x, indent + 1))
            result[-1] += ' ]'

        else:
            result.append('%s%r' % (space, obj))

        return result
