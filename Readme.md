# International Baccalaureate Diploma Program - Extended Essay (Computer Science)

## An Analysis of Transient Execution CPU Vulnerability

> How susceptible is Firestorm-M1 and Icestorm-M1 microarchitectures against Spectre Pattern History Table and Spectre Branch Target Buffer?

See the extended essay [here](https://docs.google.com/document/d/1tniHXceWUjvTjvh8Rs5kx8cf3TvMBxwdHr3HIA7PSAI/edit?usp=sharing).

<img src="logo.png" width="512" height="405">


Code for Spectre V1 and V2 PoC and covert channel taken from the paper [Branch Different - Spectre attacks on Apple silicon](https://misc0110.net/files/applespectre_dimva22.pdf).

## Overview
Each folder contains a `Readme.md` with additional documentation.

### [common](common)
Timing and cache maintenance code required by both, the spctre PoC and the covert channel.
The eviction code is a strongly modified version of [evsets](https://github.com/cgvwzq/evsets).

### [covert_channel](covert_channel)
Code of the Covert Channel.

### [spectre](spectre)
Code of Spectre V1 and Spectre V2 PoC.

### [benchmark](benchmark)
Code used for benchmarking timing and eviction
