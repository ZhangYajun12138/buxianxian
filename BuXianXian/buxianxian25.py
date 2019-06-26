# encoding: utf-8
# functions
"""
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
"""

# def abs(*args, **kwargs):  # real signature unknown
""" Return the absolute value of the argument. """
# 返回数字的绝对值，参数可以是整数、浮点数或者复数
print(abs(2))  # 正整数
print(abs(-2))  # 负整数
print(abs(0))  # 0
print(abs(1.6))  # 正浮点数
print(abs(-1.6))  # 负浮点数
# 如果参数是一个复数，此方法返回此复数的绝对值（此复数与它的共轭复数的乘积的平方根）
c1 = complex(1, 1)
print(c1)  # 复数
print(abs(c1))  # 复数绝对值
print("-" * 80)

# def all(*args, **kwargs):  # real signature unknown
"""
Return True if bool(x) is True for all values x in the iterable.
If the iterable is empty, return True.
"""
# 接受一个可迭代器对象为参数，当参数为空或者不为可迭代器对象是报错
# all(2) error
# 如果可迭代器对象中每个元素的逻辑值均为True时，返回True，否则返回False
print(all([1, 2]))  # 列表中每个元素的逻辑值均为True，返回True
print(all([0, 1]))  # 列表中0的逻辑值为False，返回False
# 如果可迭代器对象为空(元素个数为0)，返回True
print(all(()))  # 空元组
print(all({}))  # 空字典
print(all([]))  # 空列表
print('-' * 80)

# def any(*args, **kwargs):  # real signature unknown
"""
Return True if bool(x) is True for any x in the iterable.
If the iterable is empty, return False.
"""
# 接受一个可迭代器对象为参数，当参数为空或者不为的迭代器对象时报错
# any(2) error
# 如果可迭代对象汇总其中有一个元素的逻辑值为True时，返回True；全部值为False时返回False
print(any([1, 2, 3, 0]))  # 列表元素中有一个为True，返回True
print(any([0, 0]))  # 列表元素全部为False，返回False
# 如果可迭代对象为空（元素个数为0），返回False
print(any([]))  # 空列表
print(any({}))  # 空字典
print(any(()))  # 空元组
print('-' * 80)

# def ascii(*args, **kwargs):  # real signature unknown
"""
Return an ASCII-only representation of an object.
As repr(), return a string containing a printable representation of an
object, but escape the non-ASCII characters in the string returned by
repr() using \\x, \\u or \\U escapes. This generates a string similar
to that returned by repr() in Python 2.
"""
# 返回一个可打印的对象字符串方式表示，如果是非ascii字符就会输出\x，\u或\U等字符来表示
print(ascii(1))
print(ascii('&'))
print(ascii(900000))
print(ascii('中文'))  # 非ascii字符
print('-' * 80)

# def bin(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
"""
Return the binary representation of an integer.
   >>> bin(2796202)
   '0b1010101010101010101010'
"""
# 将一个整型数字转换成二进制字符串
print(bin(16))
print(type(bin(2)))


# 如果参数不是一个整数，则必须定义一个__index__()方法，并且方法返回值必须是整数
class C:
    def __index__(self):
        return 3


c = C()
print(bin(c))
print(type(bin(c)))
print('-' * 80)

# def breakpoint(*args, **kws):  # real signature unknown; restored from __doc__
"""
breakpoint(*args, **kws)
Call sys.breakpointhook(*args, **kws).  sys.breakpointhook() must accept
whatever arguments are passed.
By default, this drops you into the pdb debugger.
"""

# def callable(i_e_, some_kind_of_function):  # real signature unknown; restored from __doc__
"""
Return whether the object is callable (i.e., some kind of function).
Note that classes are callable, as are instances of classes with a
__call__() method.
"""
# 检测对象是否可被调用，对象能否使用()括号中的方法调用
print(callable(callable))
print(callable(1))


# 可调用对象，在实际调用也可能调用失败；但是不可调用对象，调用肯定不成功
# 类对象都是可被调用对象，类的实例对象是否可调用对象，取决于类是否定义了__call__方法
class A:
    pass


print(callable(A))  # 类对象A是可被调用对象
a = A()  # 调用A
print(callable(a))  # 实例对象不可调用


# a() 调用实例a失败
class B:
    def __call__(self, *args, **kwargs):
        print("can callable")


callable(B)  # 类对象B是可被调用对象
b = B()  # 调用B
callable(b)  # 实例对象b是可被调用对象
b()
print("-" * 80)

# def chr(*args, **kwargs):  # real signature unknown
""" Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff. """
# 返回整形参数值所对应的Unicode字符的字符串表示
print(chr(97))
print(type(chr(97)))
# 功能与ord函数相反
print(ord('a'))
print(type(ord('a')))
# 传入的参数值范围0-1114111（十六进制0x10FFFF）之间
# chr(-1) error
print('-' * 80)


