from setuptools import find_packages, setup

package_name = "agents"
console_scripts = [
    "executable = agents.executable:main",
    "tiny_web_client = agents.chainlit_client.app:main",
]

version = "0.3.1"


setup(
    name=package_name,
    version=version,
    packages=find_packages(exclude=["tests"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Automatika Robotics",
    maintainer_email="contact@automatikarobotics.com",
    description="Build embodied agents with ROS and local ML models",
    license="MIT License Copyright (c) 2024 Automatika Robotics",
    tests_require=["pytest"],
    entry_points={"console_scripts": console_scripts},
)
