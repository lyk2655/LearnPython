 
# 3. An Informal Introduction to Python
       Python的一个非正式介绍

In the following examples, input and output are distinguished by the presence or absence of prompts ([>>>](https://docs.python.org/3/glossary.html#term) and […](https://docs.python.org/3/glossary.html#term-1)): to repeat the example, you must type everything after the prompt, when the prompt appears; lines that do not begin with a prompt are output from the interpreter. Note that a secondary prompt on a line by itself in an example means you must type a blank line; this is used to end a multi-line command.
在接下来的例子中，输入和输出通过存不存在提示符(`>>>`和`...`)来显式区分。如果要重复例子，你必须在提示符出现后，在提示符后面输入的所有东西。不是以提示符开头的行是解释器的输出。注意，例子中的行如果有次级提示符就意味着你必须输入一个空行。这个是用来结束一个多行的命令。

Many of the examples in this manual, even those entered at the interactive prompt, include comments. Comments in Python start with the hash character, `#`, and extend to the end of the physical line. A comment may appear at the start of a line or following whitespace or code, but not within a string literal. A hash character within a string literal is just a hash character. Since comments are to clarify code and are not interpreted by Python, they may be omitted when typing in examples.
这个手册中的许多例子，即使是进入交互提示器的都有注释。Python中的注释是以一个哈希字符`#`开始的，直至这一行的最后。一个注释可以出现在一行的开头，或者空白符中或者代码中，但是不能出现在一个字符常量中间。字符常量中的一个哈希字符就仅仅表示一个哈希字符。因为注释是为了阐述代码，Python并不会解释它，所有当你在手打例子时，注释是不必要的。

Some examples:
一些例子

```
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
```

## 3.1\. Using Python as a Calculator 使用Python作为计算器

Let’s try some simple Python commands. Start the interpreter and wait for the primary prompt, `>>>`. (It shouldn’t take long.)
让我们试一下简单的Python命令。启动解释器并等待提示符（`>>>`），这个不用等太久。

### 3.1.1\. Numbers 数字

The interpreter acts as a simple calculator: you can type an expression at it and it will write the value. Expression syntax is straightforward: the operators `+`, `-`, `*` and `/` work just like in most other languages (for example, Pascal or C); parentheses (`()`) can be used for grouping. For example:
解释器就像是一个简单的计算器：你可以输入一个表达式然后它就会输出值。表达式的语法也是直截了当的，`+`, `-`, `*` and `/` 这些操作符跟其他大部分语言（例如Pascal或者C语言）一样的用法。例如：

```
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
```

The integer numbers (e.g. `2`, `4`, `20`) have type [`int`](https://docs.python.org/3/library/functions.html#int "int"), the ones with a fractional part (e.g. `5.0`, `1.6`) have type [`float`](https://docs.python.org/3/library/functions.html#float "float"). We will see more about numeric types later in the tutorial.
整数 (e.g. `2`, `4`, `20`)的类型是`int`, 有小数部分(e.g. `5.0`, `1.6`) 的类型是`float`。我们将会在后面的教程中看到更多关于数字的类型。

Division (`/`) always returns a float. To do [floor division](https://docs.python.org/3/glossary.html#term-floor-division) and get an integer result (discarding any fractional result) you can use the `//` operator; to calculate the remainder you can use `%`:
除法（`/`）总是返回一个float类型。你可以使用操作符`//`来向下取整除(floor division)，这样将会得到一个整数类型的结果（丢弃结果中的小数部分）。计算余数可以使用`%`。

```
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
```

With Python, it is possible to use the `**` operator to calculate powers [[1]](https://docs.python.org/3/tutorial/introduction.html#id3):
Python中，可以使用`**`操作符来计算乘幂:

```
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
```

The equal sign (`=`) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:
等号(`=`)是用来给一个变量赋值。在下一个交互提示符之前，没有结果会显示。
```
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```

If a variable is not “defined” (assigned a value), trying to use it will give you an error:
如果一个变量没有定义(分配一个值)，尝试使用它将会报错：

```
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not definede 'n' is not defined
```

There is full support for floating point; operators with mixed type operands convert the integer operand to floating point:
这里对浮点数是全力支持的. 混合类型的操作数上的操作会把一个整数转化为浮点数。

```
>>> 4 * 3.75 - 1
14.0
```

In interactive mode, the last printed expression is assigned to the variable `_`. This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations, for example:
在交互模式中，最后打印的表达式被赋值给变量`_`. 这也意味着当你使用Python作为一个桌面计算器的时候，将会更加容易来持续计算，例如：

```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

This variable should be treated as read-only by the user. Don’t explicitly assign a value to it — you would create an independent local variable with the same name masking the built-in variable with its magic behavior.
用户应该把这个变量当做是只读的。不要明确的把一个值赋给它--你应该用同样的名字创建一个独立的局部变量来掩饰这个内置的变量的魔法行为。

In addition to [`int`](https://docs.python.org/3/library/functions.html#int "int") and [`float`](https://docs.python.org/3/library/functions.html#float "float"), Python supports other types of numbers, such as [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") and [`Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction"). Python also has built-in support for [complex numbers](https://docs.python.org/3/library/stdtypes.html#typesnumeric), and uses the `j` or `J` suffix to indicate the imaginary part (e.g. `3+5j`).
除了`int`和`float`类型，Python还支持其他的数字类型，例如十进制和分数。Python对复数也有内置的支持，并且使用`j`或`J`后缀类来指明虚数部分(e.g. `3+5j`)。


### 3.1.2\. Strings  字符串

Besides numbers, Python can also manipulate strings, which can be expressed in several ways. They can be enclosed in single quotes (`'...'`) or double quotes (`"..."`) with the same result [[2]](https://docs.python.org/3/tutorial/introduction.html#id4). `\` can be used to escape quotes:
除了数字，Python也可以操作字符串，可以用多种方式来表示。他们可以用单引号('...')或双引号("...")括起来。`\`可以用来zhuanyi4引号：

```
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
```

In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes. While this might sometimes look different from the input (the enclosing quotes could change), the two strings are equivalent. The string is enclosed in double quotes if the string contains a single quote and no double quotes, otherwise it is enclosed in single quotes. The [`print()`](https://docs.python.org/3/library/functions.html#print "print") function produces a more readable output, by omitting the enclosing quotes and by printing escaped and special characters:
在交互式解释器中，输出的字符串还用引号括起来并且特殊字符使用反斜线来转义。所有有时这个和输入看起来有点不一样（括起来的引号可能会改变），这两个字符串是等价的。如果一个字符串里面包含单引号且不包含双引号，这个字符串就用双引号括起来，否则就用单引号。

```
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.
```

If you don’t want characters prefaced by `\` to be interpreted as special characters, you can use *raw strings* by adding an `r` before the first quote:
如果你不想在字符前加上`\`来告诉解释器这是特殊字符，你可以使用*原生字符串*，在第一个引号前面加上一个`r`:

```
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

String literals can span multiple lines. One way is using triple-quotes: `"""..."""` or `'''...'''`. End of lines are automatically included in the string, but it’s possible to prevent this by adding a `\` at the end of the line. The following example:
字符串常量可以被分成多行。一种方法就是使用三个引号`"""..."""` 或者`'''...'''`.这些行的行尾会被自动包含进字符串，可以在行尾加上一个 `\` 来避免这种情况。下列就是例子：

```
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```
produces the following output (note that the initial newline is not included):
会得到下面的输出（注意最开始的换号没有被包含进来）
```
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```

Strings can be concatenated (glued together) with the `+` operator, and repeated with `*`:
字符串可以用`+`操作符来级联(拼接在一起)，并且用`*`来重复。

```
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
```

Two or more *string literals* (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
两个或更多的*字符常量*(例如用引号括起来的)彼此相隔的话会自动级联。
```
>>> 'Py' 'thon'
'Python'
```

This feature is particularly useful when you want to break long strings:
当你想要拆开一个长字符串的时候，这个特征尤其实用。
>>>
```
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
```

This only works with two literals though, not with variables or expressions:
这个只能在两个字符串常量中起作用，不可以是变量或表达式：
```
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: invalid syntax
```

If you want to concatenate variables or a variable and a literal, use `+`:
如果你想要级联变量，或级联变量和一个常量，请使用`+`:

```
>>> prefix + 'thon'
'Python'
```

Strings can be *indexed* (subscripted), with the first character having index 0\. There is no separate character type; a character is simply a string of size one:
字符串可以被*索引*（下标），第一个字符的下标是0.这里没有分离出字符类型；一个字符就是长度为1的简单字符串。

```
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
```


Indices may also be negative numbers, to start counting from the right:
下标索引也可以是负数，表示从右边开始数：

```
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
```

Note that since -0 is the same as 0, negative indices start from -1.
注意，因为-0是0是等价的，所以负数索引是从-1开始的。

In addition to indexing, *slicing* is also supported. While indexing is used to obtain individual characters, *slicing* allows you to obtain substring:
除了索引，*切片*也是支持的。当索引用来获取某一个单独的字符，切片允许获取子字符串。
```
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
```

Note how the start is always included, and the end always excluded. This makes sure that `s[:i] + s[i:]` is always equal to `s`:
注意开头的是包含的，末尾的总是不包含的。这样就能保证`s[:i] + s[i:]`总是等价于 `s`。
```
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
```
Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
切片下标的缺索引的缺省值很有用；省略的第一个下标默认是0，第二个下标的默认值是被切片的字符串的长度。
```
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
```


One way to remember how slices work is to think of the indices as pointing *between*characters, with the left edge of the first character numbered 0\. Then the right edge of the last character of a string of *n* characters has index *n*, for example:
记住切片是怎样工作的一个方法就是把下标当做是*between*在字符之间的指针，第一个字符的左边是0。最后一个字符的右边是字符串*n*个字符的*n*，例如：
```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from *i* to *j* consists of all characters between the edges labeled *i* and *j*, respectively.
第一行的数字给出了字符串中0...6的位置；第二行给出了对应的负数下标。从*i*到*j*的切片包括了边缘标签*i*和*j*之间的所有字符。

For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of `word[1:3]` is 2.
对于非负的下标，如果都在边界范围内，切边的长度就是下标的差。例如`word[1:3]` 的长度就是2.

Attempting to use an index that is too large will result in an error:
如果试图使用一个过大的索引将会导致报错：

```
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```
However, out of range slice indexes are handled gracefully when used for slicing:
然而，当使用切片的时候，下标出界是可以被优雅处理的：

```
>>> word[4:42]
'on'
>>> word[42:]
''
```

Python strings cannot be changed — they are [immutable](https://docs.python.org/3/glossary.html#term-immutable). Therefore, assigning to an indexed position in the string results in an error:
Python字符串不能被修改，他们是不可改变的。因此，为字符串的某一个下标位置赋值会导致报错：
```
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

If you need a different string, you should create a new one:
如果你需要一个不同的字符串，你应该创建新的一个：
```
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
```
The built-in function [`len()`](https://docs.python.org/3/library/functions.html#len "len") returns the length of a string:
内置函数`len()`返回字符串的长度：

```
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```

See also 参考：
[Text Sequence Type — str  文本序列类型-str](https://docs.python.org/3/library/stdtypes.html#textseq)
   - Strings are examples of *sequence types*, and support the common operations supported by such types.
      字符串是*序列类型*的一些例如，也支持这些类型支持的常见操作。

[String Methods 字符串方法](https://docs.python.org/3/library/stdtypes.html#string-methods)
   - Strings support a large number of methods for basic transformations and searching.
    字符串支持大量的方法来支持基本的转换和搜索

[Formatted string literals 格式化字符串常量](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
  - String literals that have embedded expressions.
    字符串常量有嵌入式的表达式

[Format String Syntax 格式化字符串语法](https://docs.python.org/3/library/string.html#formatstrings)<
  - Information about string formatting with [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format").
    关于字符串格式化的方法`str.format()`
[printf-style String Formatting 格式化字符串的输出格式](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)
  - The old formatting operations invoked when strings are the left operand of the `%`operator are described in more detail here.
   这里详细介绍了当字符串是`%`操作符的左操作数时将会调用的原始的格式化操作。


### 3.1.3\. Lists 列表

Python knows a number of *compound* data types, used to group together other values. The most versatile is the *list*, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
Python的*复合数据类型*是把其他值聚合在一起。最多才多艺的就是列表，它可以表示为中括号之间一系列逗号分隔的值（名目）。列表可以包含不同类型的名目，但一般所有的类型拥有相同的类型。
```
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
```

Like strings (and all other built-in [sequence](https://docs.python.org/3/glossary.html#term-sequence) type), lists can be indexed and sliced:
就像字符串（还有其他内置的序列类型），列表可以被索引和切片：

```
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
```

All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:
所有的切片操作返回一个包含所需元素的新列表。这意味着下面的切片返回了列表的一个新的（简单）拷贝：

```
>>> squares = [1, 4, 9, 16, 25]
>>> squares[-3:]
[9, 16, 25]
```

Lists also support operations like concatenation:
列表也支持拼接操作：
```
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Unlike strings, which are [immutable](https://docs.python.org/3/glossary.html#term-immutable), lists are a [mutable](https://docs.python.org/3/glossary.html#term-mutable) type, i.e. it is possible to change their content:
不像字符串的不可改变，列表是一个可以修改的类型。例如，可以修改他们的内容：
```
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
```

You can also add new items at the end of the list, by using the `append()` *method* (we will see more about methods later):
你也可以使用`append()`方法在列表的最后加上新的元素（我们将会在后面看到更多关于这个方法）
```
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
```
Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
为列表赋值也是可以的，并且这个可以改变列表的长度或者整体清空：
```
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
```

The built-in function [`len()`](https://docs.python.org/3/library/functions.html#len "len") also applies to lists:
内置的`len()`函数也是在应用在列表上：
```
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
```

It is possible to nest lists (create lists containing other lists), for example:
也可以在列表中嵌套列表（创建一个包含其他列表的列表), 例如：
```
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
```




--- TO-DO

## 3.2\. First Steps Towards Programming[](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming "Permalink to this headline")

Of course, we can use Python for more complicated tasks than adding two and two together. For instance, we can write an initial sub-sequence of the [Fibonacci series](https://en.wikipedia.org/wiki/Fibonacci_number) as follows:

>>>

<pre style="overflow: auto hidden; padding: 5px; background-color: rgb(238, 255, 204); color: rgb(51, 51, 51); line-height: 18.528px; border: 1px solid rgb(170, 204, 153); font-family: monospace, sans-serif; font-size: 15.44px; border-radius: 3px;">>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
</pre>

This example introduces several new features.

*   The first line contains a *multiple assignment*: the variables `a` and `b` simultaneously get the new values 0 and 1\. On the last line this is used again, demonstrating that the expressions on the right-hand side are all evaluated first before any of the assignments take place. The right-hand side expressions are evaluated from the left to the right.

*   The [`while`](https://docs.python.org/3/reference/compound_stmts.html#while) loop executes as long as the condition (here: `a < 10`) remains true. In Python, like in C, any non-zero integer value is true; zero is false. The condition may also be a string or list value, in fact any sequence; anything with a non-zero length is true, empty sequences are false. The test used in the example is a simple comparison. The standard comparison operators are written the same as in C: `<` (less than), `>` (greater than), `==` (equal to), `<=` (less than or equal to), `>=`(greater than or equal to) and `!=` (not equal to).

*   The *body* of the loop is *indented*: indentation is Python’s way of grouping statements. At the interactive prompt, you have to type a tab or space(s) for each indented line. In practice you will prepare more complicated input for Python with a text editor; all decent text editors have an auto-indent facility. When a compound statement is entered interactively, it must be followed by a blank line to indicate completion (since the parser cannot guess when you have typed the last line). Note that each line within a basic block must be indented by the same amount.

*   The [`print()`](https://docs.python.org/3/library/functions.html#print "print") function writes the value of the argument(s) it is given. It differs from just writing the expression you want to write (as we did earlier in the calculator examples) in the way it handles multiple arguments, floating point quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely, like this:

    >>>

    <pre style="overflow: auto hidden; padding: 5px; background-color: rgb(238, 255, 204); color: rgb(51, 51, 51); line-height: 18.528px; border: 1px solid rgb(170, 204, 153); font-family: monospace, sans-serif; font-size: 15.44px; border-radius: 3px;">>>> i = 256*256
    >>> print('The value of i is', i)
    The value of i is 65536
    </pre>

    The keyword argument *end* can be used to avoid the newline after the output, or end the output with a different string:

    >>>

    <pre style="overflow: auto hidden; padding: 5px; background-color: rgb(238, 255, 204); color: rgb(51, 51, 51); line-height: 18.528px; border: 1px solid rgb(170, 204, 153); font-family: monospace, sans-serif; font-size: 15.44px; border-radius: 3px;">>>> a, b = 0, 1
    >>> while a < 1000:
    ...     print(a, end=',')
    ...     a, b = b, a+b
    ...
    0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
    </pre>

Footnotes

<colgroup><col class="label"><col></colgroup>
| [[1]](https://docs.python.org/3/tutorial/introduction.html#id1) | Since `**` has higher precedence than `-`, `-3**2` will be interpreted as `-(3**2)`and thus result in `-9`. To avoid this and get `9`, you can use `(-3)**2`. |

<colgroup><col class="label"><col></colgroup>
| [[2]](https://docs.python.org/3/tutorial/introduction.html#id2) | Unlike other languages, special characters such as `\n` have the same meaning with both single (`'...'`) and double (`"..."`) quotes. The only difference between the two is that within single quotes you don’t need to escape `"` (but you have to escape `\'`) and vice versa. |