# classmethod
# 装饰器函数，标识一个方法为类方法
# 类方法的第一个参数是类对象参数，在方法被调用的时候自动将类对象传入，参数名称约定为cls
# 如果一个方法被标识为类方法，则该方法可被类对象调用，也可被类的实例对象调用
class D:
    @classmethod
    def func(cls, arg1):
        print(cls)
        print(arg1)


D.func('类对象调用类方法')
d = D()
d.func("类实例对象调用类方法")


# 类被继承后，子类也可用调用父类的类方法，但是第一个参数传入的是子类的类对象
class E(D):
    pass


E.func('子类的类对象调用父类的类方法')
e = E()
e.func("子类的实例对象调用父类的类方法")
print('-' * 80)
# def compile(*args, **kwargs):  # real signature unknown
"""
compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

Compile source into a code object that can be executed by exec() or eval().

The source code may represent a Python module, statement or expression.
The filename will be used for run-time error messages.
The mode must be 'exec' to compile a module, 'single' to compile a
single (interactive) statement, or 'eval' to compile an expression.
The flags argument, if present, controls which future statements influence
the compilation of the code.
The dont_inherit argument, if true, stops the compilation inheriting
the effects of any future statements in effect in the code calling
compile; if absent or false these statements do influence the compilation,
in addition to any features explicitly specified.
"""
# 将source编译为代码或者AST对象。代码对象能够通过exec语句来执行或者eval()进行求值。
# 参数source：字符串或者AST（Abstract Syntax Trees）对象。即需要动态执行的代码段。
# 参数 filename：代码文件名称，如果不是从文件读取代码则传递一些可辨认的值。当传入了source参数时，filename参数传入空字符即可。
# 参数mode：指定编译代码的种类，可以指定为 ‘exec’,’eval’,’single’。
# 当source中包含流程语句时，mode应指定为‘exec’；
code1 = 'for i in range(10):print(i)'
compile1 = compile(source=code1, filename='', mode='exec')
exec(compile1)
# 当source中只包含一个简单的求值表达式，mode应指定为‘eval’；
code2 = '1+2+3+4+5'
compile2 = compile(code2, '', 'eval')
eval(compile2)
# 当source中包含了交互式命令语句，mode应指定为'single'。
# code3 = 'name=input("please input your name:")'
# compile3 = compile(code3, '', 'single')
# exec(compile3)
# print(name)
print('-' * 80)

# def copyright(*args, **kwargs):  # real signature unknown
"""
interactive prompt objects for printing the license text, a list of
    contributors and the copyright notice.
"""


# def credits(*args, **kwargs):  # real signature unknown
#     """
#     interactive prompt objects for printing the license text, a list of
#         contributors and the copyright notice.
#     """
#     pass

# def delattr(x, y):  # real signature unknown; restored from __doc__
#     """
#     Deletes the named attribute from the given object.
#
#     delattr(x, 'y') is equivalent to ``del x.y''
#     """
#     pass
# 删除指定对象的指定名称的属性，作用和setattr相反
class classF:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("say")


a = classF('zhang')
print(a.name)
a.say()
delattr(a, 'name')


# delattr(a,'say')#不能删除对象的方法
# print(a.name) 已删除，不能调用
# delattr(a, 'name')  # 删除不存在的属性，报错


def dir(p_object=None):  # real signature unknown; restored from __doc__
    """
    dir([object]) -> list of strings

    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.
    """
    return []


def divmod(x, y):  # known case of builtins.divmod
    """ Return the tuple (x//y, x%y).  Invariant: div*y + mod == x. """
    return (0, 0)


def eval(*args, **kwargs):  # real signature unknown
    """
    Evaluate the given source in the context of globals and locals.

    The source may be a string representing a Python expression
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
    """
    pass


def exec(*args, **kwargs):  # real signature unknown
    """
    Execute the given source in the context of globals and locals.

    The source may be a string representing one or more Python statements
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
    """
    pass


def exit(*args, **kwargs):  # real signature unknown
    pass


def format(*args, **kwargs):  # real signature unknown
    """
    Return value.__format__(format_spec)

    format_spec defaults to the empty string.
    See the Format Specification Mini-Language section of help('FORMATTING') for
    details.
    """
    pass


def getattr(object, name, default=None):  # known special case of getattr
    """
    getattr(object, name[, default]) -> value

    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.
    """
    pass


def globals(*args, **kwargs):  # real signature unknown
    """
    Return the dictionary containing the current scope's global variables.

    NOTE: Updates to this dictionary *will* affect name lookups in the current
    global scope and vice-versa.
    """
    pass


def hasattr(*args, **kwargs):  # real signature unknown
    """
    Return whether the object has an attribute with the given name.

    This is done by calling getattr(obj, name) and catching AttributeError.
    """
    pass


def hash(*args, **kwargs):  # real signature unknown
    """
    Return the hash value for the given object.

    Two objects that compare equal must also have the same hash value, but the
    reverse is not necessarily true.
    """
    pass


def help():  # real signature unknown; restored from __doc__
    """
    Define the builtin 'help'.

        This is a wrapper around pydoc.help that provides a helpful message
        when 'help' is typed at the Python interactive prompt.

        Calling help() at the Python prompt starts an interactive help session.
        Calling help(thing) prints help for the python object 'thing'.
    """
    pass


