"""Setup configuration for ggoat package."""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read version from __init__.py
def get_version():
    """Get version from package __init__.py file."""
    version_file = os.path.join("src", "ggoat", "__init__.py")
    with open(version_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
    raise RuntimeError("Unable to find version string.")

setup(
    name="ggoat",
    version=get_version(),
    author="ggoat development team",
    author_email="contact@ggoat.dev",
    description="Grammar of Graphics for Python - optimized for Pyodide and browser environments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ggoat/ggoat",
    project_urls={
        "Bug Tracker": "https://github.com/ggoat/ggoat/issues",
        "Documentation": "https://ggoat.readthedocs.io/",
        "Source": "https://github.com/ggoat/ggoat",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "ggoat": ["assets/*.js"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Jupyter",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Minimal core dependencies
    ],
    extras_require={
        "pandas": ["pandas>=1.0.0"],
        "numpy": ["numpy>=1.18.0"],
        "jupyter": ["ipython>=7.0.0", "jupyter>=1.0.0"],
        "letsplot": ["lets-plot>=3.0.0"],
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=22.0.0",
            "isort>=5.10.0",
            "flake8>=4.0.0",
            "mypy>=0.900",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
            "myst-parser>=0.18.0",
            "sphinx-autobuild>=2021.3.14",
            "sphinx-copybutton>=0.5.0",
        ],
        "all": [
            "pandas>=1.0.0",
            "numpy>=1.18.0", 
            "ipython>=7.0.0",
            "lets-plot>=3.0.0",
        ],
    },
    keywords="visualization, plotting, grammar-of-graphics, ggplot, pyodide, jupyter",
    zip_safe=False,
    include_package_data=True,
)