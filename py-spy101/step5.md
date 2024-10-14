## Additional flags and options
There are a lot more options you can use for all of the commands that we did not get into in this tutorial, but these can all be found using.

`py-spy record -h`{{exec}}

And you can of course change `record`{{}} to any of the other commands `dump`{{}} and `top`{{}} here.
Some of the important options you can use are:

`--rate` 
This determines how often you are sampling, if you increase this number precision increases but overhead also increases. This is set by default to `100`{{}} times per second.

`--duration`
Which determines how long the sampling will run. This is by default `unlimited`{{}}.

`--subprocesses`
This allows py-spy to not only profile the main Python process but also any subprocesses it spawns, which can be useful if your program has multiple processes.

`--nonblocking`
This is perhaps the most important one that we did not use, because this ensures that during the profiling the Python process is not paused. Py-Spy very briefly pauses the execution to read memory normally, and this prevents this behaviour.

One reason to not use this is that this may cause reading errors during sampling, therefore we recommend not using this as the performance overhead is usually extremely low. 