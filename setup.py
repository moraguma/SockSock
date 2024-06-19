from setuptools import setup, find_namespace_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='socksock',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.3.4',    
    description='A Python library for plug & play RPC',
    url='https://github.com/moraguma/SockSock',
    author='Moraguma',
    author_email='g170603@dac.unicamp.br',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=[            
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python'  # TODO : Specify Python versions
    ],
)