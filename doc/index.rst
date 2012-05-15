.. snoop documentation master file, created by
   sphinx-quickstart on Thu May 10 10:50:50 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to snoop's documentation!
=================================
snoop is an online data processing and monitoring tool developed for the SNO+ experiment. It reads event data from a file or `avalanche <http://github.com/mastbaum/avalanche>`_ dispatcher and calculates statistics. It is used to monitor the quality of the data being taken.

Overview
--------
snoop is based on "processor model," not unlike RAT. Processors are called for each event, and may operate on and store that data as needed. Processors are "sampled" with a user-defined period. When sampled, a processor creates a document, which is subsequently written out (probably to a database).

With this model, there are two main classes of processors:

1. Processors that look at every event, gathering data, and when sampled compute and returns statistics related to that data
2. Processors that ignore events, and perform some action when sampled, like query a server to get its disk usage

In either case, a document is produced that represents a snapshot of the parameters the processor cares about.

snoop can only get the samples to a database; the user interface layer is handled by separate software, e.g.::

    data stream --Reader-> snoop --Writer-> database --REST API-> woodstock -> client

`woodstock <http://github.com/mastbaum/woodstock>`_ was developed as a front-end.

Installation
------------
snoop is packaged with ``setuptools`` for easy installation. To install directly from the repository, run::

    $ pip install -e git+git://github.com/mastbaum/snoop.git#egg=snoop

Usage
-----
snoop is intended to be run as a daemon, but additionally can be run in the foreground or used from Python.

You can communicate with snoop processes using signals, most importantly SIGUSR1 (10), which will reload processors from the configured processor path. If processors define a ``load`` function, this is used to copy state from the old processor instances to the new ones upon reloading.

Configuration
`````````````
snoop is configured using a Python module as a configuration file. The following must be defined:

* ``sample_period``: The time between samples, in seconds
* ``processor_paths``: List of Python paths to processors, as (path, fromlist) tuples
* ``writer``: A ``Writer`` subclass instance with which to handle output
* ``reader``: A ``Reader`` subclass instance, from which events will be read

``processor_kwargs``, a ``{'name': dict}`` dictionary may also be defined to supply keyword arguments to processors.

The default configuration file path is ``./config.py``.

Daemon
``````

To run snoop as a daemon::

    $ snoop -d [/path/to/config.py]

CLI
```

To run snoop on the command line::

    $ snoop [/path/to/config.py]

Python module
`````````````

To use snoop from Python::

    >>> import snoop

All of snoop's functionality is available in Python modules -- see API documentation for detail details.

History
=======
This software is completely distinct from the old snoop used in SNO, sharing only the name and purpose.

Documentation
=============

.. toctree::
   :maxdepth: 2

   api
   design

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

