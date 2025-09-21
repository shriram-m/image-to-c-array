#!/usr/bin/env python3
"""
Setup script for Image to C Array Converter
"""

from setuptools import setup, find_packages
import os

# Read README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

# Read requirements
def read_requirements():
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name='image-to-c-array',
    version='1.0.0',
    description='Convert images to C header files with pixel data arrays for embedded graphics',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='GitHub User',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/image-to-c-array',
    py_modules=['image_to_c_array'],
    install_requires=read_requirements(),
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'image-to-c-array=image_to_c_array:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
    ],
    keywords='image converter c array embedded graphics vglite rgb565 bgr565',
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/image-to-c-array/issues',
        'Source': 'https://github.com/yourusername/image-to-c-array',
        'Documentation': 'https://github.com/yourusername/image-to-c-array#readme',
    },
)
