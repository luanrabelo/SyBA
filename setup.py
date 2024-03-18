from setuptools import setup

with open("README.md", "r") as fh:
    Readme = fh.read()

setup(
    name = 'SyBA',
    version = '0.0.2',
    description = 'SyBA: a tool and database for standardizing gene names in bacterial genomes.',
    long_description = Readme,
    long_description_content_type="text/markdown",
    author = 'Luan Rabelo',
    author_email = 'luanrabelo@outlook.com',
    maintainer = 'Luan Rabelo',
    maintainer_email = 'luanrabelo@outlook.com',
    url='https://github.com/luanrabelo/SyBA',
    download_url='https://github.com/luanrabelo/SyBA',
    packages=['SyBA'],
    license='MIT License',
    keywords='SyBA Genes Bioinformatics Synonymous',
    install_requires=['requests', 'pandas', 'numpy'],
    classifiers= [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Environment :: Web Environment",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    )