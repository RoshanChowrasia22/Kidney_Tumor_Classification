import setuptools

with open('README.md', "r",encoding='utf-8') as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME="Kidney_Tumor_Classification"
AUTHOR_NAME="RoshanChowrasia22"
SRC_REPO="cnnClassifier"
AUTHOR_EMAIL="secret"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="An end to end project for classification using CNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages()
)