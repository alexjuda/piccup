import typing as t


def is_terminal_node(e):
    return isinstance(e, str)


def html(*elements):
    return ''.join(render_tree(e)
                   for e in elements)


def render_tree(root):
    if root is None:
        return ''

    if is_terminal_node(root):
        return root

    tag, attrs, children = normalize_element(*root)
    children_str = ''
    for child in children:
        child_str = render_tree(child)
        children_str += child_str

    if len(attrs) > 0:
        attrs_str = ' {}'.format(render_attrs(attrs))
    else:
        attrs_str = ''
    return '<{}{}>{}</{}>'.format(tag, attrs_str, children_str, tag)


def render_attrs(attrs):
    return ' '.join('{}="{}"'.format(k, v)
                    for k, v in attrs.items())


def normalize_element(*args):
    tag, *rest = filter(None, args)
    if len(rest) == 0:
        attrs = {}
        children = []
    elif isinstance(rest[0], t.Mapping):
        attrs, *children = rest
    else:
        attrs = {}
        children = rest

    if is_tag_seq(children):
        children = children[0]

    return tag, attrs, children


def is_tag(e):
    return isinstance(e, str)


def is_tag_seq(children):
    try:
        return not is_tag(children[0][0])
    except IndexError:
        return False
