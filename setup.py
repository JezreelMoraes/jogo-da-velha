from setuptools import setup, find_packages

setup(
    name='meu-app-desktop',
    version='0.1.0',
    author='Seu Nome',
    author_email='seuemail@example.com',
    description='Uma aplicação desktop com interface gráfica.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # Adicione suas dependências aqui, por exemplo:
        'PyQt5',  # Se estiver usando PyQt para a interface gráfica
        # 'tkinter',  # Se estiver usando Tkinter
    ],
    entry_points={
        'console_scripts': [
            'meu-app-desktop=main:main',  # Ajuste conforme necessário
        ],
    },
)