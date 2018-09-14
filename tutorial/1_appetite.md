【注】翻译官方文档，只是想在学习Python过程留下笔记，如涉及侵权，请联系删除。
[The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
[linyk3简书:The Python Tutorial:Python教程笔记](https://www.jianshu.com/p/1ae6bef84d5b)
原文：[Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)

# 1\. Whetting Your Appetite 欢迎您的使用

If you do much work on computers, eventually you find that there’s some task you’d like to automate. For example, you may wish to perform a search-and-replace over a large number of text files, or rename and rearrange a bunch of photo files in a complicated way. Perhaps you’d like to write a small custom database, or a specialized GUI application, or a simple game.
如果你有很多工作在计算机上面，最终你会发现有许多任务你想要自动来完成。例如，你希望能够在很大的文件里实现查找和替换，或者用复杂的方式来重命名以及重新编排一系列照片。也许你会写一个小型的自定义数据库，或者一个特定的GUI交互应用，或者一个简单的游戏。

If you’re a professional software developer, you may have to work with several C/C++/Java libraries but find the usual write/compile/test/re-compile cycle is too slow. Perhaps you’re writing a test suite for such a library and find writing the testing code a tedious task. Or maybe you’ve written a program that could use an extension language, and you don’t want to design and implement a whole new language for your application.
如果你是一个专业的软件开发者，你可能已经使用了多种C/C++/Java的标准库，却发现通常编辑、 编译、测试和重编译是很慢的。也许你正在为某个标准库编写一个测试案例并且发现编写测试代码是一件很乏味的任务。或者你已经写了一个可以扩展语的程序，并且你不想为了你的应用来设计和完成一整个新的语言。

Python is just the language for you.
那么，Python就是你所需要的语言。

You could write a Unix shell script or Windows batch files for some of these tasks, but shell scripts are best at moving around files and changing text data, not well-suited for GUI applications or games. You could write a C/C++/Java program, but it can take a lot of development time to get even a first-draft program. Python is simpler to use, available on Windows, Mac OS X, and Unix operating systems, and will help you get the job done more quickly.
你可以写一个Unix的Shell脚本或者Windows的批处理文件来处理这些任务，但是Shell脚本是最适合来移动文件以及改变文本数据，却不适合于编写GUI应用或游戏。你可以写一个C/C++/Java 程序，但是即使是初稿的程序，它也会花费你很多时间来开发。Python 使用起来很简单，能同时在Windows，Mac 和 Unix 操作系统
运行，将会帮助你更快的完成任务。

Python is simple to use, but it is a real programming language, offering much more structure and support for large programs than shell scripts or batch files can offer. On the other hand, Python also offers much more error checking than C, and, being a *very-high-level language*, it has high-level data types built in, such as flexible arrays and dictionaries. Because of its more general data types Python is applicable to a much larger problem domain than Awk or even Perl, yet many things are at least as easy in Python as in those languages.
Python使用起来很简单，但是它也是一门实实在在的编程语言，为大型程序提供比Shell 脚本和批处理文件还多的结构和支持。另一方面，Python比C语言提供了更多的错误检查，并且作为一门**非常高级的语言**，Python也拥有很多内置的高级数据类型，例如可扩展的数组和字典。由于它更加常用的数据类型，Python比AWK甚至是Perl，更适用于较多问题领域中。因此相对于这些语言，很多事情在Python这边就是极简的。

Python allows you to split your program into modules that can be reused in other Python programs. It comes with a large collection of standard modules that you can use as the basis of your programs — or as examples to start learning to program in Python. Some of these modules provide things like file I/O, system calls, sockets, and even interfaces to graphical user interface toolkits like Tk.
Python 允许你把你的程序分成模块，从而你可以在其他Python程序中可以复用它。你可以在你的程序中使用它附带的一大系列的标准模块。其中一些模块可以提供类似文件I/O，系统调用，套接字，甚至类似Tk的GUI的接口工具包等等功能。

Python is an interpreted language, which can save you considerable time during program development because no compilation and linking is necessary. The interpreter can be used interactively, which makes it easy to experiment with features of the language, to write throw-away programs, or to test functions during bottom-up program development. It is also a handy desk calculator.
Python 是一门解释型语言，能够节省你程序开发阶段大量的时间，因为汇编和链接不是必须的。解释器可以用来交互，使得简单的来实现语言的特征，编写一次性的程序，或者在自上而下编程开发的测试函数的编写。它也是一个便利的桌面计算器。

Python enables programs to be written compactly and readably. Programs written in Python are typically much shorter than equivalent C, C++, or Java programs, for several reasons:
*   the high-level data types allow you to express complex operations in a single statement;
*   statement grouping is done by indentation instead of beginning and ending brackets;
*   no variable or argument declarations are necessary.

Python让程序变得能够更加简洁和可读性。Python程序通常比相同体量的C、C++、Java程序更加简洁的原因是:
 *  高级数据类型允许你在单一的语句中表示复杂的操作；
 *  语句组合是靠缩进实现的，而不是前后两个大括号；
 *  变量或参数声明是非必须的。

Python is *extensible*: if you know how to program in C it is easy to add a new built-in function or module to the interpreter, either to perform critical operations at maximum speed, or to link Python programs to libraries that may only be available in binary form (such as a vendor-specific graphics library). Once you are really hooked, you can link the Python interpreter into an application written in C and use it as an extension or command language for that application.
Python 是*可扩展的*：如果你知道怎样用C语言编程，那就很简单的为解释器增加一个新的内置函数或模块。要么是用最快的速度来执行关键步骤，要么将Python程序链接至库函数，这样或许只能以二进制的形式来获取（例如特定供应商的图形库函数）。只要你是真的想，你可以将一个用C写的程序和Python链接起来，并且把它作为应用中的一个扩展或命令行语言。

By the way, the language is named after the BBC show “Monty Python’s Flying Circus” and has nothing to do with reptiles. Making references to Monty Python skits in documentation is not only allowed, it is encouraged!
顺便说一下，这个编程语言是在BBC的节目"Monty Python's Flying Circus"之后命名的，并且和爬行动物没有关系。在文档中为Mongty Python 短剧提供参考是非必须的，而是鼓励的。

Now that you are all excited about Python, you’ll want to examine it in some more detail. Since the best way to learn a language is to use it, the tutorial invites you to play with the Python interpreter as you read.
现在对于Python你感觉到很兴奋，你将会想要在更细节的方面来审视它。因为学习一门语言最好的方式就是使用它，所有本教程邀请你在阅读的同时一起来使用Python解释器。

In the next chapter, the mechanics of using the interpreter are explained. This is rather mundane information, but essential for trying out the examples shown later.
下一章将会介绍使用解释器的机制。这是很普通的信息，但是对于实现后面展示的案例却是很必要的。

The rest of the tutorial introduces various features of the Python language and system through examples, beginning with simple expressions, statements and data types, through functions and modules, and finally touching upon advanced concepts like exceptions and user-defined classes.
剩下的教程将会通过例子来介绍Python语言和系统的许多特征。从简单的表达式、语句和数据类型开始，然后是函数和模块，最后触及类似异常和用户自定义类等高级概念。
