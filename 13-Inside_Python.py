"""
Python is a Interpreted Language means executed Line by Line. It doesnot have the compiler but does compile into something called compiler
like

text-file -> parser                  "Your Code in Text file is parsed by Python"
parser -> AST                        "Python Parser Converts your Code into AST (Abstract Syntax Tree)"
AST -> Bytecode                      "AST is compiled into the ByteCode"
ByteCode -> Python Virtual Machine   "PVM is actually executing the ByteCode."
PVM -> C Lang Code                   "PVM is a C Loop, actually implemented in C Lang execute your byteCode line by line on CPU."
C Lang Code executed in CPU.         "PVM is actaully a C Lang Code which execute the ByteCode on CPU line by Line (Interpret). "


cpython is the engine implemented in c Language which performs all the steps above. It compile the code into ByteCode and then Interpreted line by line usig PVM.

==> Note: " .py -> .pyc -> PVM -> CPU "

At, the time of executing the Program, Python stores ByteCode into the Memory (compiled Python Code 'pyc'), then interpreted line by line. and also in .pyc file (__pycache__) for reuse.


Key Concepts:

Passed by Reference:
    1. List
    2. Dict
    3. Tuple (Immutable cannot change it) and set

    -> In Memory, their memory reference is passed if the variable of these datatypes are passed to some other variable. Changing one will effect others.
    
Passed by Value:
    1. String
    2. Int & Float
    3. Bool
    4. None

    -> In Memory, there value are stored, and these variables are pointing to the memory location. Variables of same value point to same memory location. Changing on will not effect other.
    
Import Libarary:
     -> First check either exist in build-in libraries which come with python otherwise lock at the downloaded ones in venv or global env.


"""