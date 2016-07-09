# coding: utf-8
from setuptools import setup, find_packages


setup(
    name='telegram_aiohttp',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'bot = bot.main:main',
        ]
    },
)
