# Advent_of_Code_2023

**Date** -  - Day 1 Part 2 Complete - Total Time: 10 hours  
> *Reflections* - This was a real pain.
> > *Difficulties*
> > >

**12/16/2023** -  - Day 9 - Total time 1.5 hours  
> *Reflections* - This came along pretty great! Part 2 felt easy as well
> > *Difficulties*
> > > Took some time to try and consolidate. Tried to avoid either redundant or unnecessary variables.
> > > Took a little while to find my "while" ender. Originally thought I would count "0s" but realized that was unnecessary

**12/15/2023** -  - Day 8 - Total Time: 5 hours  
> *Reflections* - Once again I wasted hours because I hurried through the prompt.
> > *Difficulties*
> > > READ THE DAMN PROMPT CORRECTLY
> > > Practiced setting up and calling functions
> > > Feel like code is readable and concise-ish
> > > Need to study how to properly format lines in a efficient way
> > > All in all difficulty 3/10

**12/14/2023** -  - Day 7 - Total Time: 4.5 hours  
> *Reflections* - The concept came early and I stuck to the plan. Wasn't the most optimized plan, but it worked!
> > *Difficulties*
> > Learned some skills with creating and calling functions
> > Learned some tricks with sort and lambda and keys
> > Pt 2 definitely could have been optimized more; I was kind of on a roll spelling each step out and just continued with that process.
> > Had a few hiccups as I overlooked a couple conditions.
> > Getting a little faster at debugging.

**12/13/2023** -  - Day 6
> *Reflections* - Took a break from Day 5 and it went smooth
> > *Successes*
> > >Either this day was incredibly easy or I am actually learning something! (a little of both)
> > >I think background on math and physics beneficial

**12/12/2023** -  - Day 5
> *Reflections* - This is going to be a Day 3 all over
> > *Difficulties*
> > >I will come back to this after studying maps more.
> > >I was able to get it working with a very unoptimized, logically simple code for the test input. However, the code required creating/comparing lists with 10s of millions of data points, and my compute could not take it.
> > >Reviewed a couple cheat sheets which make me want to go a different, simpler route.


**12/11/2023** -  - Day 4
> *Reflections* - Took a break from Day 3 and dont regret it
> > *Successes*
> > >Pretty straight forward
> > >Was able to get part 1 and part 2 without any aid!
> > >Part 1 can definitely be cleaned up. I think part 2 is tidy but things can always be made simpler

**12/7/2023 - 12/Forever/23** -  - Day 3 Part 1 
> *Reflections* - NEED TO RETURN TO
> > *Difficulties*
> > >Thought I created a good system for getting previous, current, and next lines. Think that was a keeper
> > >Need a better solution for contextualized the number(I had been looking digit by but that runs into the issue of knowing when a digit is apart of a larger digit and storing the value of the larger digit)
> > > > (perhaps first I should identify all digits that belong to one number, then store the indexes of the digits in a list, then for the symbol search, look based off symbol index range of [min(digit list)-1:max(digit list)+1]
> > > > > Within that loop, the digits can be stored in a terminating list... then if that digit has symbol, that terminating list can append the wanted value list


**12/6/2023** -  - Day 2 Part 2 Complete - Total Time: 2 hours  
> *Reflections* - May be the cleanest planning and execution yet!
> > *Successes*
> > >Instead of constantly calling back three different arrays, I used a dict. to only call back a specific array as needed!
> > >Successfully used split() which made life  so much easier.
> > >Continued practicing append() and learned clear() and min/max().
> > >GOT IT ON FIRST TRY!
> > >**I continue to misread the prompt though, need to be slower with instructions**

**12/5/2023** -  - Day 2 Part 1 Complete - Total Time: 6 hours  
> *Reflections* - I think I did well on the plan, ran into a few hiccups with the structure
> > *Difficulties*
> > >Have since learn split(), would have helped in getting numbers and ID
> > >Ran into big problems with "break"; was messing with identifying 3 digit values
> > >Learned some range(len()) situations

**12/5/2023** -  - Day 1 Part 2 Complete - Total Time: 10 hours - pt2.py 
> *Reflections* - This was a real pain.
> > *Difficulties*
> > > Refamiliarized with dictionaries, range, len(), and creating functions
> > >Did not take the most efficient route of reading chunks out of each line of array
> > > 
> > > Creating a stop to nested For loop
> > > 
> > > Had to create a function "num_there" to fix false positive flaw in structure
> > > 
> > > Aware that I did not need as many lists/variables as I used
> > > 
> > > Inefficient structure; But glad I was able to stick with original plan and find a way

**12/3/2023** -  - Day 1 Part 1 Complete - Total Time: 4 hours - main.py  
> *Reflections* - Have some basic knowledge; Used A LOT of resources
> > *Difficulties*
> > > Had difficulty getting the the "sum" counter correct.
> > > 
> > > .read().splitlines() v.s. .readlines()
> > > 
> > > reversed() vs "[::-1]"
> > > 
> > > learned isdigit()  function

First attempts at using Python to solve challenges presented in the Advent of Code 2023 Calendar.
