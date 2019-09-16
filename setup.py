import setuptools


with open('README.md') as f:
    long_desc = f.read()


setuptools.setup(name='piccup',
                 version='0.1.1',
                 author='Alexander Juda',
                 description="Render HTML from Python using plain data structures, inspired by Clojure's Hiccup",
                 long_description=long_desc,
                 long_description_content_type='text/markdown',
                 url='https://github.com/alexjuda/piccup',
                 packages=setuptools.find_packages(),
                 classifiers=['Development Status :: 3 - Alpha',
                              'Environment :: Web Environment',
                              'License :: OSI Approved :: MIT License',
                              'Programming Language :: Python :: 3',
                              'Topic :: Text Processing :: Markup :: HTML'],
                 python_requires='>=3')
