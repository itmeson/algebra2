Week 7 Materials 
################

:date: 2014-10-13
:summary: How do you solve pursuit problems analytically? A non-linear example that requires some ingenuity and factoring 
:category: lessons
:tags: interest, pursuit, systems, linear, factoring, simplification



=====
Day 1
=====

 1. Check-in on quiz, notebooks, etc. (grading notebooks soon)

 2. Write out a process for dealing with a system. What is the process you follow in figuring out where two lines meet? 

 3. Discussion: How many different ways can you handle accounting for a headstart in one of these pursuit problems?

 4. How do you solve analytically -- using just the equations and not a graph? 


=====
Day 2
=====

 1. return quizzes, discuss problem and retakes

 2. Fry's bank account.  Fry is a character from the tv cartoon Futurama.  He was somehow transported from the year 1999 to the year 2999, and hilarity ensues.  One day he goes to check out his bank account at the local bank.  He started with 97 cents, with "two and a quarter percent" interest rate for 1000 years. How much money will be in his account after just one year of receiving interest.  How about two?

 3. Graph the resulting values.  Discussion: what makes it non-linear? What kind of bank account would be linear? Can we compare different bank account rules?

 4. Practice with combining like terms and solving simple equations

=====
Day 3
=====

 1. More on Fry's bank account.  Really, why isn't it linear?  What would it mean if it were linear?  Imagine a bank account where you deposit \\$1000 on the first day, and then every year thereafter you earn 5% interest *of the money you originally put in*.  That would be \\$50 every year.  So the account would grow by the same amount year after year, fifty dollars each time.  *That* would be linear.  The equation would be.... $y = 50x + 1000$.  The x would represent years, the y the amount of money in the account, the 50 how much it grows each year, and the 1000 the starting point.

Why should you not be satisfied with that?  Because you would get the same amount of money, exactly, by taking the extra \\$50 out of that bank each year and putting it under your mattress.  The bank gives you interest based on what you started with, so there's no reason not to take that extra out of the bank and put it somewhere else.  Even better, would be to put it *in another bank*.  Then that other bank *would* pay you interest on that \\$50 too.  So you'd actually get more money that way.

But you'd get more money, and the first bank would have less to play with because you would be taking fifty dollars out of that account every year.  Banks are not fans of situations where you make more money, and they don't.  If they can get you to leave every penny in the first account, then they get to count all of that deposit as an asset they can use to make loans to other people (that's how banks make money).  So they always pay you interest based on what is currently in the account -- otherwise you would siphon the extra bits out into a different account at a different bank.

So the real way it grows is to increase by the same factor every year:

======= =================================
1000    $y_2 = .05*1000 + 1000 = 1050$
1050    $y_3 = .05*1050 + 1050 = 1102.50$
1102.50 $y_4 = \\ldots$
======= =================================

What's the pattern? Always multiply by the interest rate, add to the preceding amount: $y_n = .05 \\cdot y_{n-1} + y_{n-1}$.  Whenever you see the same operation repeated over and over, you should look for a shorter way to *write* the rule that describes what to do.  Partly to save time and ink (a surprising amount of what we're taught in school mathematics was invented originally for the sole reason that it took less ink to write it that way), and partly because expressing it more simply can illuminate structure, can make the reasoning more clear so we can see something deeper going on.  In this case, because the preceding amount is written in the equation twice, you should immediately consider *factoring* it, like this:

$.05 * 1000 + 1000 = 1000(.05 + 1) $

do you see how the two sides of that equation are really the same?  Just different ways of writing the same thing, but the one on the right uses less ink?  Well there's an even shorter way of writing it: 

$1000(.05 + 1) = 1000(1.05)$

Huh.  So figuring out the interest for a year, which had involved multiplying then adding, is really the same thing as just multiplying by the interest plus 1.  And then we can see another way of shortcutting it, because each step is taking the previous amount and multiplying it by 1.05.  Again, whenever you see the same thing written more than once, try to find a way to write it more simply:

======= ===============================================
1000    $y_2 = 1.05*1000$
1050    $y_3 = 1.05*(1.05*1000) = 1.05^2 * 1000$
1102.50 $y_4 = 1.05*(1.05*(1.05*1000)) = 1.05^3 * 1000$
======= ===============================================

Aha! So doing the year after year calculation is the same as using an *exponent* to represent the repeated multiplication of the interest.

Now use Desmos to make new tables and graphs showing Fry's bank account year after year, using the exponent to represent the amount in the account, to find out how much money he had.

 2. Practice factoring simple expressions (linear binomials)


=====
Day 4
=====

No School!!  Mid-term grades will be coming out on Monday.



   
