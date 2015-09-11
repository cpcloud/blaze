=======
Install
=======

Installing
~~~~~~~~~~

Blaze can be most easily installed from conda_

::

    conda install blaze

More up-to-date builds are available on the ``blaze`` anaconda channel:
http://anaconda.org/blaze

::

    conda install -c blaze blaze

Blaze may also be installed using ``pip``:

::

    pip install blaze --upgrade

or

::

    pip install git+https://github.com/blaze/blaze  --upgrade

If you are interested in the development version of Blaze you can
obtain the source from Github.

::

    git clone git@github.com:blaze/blaze.git

Anaconda can be downloaded for all platforms here:
https://store.continuum.io/cshop/anaconda/.

Introduction
~~~~~~~~~~~~

To build blaze from source:

::

    python setup.py install

To build the documentation:

::

    cd docs
    make html

To run tests:

::

    py.test --doctest-modules --pyargs blaze

Strict Dependencies
~~~~~~~~~~~~~~~~~~~

Blaze depends on NumPy, Pandas, and a few pure-python libraries.  It should be
easy to install on any Numeric Python setup.

* numpy_ >= 1.7
* pandas_ >= 0.15.0
* datashape_ >= 0.4.6
* odo_ >= 0.3.3
* toolz_ >= 0.7.0
* cytoolz_
* multipledispatch_ >= 0.4.7
* psutil_

Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~

Blaze can help you use a variety of other libraries like ``sqlalchemy`` or
``h5py``.  If these are installed then Blaze will use them.  Some of these are
non-trivial to install.  We recommend installation through ``conda``.

* dynd-python_ >= 0.6.5
* sqlalchemy_ >= 0.8.0
* h5py_
* flask_ >= 0.10.1 (for :mod:`~blaze.server.server`)
* requests_ (for :mod:`~blaze.server.server`)
* pytables_ >= 3.0.0
* pymongo_ >= 2.8
* bcolz_
* numba_
* pyyaml_ (for :mod:`~blaze.server.server`)
* pytest_ >= 2.7.0
* spark_ >= 1.3.0


.. _numpy: http://www.numpy.org/
.. _odo: https://github.com/blaze/odo
.. _h5py: http://docs.h5py.org/en/latest/
.. _pytest: http://pytest.org/latest/
.. _dynd-python: https://github.com/libdynd/dynd-python
.. _datashape: https://github.com/blaze/datashape
.. _pandas: http://pandas.pydata.org/
.. _cytoolz: https://github.com/pytoolz/cytoolz/
.. _sqlalchemy: http://www.sqlalchemy.org/
.. _spark: http://spark.apache.org/
.. _toolz: http://toolz.readthedocs.org/
.. _multipledispatch: http://multiple-dispatch.readthedocs.org/
.. _conda: http://conda.pydata.org/
.. _pymongo: http://api.mongodb.org/python/current/
.. _pytables: http://www.pytables.org/
.. _bcolz: https://github.com/Blosc/bcolz
.. _flask: http://flask.pocoo.org/
.. _requests: http://www.python-requests.org/en/latest/
.. _psutil: https://pythonhosted.org/psutil/
.. _numba: http://numba.pydata.org/
.. _pyyaml: http://pyyaml.org/
