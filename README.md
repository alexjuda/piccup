# piccup

![PyPI](https://img.shields.io/pypi/v/piccup?style=flat)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/piccup?style=flat)

**[EXPERIMENTAL]**

Render HTML from Python using plain data structures, inspired by Clojure's Hiccup.

## Installation

```
pip install piccup
```

## Usage

piccup allows you to write HTML using plain Python data structures.

```python
>>> p.html(['p', 'hello'])
'<p>hello</p>'
```

Each HTML node is defined using `[element, attributes, contents]` triple. `element` string is required, `attributes` dict and `contents` object are optional.

```python
>>> p.html(['a',
            {'href': 'http://example.com'}, 
            'Click Me'])
'<a href="http://example.com">Click Me</a>'
```

Nested HTML nodes are passed to `contents`.

```python
>>> p.html(['ul', 
            [['li', 'first'], 
             ['li', 'second'], 
             ['li', 'third']]])
'<ul><li>first</li><li>second</li><li>third</li></ul>'
```

piccup uses simple data structures, so you can write normal Python code instead of a foreign templating language.

```python
>>> p.html(['ul',
            [['li', {'class': 'link-item'},
              ['a', {'href': 'http://example.com/{}'.format(e)}, e]]
             for e in ['item1', 'item2', 'item3']]])
'<ul><li class="link-item"><a href="http://example.com/item1">item1</a></li><li class="link-item"><a href="http://example.com/item2">item2</a></li><li class="link-item"><a href="http://example.com/item3">item3</a></li></ul>'
```