def hex(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
    """
    Return the hexadecimal representation of an integer.

       >>> hex(12648430)
       '0xc0ffee'
    """
    pass


def id(*args, **kwargs):  # real signature unknown
    """
    Return the identity of an object.

    This is guaranteed to be unique among simultaneously existing objects.
    (CPython uses the object's memory address.)
    """
    pass


def input(*args, **kwargs):  # real signature unknown
    """
    Read a string from standard input.  The trailing newline is stripped.

    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
    """
    pass


def isinstance(x, A_tuple):  # real signature unknown; restored from __doc__
    """
    Return whether an object is an instance of a class or of a subclass thereof.

    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
    """
    pass


def issubclass(x, A_tuple):  # real signature unknown; restored from __doc__
    """
    Return whether 'cls' is a derived from another class or is the same class.

    A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
    or ...`` etc.
    """
    pass


def iter(source, sentinel=None):  # known special case of iter
    """
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.
    """
    pass


def len(*args, **kwargs):  # real signature unknown
    """ Return the number of items in a container. """
    pass


def license(*args, **kwargs):  # real signature unknown
    """
    interactive prompt objects for printing the license text, a list of
        contributors and the copyright notice.
    """
    pass


def locals(*args, **kwargs):  # real signature unknown
    """
    Return a dictionary containing the current scope's local variables.

    NOTE: Whether or not updates to this dictionary will affect name lookups in
    the local scope and vice-versa is *implementation dependent* and not
    covered by any backwards compatibility guarantees.
    """
    pass


def max(*args, key=None):  # known special case of max
    """
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
    """
    pass


def min(*args, key=None):  # known special case of min
    """
    min(iterable, *[, default=obj, key=func]) -> value
    min(arg1, arg2, *args, *[, key=func]) -> value

    With a single iterable argument, return its smallest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the smallest argument.
    """
    pass


def next(iterator, default=None):  # real signature unknown; restored from __doc__
    """
    next(iterator[, default])

    Return the next item from the iterator. If default is given and the iterator
    is exhausted, it is returned instead of raising StopIteration.
    """
    pass


def oct(*args, **kwargs):  # real signature unknown; NOTE: unreliably restored from __doc__
    """
    Return the octal representation of an integer.

       >>> oct(342391)
       '0o1234567'
    """
    pass


def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None,
         closefd=True):  # known special case of open
    """
    Open file and return a stream.  Raise OSError upon failure.

    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)

    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:

    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================

    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.

    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.

    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.

    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:

    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.

    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.

    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.

    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.

    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:

    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.

    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.

    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.

    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).

    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.

    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.
    """
    pass


def ord(*args, **kwargs):  # real signature unknown
    """ Return the Unicode code point for a one-character string. """
    pass


def pow(*args, **kwargs):  # real signature unknown
    """
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.
    """
    pass


def print(self, *args, sep=' ', end='\n', file=None):  # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    pass


def quit(*args, **kwargs):  # real signature unknown
    pass


def repr(obj):  # real signature unknown; restored from __doc__
    """
    Return the canonical string representation of the object.

    For many object types, including most builtins, eval(repr(obj)) == obj.
    """
    pass


def round(*args, **kwargs):  # real signature unknown
    """
    Round a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
    """
    pass


def setattr(x, y, v):  # real signature unknown; restored from __doc__
    """
    Sets the named attribute on the given object to the specified value.

    setattr(x, 'y', v) is equivalent to ``x.y = v''
    """
    pass


def sorted(*args, **kwargs):  # real signature unknown
    """
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    """
    pass


def sum(*args, **kwargs):  # real signature unknown
    """
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers

    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
    """
    pass


def vars(p_object=None):  # real signature unknown; restored from __doc__
    """
    vars([object]) -> dictionary

    Without arguments, equivalent to locals().
    With an argument, equivalent to object.__dict__.
    """
    return {}


def __build_class__(func, name, *bases, metaclass=None, **kwds):  # real signature unknown; restored from __doc__
    """
    __build_class__(func, name, *bases, metaclass=None, **kwds) -> class

    Internal helper function used by the class statement.
    """
    pass


def __import__(name, globals=None, locals=None, fromlist=(), level=0):  # real signature unknown; restored from __doc__
    """
    __import__(name, globals=None, locals=None, fromlist=(), level=0) -> module

    Import a module. Because this function is meant for use by the Python
    interpreter and not for general use, it is better to use
    importlib.import_module() to programmatically import a module.

    The globals argument is only used to determine the context;
    they are not modified.  The locals argument is unused.  The fromlist
    should be a list of names to emulate ``from name import ...'', or an
    empty list to emulate ``import name''.
    When importing a module from a package, note that __import__('A.B', ...)
    returns package A when fromlist is empty, but its submodule B when
    fromlist is not empty.  The level argument is used to determine whether to
    perform absolute or relative imports: 0 is absolute, while a positive number
    is the number of parent directories to search relative to the current module.
    """
    pass
