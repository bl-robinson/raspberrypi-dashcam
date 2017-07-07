from setuptools import setup

setup(
    name='dashcam',
    version='1.0',
    description='Python Dashcam Module for the raspberry pi',
    author='Ben Robinson',
    author_email='roaming.b.robinson@gmail.cmo',
    packages=['dashcam',
              ],
    install_requires=["python-daemon",
                      "picamera"],
    entry_points={
        "console_scripts": [
            "dashcam=dashcam.dashcam:main"
        ]
    }
)
