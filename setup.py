from setuptools import find_packages, setup

setup(
    name='meu-app-desktop',
    version='0.1.0',
    author='Seu Nome',
    author_email='seuemail@example.com',
    description='Uma aplicação desktop com interface gráfica.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'PyQt5',
        'pyqt5-tools'
        'Flask',
    ],
    entry_points={
        'console_scripts': [
            'meu-app-desktop=main:main',
        ],
    },
)
