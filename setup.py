from setuptools import setup, find_packages

setup(
    name='print',
    version='1.0',
    author='dae',
    author_email='pixilreal@gmail.com',
    description='console input/output but better.',
    long_description='',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
    install_requires=['rich'],
)
