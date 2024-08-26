from setuptools import setup, find_packages

setup(
    name='enbdleap-python-core',
    version='0.1.0',
    description='A Python framework for microservices using Flask or FastAPI with Dependency Injection',
    author='Mohammed Ashfaq Moosa',
    author_email='',
    url='',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'fastapi',
        'flask',
        'injector',
        'python-dotenv',
        'uvicorn',
        'starlette',
    ],
    extras_require={
        'dev': [
            'pytest',
            'flake8',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Beta',
        'Framework :: Flask',
        'Framework :: FastAPI',
    ],
    python_requires='>=3.10',
)
