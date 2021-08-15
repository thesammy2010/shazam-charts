from setuptools import setup, find_packages

setup(
    name="shazam-charts",
    version="1.0.0",
    description="Command line tool to get data about Shazam charts",
    author="Leo Parkes-Neptune / TheSammy2010",
    url="https://github.com/thesammy2010/shazam-charts",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    entry_points=("[console_scripts]\n" "shazam-charts=shazam_charts.run:main"),
    package_data={
        "shazam_charts": [
            "shazam-tag-data.jsonl",
        ]
    },
)
