from setuptools import find_packages, setup

setup(
    name="mars_explorer",
    version="1.0.0",
    keywords="exploration, robotics, environment, agent, rl, gymnasium",
    description="Exploration of unknown areas using lidar",
    install_requires=["gymnasium>=1.2.3", "numpy>=1.19.2", "pygame>=2.0.0"],
    include_package_data=True,
    packages=find_packages(),
    package_data={
        'mars_explorer': ['img/*.png', 'img/*.jpg', 'img/*.jpeg'],
    },
)
