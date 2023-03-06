from setuptools import setup, find_packages

setup(
    name='Pyrebase4Lite',
    version='0.1.1',
    url='https://github.com/kengoon/Pyrebase4Lite',
    description='A simple python wrapper for the Firebase API with current deps',
    author='Kenechukwu Akubue',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='Firebase',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests>=2.19.1',
        'requests_toolbelt>=0.7.1',
    ]
)
