## Another day in the office
Now that we've gone through the basics, you'll get a little exercise that will use py-spy both in development and operations.

Picture yourself this, you've spent a long day in the office working and you're finally done with your project; a standard impelementation of Quicksort. You'll quickly get it into production, just after you've done some quick testing with your favorite tool, py-spy.

You run `py-spy top -- python sort.py 200`{{exec}}, but you notice something odd; why is Quicksort so relatively quick?
py-spy must have caught something you didn't. 

Click `Editor`{{}}, to the left of `Tab 1`{{}} and investigate `sort.py`{{}} using the information recieved from py-spy.