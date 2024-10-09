## Additonal flags and options
There is alot more options you can use for all the commands that we did not get into in this tutorial but these can all be found using

`py-spy record -h`{{exec}}

And you can ofcourse change `record`{{}} to any of the other subcommands `dump`{{}} and `top`{{}} here.
Some of the options you can use that is important are:

`--rate` 
Which determines how often you are sampling if you increase this number precision increases but overhead also increases. This is by default `100`{{}} times per second

`--duration`
Which determines how long the sampling will run. This is by default `unlimited`{{}}

`--subprocesses`
This allows py-spy to not only profile the main Python process but also any subprocesses it spawns, which can be useful if your program has multiple processes.

`--nonblocking`
This is maybe the most important one that we did not use, because this ensures that during the profiling the Python process is not paused.
One reason to not use this is that this may cause reading errors during sampling, and therefore we recommend not using it if it is possible to cause abit of overhead to the program.