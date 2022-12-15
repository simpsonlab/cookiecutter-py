'''
Setup.py file for the {{cookiecutter.slug}} package.
'''
import setuptools

from {{ cookiecutter.name }} import __version__

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='{{ cookiecutter.slug }}',
    version=__version__,
    author='{{ cookiecutter.author }}',
    author_email='{{ cookiecutter.email }}',
    maintainer='{{ cookiecutter.maintainer }}',
    description='{{ cookiecutter.description }}',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    url='https://github.com/{{ cookiecutter.github }}/{{ cookiecutter.slug }}',
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
    ],
    # uncomment to add executable scripts to a location within PATH
    #entry_points={
        #'console_scripts': [
            #'{{ cookiecutter.slug }}=:main'
        #]
    #},
)
