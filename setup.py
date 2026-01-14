from setuptools import setup

setup(
    name='mars_explorer',
    version='0.0.1',
    keywords='exploration, robotics, environment, agent, rl, gymnasium',
    description='Exploration of unknonw areas using lidar',
    install_requires=[
        'gymnasium>=1.2.3',
        'numpy>=1.19.2',
        'pygame>=2.0.0'
    ],
    include_package_data=True,
    py_modules=[]
)
