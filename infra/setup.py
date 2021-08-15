import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="infra",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "infra"},
    packages=setuptools.find_packages(where="infra"),

    install_requires=[
        "aws-cdk.core==1.118.0",
        "aws-cdk.aws-ec2==1.118.0",
        "aws-cdk.aws-autoscaling==1.118.0",
        "aws-cdk.aws-s3-notifications==1.118.0",
        "aws-cdk.aws-lambda-event-sources==1.118.0",
        "aws-cdk.aws-codedeploy==1.118.0",
        "aws-cdk.aws-codebuild==1.118.0",
        "aws-cdk.aws-codepipeline==1.118.0",
        "aws-cdk.aws-codecommit==1.118.0",
        "aws-cdk.aws-codepipeline-actions==1.118.0",
        "aws-cdk.aws-cloudfront==1.118.0",
        "aws-cdk.aws-cloudfront-origins==1.118.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
