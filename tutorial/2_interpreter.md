【注】翻译官方文档，只是想在学习Python过程留下笔记，如涉及侵权，请联系删除。
[The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
[linyk3简书:The Python Tutorial:Python教程笔记](https://www.jianshu.com/p/1ae6bef84d5b)
[linyk2655 Github LearnPython ](https://github.com/lyk2655/LearnPython/blob/master/tutorial/interpreter.md)
原文：[Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)

2. Using the Python Interpreter  使用Python 解释器

2.1. Invoking the Interpreter  调用解释器

The Python interpreter is usually installed as /usr/local/bin/python3.7 on those machines where it is available; putting /usr/local/bin in your Unix shell’s search path makes it possible to start it by typing the command:
在能够使用Python的机器中，Python解释器经常安装在 /usr/local/bin/python3.7. 把 /usr/local/bin 这个目录加在Unix shell 的搜索路径，就能在Shell.输入下面的命令来启动它：
```
Python3.7
```
to the shell. [[1]](https://docs.python.org/3/tutorial/interpreter.html#id2) Since the choice of the directory where the interpreter lives is an installation option, other places are possible; check with your local Python guru or system administrator. (E.g., `/usr/local/python` is a popular alternative location.)
Python解释器的路径的选择是安装时的选项，其他路径也是可以的。可以让你的Python大师或系统管理员来检查。(例如，`/usr/local/python` 这个路径是另外一个比较流行的选择)

On Windows machines, the Python installation is usually placed in C:\Python36, though you can change this when you’re running the installer. To add this directory to your path, you can type the following command into the command prompt in a DOS box:
在Windows的机器中，Python经常安装在`C:\Python36`，即使你可以在执行安装程序的时候修改路径。如果要把这个目录加到环境变量中的Path中，你可以在Dos命令行提示器中输入下面的命令:
 ```
set path=%path%;C:\python36
```
Typing an end-of-file character (`Control-D` on Unix,`Control-Z` on Windows) at the primary prompt causes the interpreter to exit with a zero exit status. If that doesn’t work, you can exit the interpreter by typing the following command: `quit()`.
在命令行提示器中输入结束符（Unix是`Control-D`, Windows是`Control-Z`）可以让解释器以状态‘0’退出。如果这个不起作用，你可以输入下面的命令来退出解释器：`quit()`.

The interpreter’s line-editing features include interactive editing, history substitution and code completion on systems that support readline. Perhaps the quickest check to see whether command line editing is supported is typing `Control-P` to the first Python prompt you get. If it beeps, you have command line editing; see Appendix [Interactive Input Editing and History Substitution](https://docs.python.org/3/tutorial/interactive.html#tut-interacting) for an introduction to the keys. If nothing appears to happen, or if `^P` is echoed, command line editing isn’t available; you’ll only be able to use backspace to remove characters from the current line.
在支持按行读取的系统中，解释器的行编辑的特征包括：交互式编辑、历史替换以及代码补全。获取最快地检查是否支持命令行编辑的方法就是在你的Python提示器中输入`Control-P`. 如果它发出蜂鸣声，说明支出命令行编辑。相关的介绍可以参考附录[Interactive Input Editing and History Substitution:交互式编辑和历史替换](https://docs.python.org/3/tutorial/interactive.html#tut-interacting)。如果没有任何事情发生，或者提示的是`^P`,说明命令行编辑是不支持的。这样你只能使用退格键来删除当前行的字符。

The interpreter operates somewhat like the Unix shell: when called with standard input connected to a tty device, it reads and executes commands interactively; when called with a file name argument or with a file as standard input, it reads and executes a *script*from that file.
解释器的操作类似Unix Shell: 当调用关联于某个tty设备的标准输入时，它交互式的读取并执行命令。当调用一个文件名为参数或者文件作为标准输入时，它读取并执行这个文件中的脚本。

A second way of starting the interpreter is `python -c command [arg] ...`, which executes the statement(s) in *command*, analogous to the shell’s [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c) option. Since Python statements often contain spaces or other characters that are special to the shell, it is usually advised to quote *command* in its entirety with single quotes.
第二个启动解释器的方式是：`python -c command [arg] ...`， 这样可以执行*command* 这个语句，类似shell 的   `-c` 选项。因为Python语句经常包含有空格符或其他Shell中的特殊字符，所以建议将 *command* 整体用引号包起来。

Some Python modules are also useful as scripts. These can be invoked using `python-m module [arg] ...`, which executes the source file for *module* as if you had spelled out its full name on the command line.
一些Python模块也跟脚本一样很有用。这些可以用`python-m module [arg] ...`命令来调用，就可以像在命令中把模块的全名拼出来一样来执行*module* 这些模块文件。

When a script file is used, it is sometimes useful to be able to run the script and enter interactive mode afterwards. This can be done by passing [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i) before the script.
当一个脚本文件被使用，如果可以运行脚本并且在后面输入交互命令就更好了。这个可以通过在脚本前面加上`-i`来实现。

All command line options are described in [Command line and environment](https://docs.python.org/3/using/cmdline.html#using-on-general).
所有的命令的选项都在 [Command line and environment:命令行与运行环境](https://docs.python.org/3/using/cmdline.html#using-on-general)中有详细介绍。

### 2.1.1\. Argument Passing 参数传递

When known to the interpreter, the script name and additional arguments thereafter are turned into a list of strings and assigned to the `argv` variable in the `sys` module. You can access this list by executing `import sys`. The length of the list is at least one; when no script and no arguments are given, `sys.argv[0]` is an empty string. When the script name is given as `'-'` (meaning standard input), `sys.argv[0]` is set to `'-'`. When [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c) *command* is used, `sys.argv[0]` is set to `'-c'`. When [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) *module* is used, `sys.argv[0]` is set to the full name of the located module. Options found after [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c)*command* or [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) *module* are not consumed by the Python interpreter’s option processing but left in `sys.argv` for the command or module to handle.
我们知道解释器中，脚本的名字及其后面附加的参数会被转换为一个字符串列表并且赋值给`sys`模块中的变量`argv`。 你可以通过执行`import sys`来访问这个列表。这个列表的长度至少是1；当没有提供脚本或参数时，`sys.argv[0]` 是一个空字符串。当脚本的名字是`'-'`(表示标准输入)， `sys.argv[0]` 设置为 `'-'`. 当使用 [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c) *command* 时, `sys.argv[0]` 设置为 `'-c'`. 当使用 [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) *module* 时, `sys.argv[0]` 被赋值为本地模块的全称. 在 [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c)*command* 或者 [`-m`](https://docs.python.org/3/using/cmdline.html#cmdoption-m) *module* 后面的选项不会被Python解释器处理，而是留在 `sys.argv` 给 command or module 去处理。

### 2.1.2\. Interactive Mode 交互模式

When commands are read from a tty, the interpreter is said to be in *interactive mode*. In this mode it prompts for the next command with the *primary prompt*, usually three greater-than signs (`>>>`); for continuation lines it prompts with the *secondary prompt*, by default three dots (`...`). The interpreter prints a welcome message stating its version number and a copyright notice before printing the first prompt:
当命令是从tty中读取的，这时解释器就是在所谓的*交互模式*。在这个模式中它为下一个命令提供了*主要提示*，经常是三个大于号（`>>>`）来表示。为延续行提供了*次级提示*，缺省是三个点(`...`). 解释器在开始它的第一个提示符之前，会打印欢迎信息，以其版本号和版权开始：
```
$ python3.7
Python 3.7 (default, Sep 16 2015, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Continuation lines are needed when entering a multi-line construct. As an example, take a look at this [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) statement:
延续行是在输入一个多行的结构时需要的。例如，可以看看`if`语句：

```
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
```

For more on interactive mode, see [Interactive Mode](https://docs.python.org/3/tutorial/appendix.html#tut-interac).
更多关于交互模式，可以参考 [Interactive Mode:交互模式](https://docs.python.org/3/tutorial/appendix.html#tut-interac).


## 2.2\. The Interpreter and Its Environment  解释器及其运行环境

### 2.2.1\. Source Code Encoding  源码编辑 [](https://docs.python.org/3/tutorial/interpreter.html#source-code-encoding "Permalink to this headline")

By default, Python source files are treated as encoded in UTF-8. In that encoding, characters of most languages in the world can be used simultaneously in string literals, identifiers and comments — although the standard library only uses ASCII characters for identifiers, a convention that any portable code should follow. To display all these characters properly, your editor must recognize that the file is UTF-8, and it must use a font that supports all the characters in the file.
默认地，Python源文件都是UTF8编码的。用这个编码格式，世界上大部分的字符都可以同时来表示 字符串文字、标识符和注释 -- 虽然标准库中的标识符只使用了ACSII字符，遵从了可移植性代码的便利性。为了能够正确展示这些字符，你的编辑器必须能够辨识出这个文件是UTF-8，并且使用一种支持文件中所有字符的字体。

To declare an encoding other than the default one, a special comment line should be added as the *first* line of the file. The syntax is as follows:
为了声明一种非默认的编码格式，需要在文件的*第一行*中加上一个特殊的注释，相关的语法就是：
```
# -*- coding: encoding -*-
```

where *encoding* is one of the valid [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.") supported by Python.
 *encoding* 是Python支持的的一个合法的[`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.") 。

For example, to declare that Windows-1252 encoding is to be used, the first line of your source code file should be:
例如，为了声明使用的是 `Windows-1252 `编码格式，你的源文件中的第一行应该是：
```
# -*- coding: cp1252 -*-
```

One exception to the *first line* rule is when the source code starts with a [UNIX “shebang” line](https://docs.python.org/3/tutorial/appendix.html#tut-scripts). In this case, the encoding declaration should be added as the second line of the file. For example:
第一行规则的一个例外就是源文件以[UNIX “shebang” line](https://docs.python.org/3/tutorial/appendix.html#tut-scripts) 开头。在这种情况中，编码格式的声明应该加在文件中的第二行。例如：
```
#!/usr/bin/env python3
# -*- coding: cp1252 -*-
```
Footnotes 注脚
[[1]](https://docs.python.org/3/tutorial/interpreter.html#id1) | On Unix, the Python 3.x interpreter is by default not installed with the executable named `python`, so that it does not conflict with a simultaneously installed Python 2.x executable. |




