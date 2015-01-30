Week 7 Materials 
################

:date: 2015-01-26
:summary: Starting to learn more formal methods for figuring out coefficients in linear and quadratic models
:category: lessons
:tags: quadratic, linear, model, analytic


===========
Day 1 and 2
===========

 1. Figure out the equation that matches the following x,y points, using the process of constructing patterns of dots and guess-and-check that we used back in December.

 a. Pattern 1
 
.. image:: images/1-26-1.png
   :width: 100%
   :alt: A number dot pattern, find the equation
   :align: center
..


 b. Pattern 2

.. image:: images/1-26-2.png
   :width: 100%
   :alt: Number dot pattern #2,find the equation
   :align: center
..

 2. Remember that the goal of the dot representation is to use the visual pattern as a clue to the algebraic pattern.  If the number of rows in the dot representations is always the same as x, that suggests that the equation will be something like :math:`y  = (x)(  ?  )`.

If the number of rows is always the same as the **x**, and the number of columns is always 2 less than the  x, that suggests that the equation is :math:`y = (x) ( x - 2)`.

Even a wrong guess can help you, because it gives you something to check, and you can learn something from the checking process.  If your guess produces a sequence that is always 3 dots short, then you should add 3 to your guess.  If you guess produces a sequence that has too many dots,and the excess is always 2 times x, then you should :math:`2x` to your guess.

 3. Now let's try to do this process with algebraic techniques, by plugging the data values into the base equation, :math:`y = ax^2 + bx + c`

=====
Day 3
=====

 0. Figure out the equation that matches the following x,y points:

   ===  ===
    x    y
   ===  ===
    0    7 
    1    10
    2    13
   ===  ===

 1. Okay, so yesterday I think we moved a little too fast and I tried to introduce figuring out the coefficients in a quadratic too quickly, which led quite a few of you to rightly say "Where did that a and b come from?  That just doesn't make sense to me"  --- so I want to back up a little bit and remind you of a few things.

 2. What's the equation of a line look like?  :math:`y = mx + b`, right?  The **m** stands for the slope, the steepness, the "how much it goes up", or, as I heard someone say earlier, it's the "increaser".  The **b** is "where it starts", the "intercept", "how much you have to add to fix the pattern".  And we've done a lot to learn how to figure out what those numbers will be for a given pattern, but we haven't done it in a while.  Our real goal this week is to figure out how to do this same thing for quadratics, equations that have an :math:`x^2` in them

 3. So let's review how to figure out the coefficients for linear equations.  If you are doing this on your own, don't look at the equations until you've tried it yourself:

   ===  ===
    x    y
   ===  ===
    0    2 
    1    -2
    2    -6
   ===  ===

  (:math:`y=-4x+2`)


   ===  ===
    x    y
   ===  ===
    1    1
    2    6
    3    11
   ===  ===
 

  (:math:`y=5x-4` Notice that I didn't give you the value at :math:`x=0` on this one)


   ===  ===
    x    y
   ===  ===
    1    3 
    3    -1
    7    -9
   ===  ===

  (:math:`y=-2x+5`  Notice that the x-values are not evenly spaced on that one)


 4. Okay, so far you have mostly been doing this by figuring out the "increaser",or how much the y-value changes each time x changes.  This is finding the slope, or the **m** in :math:`y=mx+b`, and it involves a certain amount of guessing and checking.  I think guessing and checking is a great way to solve problems, because it works even when you don't understand the problem, as long as you have a way of checking the guess, it is a really powerful tool.  But we also want to have tools that help make it easier, once we understand enough to make use of them, and the work we've been doing for weeks on systems of equations could be really useful here.  In systems problems, you have two equations with two variables that you don't know, and you combine the two equations in some way so you can find out which values work for both of them.

Well the data I'm giving you for the x and y values gives you information that you might be able to use to set up equations to figure out what the **m** and the **b** are in the equation of a line.

For example, on the previous question, substitute into the equation of a line the x and y values 1 and 3:

:math:`y = mx + b`

:math:`3 = m(1) + b`   and   :math:`-1 = m(3) + b`

which is a problem you know how to solve now.  Use it to figure out the **m** and the **b** again (and we already know that the answer is -2 and 5)


 5. Now try a couple more, using this technique of constructing equations that you can combine to figure out what the m and b are *without having to guess*.

 a.

   ===  ===
    x    y
   ===  ===
    0    7 
    2   -47
   ===  ===

 b.

   ===  ===
    x    y
   ===  ===
    1   -10 
    4   -28
   ===  ===




 6. Nice work -- we will return on Friday and Monday to do more with this idea to figure out equations of quadratics.  For now, I would like to work on building some vocabulary to describe the graphs of quadratic equations, so we are going to play a game of 20 questions, using a tool on Desmos.  The idea is that you will ask questions of someone else in the class, who will answer yes or no to describe the graph they have picked, and you will try to determine which one it was.  Go to student.desmos.com and enter the class code  **2uep** for F block, or **dju7** for G block.



=====
Day 4
=====
  
 1. Discussion of parabola vocabulary

 2. Practice finding the coefficients of linear and quadratic equations 


 
