from setuptools import find_packages, setup
from typing import List

hypen_E_dot = "-e ."
def get_requirements(file_path: str) -> List[str]:

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hypen_E_dot in requirements:
            requirements.remove(hypen_E_dot)

    return requirements

setup(
    name="tech_tweet_sentiment_dashboard",
    version="0.0.1",
    author="Yash Jaiswar",
    author_email="yash.jaiswar9955@gmail.com",
    description="An end-to-end MLOps project for analyzing sentiment of tech tweets and visualizing results in a dashboard",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JaiswarYash/Tech-Tweet-Sentiment-Dashboard.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)