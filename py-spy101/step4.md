## Dump subcommand
The `dump`{{}} subcommand can be called like this
```
py-spy dump --pid <PID>
```

## Using dump
We will use `exampleprogram.py`{{}} and this time we will once again need the power of two terminal windows so starting by using the first tab we will call.

`python exampleprogram.py 40`{{exec}}

then we switch tabs (terminal windows) and in the new one we will like in step 2 need to find out the PID of the python process (Do you remember it?)

<details>
  <summary>Do you remember the command from step 2? (Click this spoiler if not)</summary>
  ```
  ps -e{{exec}}
  ``` 
</details>

Once we find the python process PID which should be near the bottom we can now run `dump`{{}} to find the Python call stacks. And remember to change `<PID>`{{}} to the correct number that you see in the terminal for example it should look like this `py-spy dump --pid 2470`{{}}

`py-spy dump --pid <PID>`

We should now see the call stacks and this can be very useful if you have more threads for example.