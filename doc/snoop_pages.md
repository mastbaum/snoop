SNOOP Monitoring Categories
===========================
Meta
----
* Run number
* Run type
* Last update time
* Last update GTID
* SNOOP memory/CPU usage

Alarm Summary
-------------
* Alarm name / status

CMA Summary
-----------
* CMA Alarm / status

Start of Run Checks
-------------------
* Link to "neutrino report cards"
  * Neutrino report card: per run pass/fail for status tests: Run mask (!&UC), crate mask, trigger mask, trigger thresholds, pulser enabled, pedestals disabled, percent of nhit triggers per crate, blind flasher check, trigger on/hv off check, event rate, pulse gt rate, orphan count, no zero occ normal/owl/butt/neck paddle cards, inter-event timing, clock drift, cgt/cmos errors, lgi select errors

Run Statistics
==============
Summary
-------
* Duration
* Events analyzed
* Orphans
* lone orphans*
* owl/neck/butt events*
* event rate*
* dispatch rate

Last run record
---------------
* Date
* Time
* ID
* Valid GTID

Run type
--------
* List of names

Crate mask
----------
* List of IDs

Source mask
-----------
* List of names

Last TRIG record
----------------
* GTID
* Lockout width

Trigger Settings (table)
------------------------
* Masked in
* Threshold
* Zero
* Zero diff
* Alarm zero
* Alarm zero diff

Other triggers masked in
------------------------
* List of names

NHIT statistics
---------------
* Mean*
* Count nhit < 30*
* Count nhit >= 30*
* Mean orphan nhit

Triggers (table)
----------------
* ID
* Name
* Number
* Short frac/rate/mean/rms
* Run frac/rate/mean/rms

Derived trigger stats
---------------------
* N100M/PULSEGT
* ESHI/PULSEGT

Solar neutrino flux
-------------------
* CC: short/run/units
* ES: short/run/units
* NC: short/run/units
* Solar core temp: short/run/units

Event pathologies (table)
-----------------
* Rows: Sharkfin, flasher, neck, junk, elecpickup, muon, muonfollower, lightwater, unidentified h/m/l, burst
* Short count, rate, mean nhit, percent
* Run count, rate, mean nhit, percent

Analog Measurement Board
------------------------
* All data: differential (mean), integral (mean), peak (mean)
* PGT: differential (mean), integral (mean), peak (mean)
* Nhit > 30 && !ESUMHI: (integral-integral pedestal)/nhits, (peak-peak pedestal)/nhits

Timing and CMOS
---------------
* Mean 10MHz vs 50MHz inter-event timing difference
* Peak 10MHz vs 50MHz clock drift
* Count of consecutive event pairs < 410 ns apart
* Count of CGT SYNC CLEAR 16 errors
* Count of CGT SYNC CLEAR 24 errors
* Count of CMOS SYNC CLEAR 16 errors
* Count of PMT LGI SELECT errors

DQXX
----
* File, date
* Sequencers enabled (value out of total)
* 20ns triggers enabled
* 100ns triggers enabled
* HV resistors pulled
* HV cables pulled
* Channels not operational
* Relays enabled
* OWL/BUTT/NECK relays enabled

Occupancy
---------
* Mean/low/high occupancy: short/med/run
* Total/normal tubes: short/med/run
* Zero/low/high occupancy tubes: short/med/run
* Zero occupancy PCs
* Zero occupancy NECK/OWL/BUTTs
* Zero occupancy BUTT/OWL PCs
* Crate occupancies (short)

Charge distribution plots
-------------------------
* Links to QHS, QHL, QLX, T plots

Base current and CMOS rate information
--------------------------------------
* Empty

CMA information
---------------
* Link to graphs

Hydrophone information
----------------------
* Link to graphs

NCD information
---------------
* Empty

NHIT Trigger Monitor
--------------------
* NHIT100MED: number, timestamp
* NHIT100HI: number, timestamp
* NHIT20: number, timestamp

Data Flow
=========
* Current run
* UGND: date, last file on disk, last transferred AG, tape ID, last to tape, tape usage
* AGND: date, last file on disk, last transferred to surf, tape ID, last to tape, tape usage

