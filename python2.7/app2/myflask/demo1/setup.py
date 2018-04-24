from setuptools import setup, find_packages

setup(
    name = 'lzatest1',
    version = '0.0.1',
    keywords = ('lza'),
    description = 'just a simple test',
    license = 'MIT License',
    install_requires = ['flask'],

    author = 'lza',
    author_email = '318724186@qq.com',
    
    packages = find_packages(),
    platforms = 'any',
)
