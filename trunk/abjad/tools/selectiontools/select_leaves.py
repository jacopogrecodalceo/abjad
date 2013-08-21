# -*- encoding: utf-8 -*-


def select_leaves(
    expr=None,
    start=0,
    stop=None,
    leaf_classes=None,
    recurse=True,
    allow_discontiguous_leaves=False,
    ):
    r'''Selects leaves in `expr`.

    ..  container:: example
    
        **Example.** Select leaves in staff:

        ::

            >>> staff = Staff()
            >>> staff.extend(r"c'8 d'8 \times 2/3 { e'8 g'8 f'8 }")
            >>> staff.extend(r"g'8 f'8 \times 2/3 { e'8 c'8 d'8 }")
            >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> f(staff)
            \new Staff {
                c'8
                d'8
                \times 2/3 {
                    e'8
                    g'8
                    f'8
                }
                g'8
                f'8
                \times 2/3 {
                    e'8
                    c'8
                    d'8
                }
            }

        ::

            >>> selection = selectiontools.select_leaves(staff)

        ::
            
            >>> selection
            ContiguousLeafSelection(...)

        ::

            >>> for leaf in selection:
            ...     leaf
            Note("c'8")
            Note("d'8")
            Note("e'8")
            Note("g'8")
            Note("f'8")
            Note("g'8")
            Note("f'8")
            Note("e'8")
            Note("c'8")
            Note("d'8")

    Returns contiguous leaf selection or free leaf selection.
    '''
    from abjad.tools import componenttools
    from abjad.tools import iterationtools
    from abjad.tools import leaftools
    from abjad.tools import selectiontools
    Selection = selectiontools.Selection
    leaf_classes = leaf_classes or (leaftools.Leaf,)
    if recurse:
        expr = iterationtools.iterate_leaves_in_expr(expr)
    music = [
            component for component in expr
            if isinstance(component, leaf_classes)
            ]
    music = music[start:stop]
    if allow_discontiguous_leaves:
        selection = selectiontools.FreeLeafSelection(music=music)
    else:
        assert Selection._all_are_contiguous_components_in_same_logical_voice(
            music)
        selection = selectiontools.ContiguousLeafSelection(music=music)
    return selection
