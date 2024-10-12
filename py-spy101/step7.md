## Not Again...
Oh dear, you see that you've done it again... You accidentally included bogosort in your quicksort... Nothing to be ashamed of, it happens to the best of us from time to time.

You quickly comment out the bogosort call and elif statement on lines 18 & 19 and now you're good to go, into production it goes!

## Happily ever after... You hoped
Run `python sort.py 500000`{{exec}} in a seperate tab, then `ps -e`{{exec interrupt}} and `py-spy top --pid <PID>` in your main tab to get it into production.

Your code has now been in production for a while, when you get pinged by your company's ChatOps bot: "py-spy indidicates odd resource usage".

You rush to the py-spy tab and you're horrified by what you see, Snorlax has fallen asleep inside your program.

You quickly shut down the program and head right back into `sort.py`{{}} to wake him up.

It's been a rough road, but with the power of py-spy you avoided one bug and mitigated the damage done by another one.
