Solutions to the exercises from _The Little Book of Semaphores_ by Allen Downey.

Also includes a hacked up version of Downey's simulator
[Sync](https://github.com/AllenDowney/Swampy), with the following changes:

 - The GUI is gone: it's intended to be run either on the command line or
   controlled by another program.
 - Function and class definitions are supported in user code. Definitions are
   evaluated atomically; function calls are atomic. The idea is that these can
   be used to test correctness, for use in tests.
 - By default, threads don't loop round back to the top once they're finished.
   You can control this with the --loop option.
 - You can also fail immediately on deadlock, control the delay, or set a
   maximum number of steps with command-line options; run `sync --help` for a
   list.

The idea (illustrated by some of the tests) is to run Sync headlessly under the
control of [Hypothesis](https://hypothesis.works) for program verification.
