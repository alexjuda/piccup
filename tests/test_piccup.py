import piccup as p


class TestHTML:
    def test_empty(_):
        assert '' == p.html()

    def test_one_simple_tag(_):
        assert ('<button></button>'
                ==
                p.html(['button']))

    def test_one_tag_attrs(_):
        assert ('<button class="my-btn"></button>'
                ==
                p.html(['button', {'class': 'my-btn'}]))

    def test_nested_elements_with_attrs(_):
        assert ('<p class="my-p"><button class="my-btn"></button></p>'
                ==
                p.html(['p', {'class': 'my-p'},
                        ['button', {'class': 'my-btn'}]]))

    def test_nested_elements_no_attrs(_):
        assert ('<p><button></button></p>'
                ==
                p.html(['p',
                        ['button']]))

    def test_parent_attrs_nested_terminal(_):
        assert ('<p class="my-p">yo</p>'
                ==
                p.html(['p', {'class': 'my-p'},
                        'yo']))

    def test_no_parent_attrs_nested_terminal(_):
        assert ('<p>yo</p>'
                ==
                p.html(['p',
                        'yo']))

    def test_seqs(_):
        form = ['ul', [['li', 'first'], ['li', 'second'], ['li', 'third']]]
        assert ('<ul><li>first</li><li>second</li><li>third</li></ul>'
                ==
                p.html(form))


class TestIsTagSeq:
    def test_terminal(_):
        assert not p.is_tag_seq(['abc'])

    def test_tag(_):
        assert not p.is_tag_seq([['p', 'abc']])

    def test_nested_tag_terminal(_):
        assert not p.is_tag_seq([['div',
                                  ['p', 'abc']]])

    def test_nested_empty_tag(_):
        assert not p.is_tag_seq([['div',
                                  ['button']]])

    def test_li_seq(_):
        assert p.is_tag_seq([[['li', 'first'], ['li', 'second'], ['li', 'third']]])

    def test_nested_li_seq(_):
        assert not p.is_tag_seq([['ul',
                                  [['li', 'first'], ['li', 'second'], ['li', 'third']]]])


class TestNormalizeElement:
    def test_tag_only(_):
        assert ('button', {}, []) == p.normalize_element('button')

    def test_tag_attrs(_):
        assert ('button', {'class': 'my-btn'}, []) == p.normalize_element('button', {'class': 'my-btn'})

    def test_tag_attrs_content(_):
        child = ('button', {'class': 'my-btn'}, [])
        assert ('p', {'class': 'my-p'}, [child]) == p.normalize_element('p', {'class': 'my-p'}, child)
