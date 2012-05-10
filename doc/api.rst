snoop Python API
================

snoop.processors_all
--------------------

Built-in processors. To make snoop use them, create symlinks to them inside ``snoop/processors``. Alternatively, construct your ``ProcessorBlock`` with a list of ``Processor`` instances instead of a list of paths.

.. automodule:: snoop.processors_all.count
   :members:

.. automodule:: snoop.processors_all.exception
   :members:

.. automodule:: snoop.processors_all.nhit_statistics
   :members:

.. automodule:: snoop.processors_all.slow
   :members:

snoop.core
----------

Core functionality of snoop.

Processors
``````````

.. automodule:: snoop.core.processor
   :members:

Readers
```````

.. automodule:: snoop.core.reader
   :members:

Writers
```````

.. automodule:: snoop.core.writer
   :members:

