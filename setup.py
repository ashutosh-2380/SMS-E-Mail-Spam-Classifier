from setuptools import setup, find_packages

setup(
    name='email-spam-classifier',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'nltk',
        'pickle',
        'nltk.corpus',
        'nltk.stem.porter',
    ],
    entry_points={
        'console_scripts': [
            'start_app = app.py:main',  
        ],
    },
)
