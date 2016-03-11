from setuptools import setup

setup(
    name='DSFacebookVideo',
    version='1.0.0.0',
    description='Easily download videos from Facebook. You can use as program or as module!',
    url='https://github.com/DiSiqueira/DSFacebookVideo',
    author='Diego Siqueira',
    author_email='dieg0@live.com',
    license='MIT',
    package_dir={'DSFacebookVideo': 'src'},
    packages=['DSFacebookVideo'],
    zip_safe=False,
    keywords=['download', 'thread', 'speed', 'resume', 'multi', 'simple', 'facebook', 'video'],
    entry_points=
    {
        'console_scripts':
            [
                'dsfbvideo = DSFacebookVideo:main',
                'dsfacebookvideo = DSFacebookVideo:main',
            ],
    },
    install_requires=['DSDownload', 'facebook-python-sdk']
)
