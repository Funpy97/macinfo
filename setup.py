from distutils.core import setup

setup(
    name='macinfo',
    packages=['macinfo', 'macinfo.modules', 'macinfo.modules.data'],
    version='0.0.4a',
    license='MIT',
    long_description='More information on: https://github.com/Funpy97/macinfo',
    long_description_content_type='text/markdown',
    description='Search mac address info offline in about 29915 tech companies',
    author='Marino Iannarelli',
    author_email='marinoiannarelli97@gmail.com',
    url='https://github.com/Funpy97/macinfo',
    download_url='https://github.com/Funpy97/macinfo/archive/v0.0.4-alpha.tar.gz',
    keywords=['mac address', 'companies', 'whois', 'company'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
)
