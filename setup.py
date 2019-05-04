from setuptools import setup

setup (
    name = 'Snapshots',
    version = '0.1',
    author = 'Roushan Khan',
    author_email = 'roushan.khan@outlook.com',
    description = 'Script to manage AWS ec2 volumes snapshots lifecycle',
    license = 'GPLv3+',
    packages =  ['Scripts'],
    url = 'https://github.com/roushankhan/SnapShotsManager',
    install_requires = [
        'click',
        'boto3'
    ],
    entry_points = '''
        [console_scripts]
        scripts=scripts.Snapshots:cli
    ''',
)