from setuptools import setup, find_packages

setup(
    name='email-spam-classifier',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'nltk',
        'pickleshare==0.7.5'
    ],
    entry_points={
        'console_scripts': [
            'start_app = app.py:main',  
        ],
    },
)
