import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# activate __version__ variable
exec(open("thingsvision/_version.py").read())

requirements = [
    "ftfy",
    "h5py",
    # "keras-cv-attention-models>=1.3.5",
    "matplotlib",
    "numba",
    "numpy>=1.22.*",
    "open_clip_torch==2.0.*",
    "pandas>=1.3.*",
    "regex",
    "scikit-image",
    "scikit-learn",
    "scipy",
    "tensorflow==2.9.* ; sys_platform != 'darwin' or platform_machine != 'arm64'",
    "tensorflow-macos==2.9.* ; sys_platform == 'darwin' and platform_machine == 'arm64'",
    "timm==0.6.*",
    "torch>=1.13.*",
    "torchvision==0.14.*",
    "torchtyping",
    "tqdm",
    "CLIP",
    # 'CLIP @ git+ssh://git@github.com/openai/CLIP@v1.0#egg=CLIP' # TODO: see issue #111
]

setuptools.setup(
    name="thingsvision",
    version=__version__,
    author="Lukas Muttenthaler",
    author_email="muttenthaler@cbs.mpg.de",
    description="Extracting image features from state-of-the-art neural networks for Computer Vision made easy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ViCCo-Group/thingsvision",
    packages=setuptools.find_packages(),
    license="MIT License",
    install_requires=requirements,
    keywords="feature extraction",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["thingsvision = thingsvision.thingsvision:main"]},
    python_requires=">=3.8",
    dependency_links=[
        "git+https://github.com/openai/CLIP.git",
    ],
)
