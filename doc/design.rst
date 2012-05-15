snoop Design
============

This document outlines the design requirements for a SNOOP replacement, covering features found in both `snoop <http://github.com/mastbaum/snoop>`_ and `woodstock <http://github.com/mastbaum/woodstock>`_.

Design Criteria
---------------
Logic Layer
```````````
* Polls the same data sources as old snoop

  * Dispatcher
  * Alarms
  * DAQ/Computer status
  * Data flow

* Runs forever

  * Cannot crash
  * Cannot be restarted

Data Layer
``````````
* Query over time ranges
* Query fields selecting on other fields
* Caching of large/frequent requests
* Persistent
* Automatic fault recovery or replication

Presentation Layer
``````````````````
* Sensible defaults, highly configurable
* Programmable by non-experts (ASCII templating)
* Alarms immediate but not intrusive
* Plotting of arbitrary data

  * Histograms
  * Time series
  * Scatter plots

Design Choices
--------------
Logic Layer
```````````
* Python daemon

  * Communication through signals
  * start, stop, restart, reload operations
  * Dynamic module reloading while running

* Processor model

  * Arbitrary processor code

    * Aggregated event data
    * Polling external sources

  * Called per event

  * State sampled at regular interval

    * Asynchronous
    * Output handled by writer

      * Push to database
      * Log, email, alarm, ...

Data Layer
``````````
* CouchBase server

  * JSON key/value store
  * High performance

    * Incremental view indexing
    * In-memory caching
    * Clustered

* Python/WSGI interface

  * Implements REST API for client queries

    * Date ranges, SELECT-like operations

Presentation Layer
``````````````````
* snoop Web Interface

  * Templates written in ReST/Markdown with special tags
  * Framework renders templates as HTML + JS (Backbone?)

