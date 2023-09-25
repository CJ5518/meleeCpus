# meleeCpus
Finding out which melee cpu is truly the best.

I used the [Falcon supercomputer](https://www.c3plus3.org/falcon/) to run a few thousand CPU vs CPU games in melee.

Once analysis has been completed, you should be able to see the computed matchup chart here:


# Usage
If, for whatever reason, you would like to do something like this yourself, here are the steps to do things as I did them:

1. Clone the repo onto your supercomputer of choice.
2. Use the command `apptainer build --sandbox melee.sif melee.def` (Note the --sanbox, I never could get the container to work properly without it being writable)
3. Use apptainer exec --writable python3 /meleeScript.py [options] (Note the --writable, again, I never could get it to work without this, I suspect it has something to do with xvfb)

And that's about it, you'll need to put a melee iso somewhere but the above command should run some number of cpu battles for you.

Use `runner.lua` to submit a bunch of jobs (I included a small delay between submissions just in case too many concurrent jobs broke my code) and in a few hours (only takes so long because of the delay) you'll have your own melee CPU battle dataset.

# Parser usage
To speed up parsing, that is also accelerated by the super computer. On the machine I was using, I had to do some weird container stuff such that the command I use to parse a folder of replays is as follows:

`apptainer exec --writable -f ../pythonContainer/ python3 /root/meleeCpus/parseFolder.py -i /root/meleeCpus/Slippi
Files/Job_5143`

Where ../pythonContainer/ is a container with a newer version of python installed than what was on the machine.

The parseRunner.py file can be used to run all the parser jobs.
