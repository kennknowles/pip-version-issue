This repo contains a dependency set up to illustrate a limitation / bug in pip. The dependencies are like so:

    intermediate-package:
        boto==2.3.0

    main-package:
        boto>=2.3.0
        intermediate-package


The issue is that `pip install main-package` will install boto-2.5.2 when boto-2.3.0 is the version that makes sense.

Exact steps to reproduce, starting in a clone of this repo:

    mkvirtualenv pip-version-issue
    (cd intermediate-package && python setup.py sdist)
    cp intermediate-package/dist/*.tar.gz fake-pypi/intermediate-package/
    pip install --extra-index-url "file://$PWD/fake-pypi" -e main-package

You'll see stuff installed, including boto-2.5.2, and then output like this:

    Successfully installed boto intermediate-package main-package
    Cleaning up...

But intermediate-package does not have its requirements met.
