## Top subcommand
So what we will be starting with is the `top`{{}} subcommand which provides a top-like view of the CPU usage of function calls, and it can be used like this.
```
py-spy top --pid <PID>
# OR
py-spy top -- python executable.py
```

In the first case you need to know the pid of the python process to do that we are going to be using `ps`{{exec}} to find it, the problem is that we just run that command on a different tab we will not be able to find the python process so we will instead run `ps -e`{{exec}} and since no python process is currently running we can't find it right now either.


## Using Top

So were going to start by using `exampleprogram.py`{{}} which should be located in `somewhere/someplace`{{}} and we will start by using the following command.

`py-spy top -- python exampleprogram.py 35`{{exec}}

We can now see clearly what the program is doing in terms of function calls and can see which functions appear to be taking alot of time.

To see how this can be attached to an already running process we will first open a new tab where will start a new program.

`python exampleprogram.py 40`{{exec}}

Now we can go back to the original tab and run 

`ps -e`{{exec interrupt}} 

we should see the python process somewhere near the bottom and it should look like this.

`image template`

After finding the pid we will now run

`py-spy top --pid <PID>` 

and make sure to replace `<PID>`{{}} with the PID you found for example `3075`{{}}

Now that we are running we can once again see what type of functions are being called and what the CPU is spending the time on.