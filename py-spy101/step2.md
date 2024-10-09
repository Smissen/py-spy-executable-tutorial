## Top subcommand
So what we will be starting with is the `top`{{}} subcommand which provides a top-like view of the CPU usage of function calls, and it can be used like this.
```
py-spy top --pid <PID>
# OR
py-spy top -- python executable.py
```

In the first case you need to know the pid of the python process to do that we are going to be using `ps`{{exec}} to find it, the problem is that we just run that command on a different tab we will not be able to find the python process so we will instead run `ps -e`{{exec}} and since no python process is currently running we can't find it right now either.


## Using Top

So were going to start by using `exampleprogram.py`{{}} which should be located in our working directory and we will start by using the following command.

`py-spy top -- python exampleprogram.py 35`{{exec}}

We can now see clearly what the program is doing in terms of function calls and can see which functions appear to be taking alot of time.

To see how this can be attached to an already running process we will first open a new tab (ie a new terminal window) where will start a new program.

`python exampleprogram.py 40`{{exec}}

Now we can go back to the original tab and run 

`ps -e`{{exec interrupt}} 

we should see the python process somewhere near the bottom and it should look like this.

<img src="./pythonpid.png" width="350px">

After finding the pid we will now run

`py-spy top --pid <PID>` 

and make sure to replace `<PID>`{{}} with the PID you found for example `2603`{{}} so the command should look like this `py-spy top --pid 2603`{{}} except with probably a different PID number.

If the command fails that probably means the python process has finished since it only runs for about 60 seconds in that case you need to go back to the second tab(terminal window) and run the program again.

Now that we are running we can once again see what type of functions are being called and what the CPU is spending the time on.