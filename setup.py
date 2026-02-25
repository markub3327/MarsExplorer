from setuptools import setup, find_packages

setup(
    name='mars_explorer',
    version='1.0.0',
    keywords='exploration, robotics, environment, agent, rl, gymnasium',
    description='Exploration of unknown areas using lidar',
    install_requires=[
        'gymnasium>=1.2.3',
        'numpy>=1.19.2',
        'pygame>=2.0.0'
    ],
    include_package_data=True,
    packages=find_packages(),
)
