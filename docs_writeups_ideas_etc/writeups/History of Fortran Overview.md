# Fortran  
 
Long before Python and Java, one had to code in machine code or assembly.  This was a process that seems incredibly tedious to those of us today who expect data for variables to be allocated automatically.  There did eventually come to exist some interpreted/compiled languages, like Speedcode, that would make coding easier; however, this came with huge drawbacks in speed and efficiency of the resulting program.  The IBM 704, released in 1954, was much better at floating point operations.  The result of this was that inefficiencies in many compilers, which were previously irrelevant due to the limiting factor of floating-point operations, were laid bare.  Many programmers came to believe that it would be impossible to create an efficient "automatic programming" system.  

In late 1953, John Backus made a proposal to his boss at IBM to create an "automatic programming" system.  His rationale was that it took about as much money to pay the programmers for a computer as the computer cost itself.  He also foresaw that debugging machine code was going to become an increasing issue as computers became cheaper and more plentiful.  

Backus's proposal was approved by his boss and he and his team began development of Fortran, short for Formula Translation.  And after "25 man years of effort," the Fortran language and compiler was released in 1957.  

Although Backus was seeking to make programming easier, he considered the problem of language design as secondary to the efficiency of the compiler (he also thought that syntax errors would be a nonissue with the new language, and thus Fortran I's compiler was not good at checking them).  Backus also did not foresee that Fortran would persist beyond the IBM 704, and thus Fortran was not initially portable.  He did realize that in order to convince programmers to adopt his language, he had to make the resulting compiled programs as efficient as those made by a competent human programmer working in machine code.  The predominant mindset at the time was that compile time was not as important as program speed, as the program would be run more times than it was compiled.  Fortran I even had a `FREQUENCY` statement to be used with conditionals, which the compiler would use to perform a Monte Carlo simulation to determine how to optimally assign index registers.  The result of this was an extremely effective, if slow, compiler, which basically established modern compiler technology.  "In some cases it produced code which was so good that users thought it was wrong since it bore no obvious relationship to the source. It set a standard for object program efficiency which has rarely been equaled" (Allen).   And, despite its language flaws, Fortran was still much easier to work with than machine code-- it cut the number of lines of code necessary for a program by a factor of 20.  

Fortran II, released in spring of 1958, added support for subroutines.   This helped alleviate the issue of long compile times by allowing problems to be broken up.  Despite a buggy initial distribution, the use of Fortran began to spread rapidly.  

"A report on FORTRAN usage in November 1958 [Backus 1958] says that 'a survey in April [1958] of twenty-six 704 installations indicates that over half of them use FORTRAN [I] for more than half of their problems. Many use it for 80~ or more of their work... and almost all use it for some of their work.'" (Backus)

Fortran had a significant impact on future computer languages, most notably BASIC, and was responsible for many innovations in compiler technology.  Although Fortran has now seen the peak of its popularity come and go, Fortran is still being developed (with Fortran 2018 in development right now) and still remains in use today among scientists, due to the large body of legacy code written in Fortran.  Proponents claim that modern Fortran is simpler than object-oriented languages-- and to this day, Fortran remains one of the fastest languages, 100 times faster than Python.  

Sources: 

TODO: format these 

http://moreisdifferent.com/2015/07/16/why-physicsts-still-use-fortran/

https://dl.acm.org/citation.cfm?id=602379

https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5390587

http://delivery.acm.org/10.1145/810000/808380/p165-backus.pdf?ip=18.30.118.141&id=808380&acc=ACTIVE%20SERVICE&key=7777116298C9657D%2EDE5F786C30E1A3B4%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1543252646_a3d54721bcd9ba00b40632543a52fc22
https://en.wikipedia.org/wiki/Fortran