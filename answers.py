# -*- coding: utf-8 -*-

# This is the answers file for the CMPSC 473 - Spring 2019 - Project #1
# Answers data structures
# DO NOT MODIFY THESE VARIABLES HERE
wordy = {
    "1b": None,
    "1d": None,
    "1e": None,
    "2b": None,
    "2c": None,
    "2d": None,
    "2e": None,
    "3b": None,
    "3c": None,
    "4a": None,
    "4bi": None,
    "4bii": None,
    "4biii": None,
    "4biv": None,
    "4bv": None,
    "4bvi": None
}
numerical = {
    "1a": None,
    "1c": None,
    "2ai32": None,
    "2aii32": None,
    "2aiii32": None,
    "2ai64": None,
    "2aii64": None,
    "2aiii64": None,
    "3ai32": None,
    "3aii32": None,
    "3aiii32": None,
    "3ai64": None,
    "3aii64": None,
    "3aiii64": None,
}

###########################################################
# Answer Section
# You may edit the values of variables below
###########################################################

# FILL OUT YOUR ID AND ANSWERS BELOW
# PSU ID (e.g. xyz1234)
ID = "nmn5152"

###########################################################
# (1) Stack, heap, and system calls
###########################################################

# (1.a) What is the size of the proces stack when it is
#   waiting for user input?
#   Enter your answer in bytes.
numerical["1a"] = 86016

# (1.b) Which addresses are for the local variables and
#   which ones are for the dynamically allocated variables?
#   What are the directions in which the stack and the heap
#   grow on your system?
wordy["1b"] = '''Address 1 is for local variables, Address 2 is for dynamically allocated variables.
The stack grows from high to low, the heap grows from low to high.'''

# (1.c) What is the size of the process heap when it
#   is waiting for user input?
#   Enter your answer in bytes.
numerical["1c"] = 135168

# (1.d) What are the address limits of the stack and the heap?
wordy["1d"] = '''stack: 7ffcedf99000-7ffcedfae000, heap: 0143e000-0145f000'''

# (1.e) For each unique system call, write in your own words
#   (just one sentence should do) what purpose this system
#   call serves for this program.
wordy["1e"] = '''

execve("./prog1", ["prog1"], [/* 50 vars */]) = 0: Takes 3 arguments, the filename of a program 
which it executes upon call with no return on success, an array of string arguments to pass to 
that program(the first of which is the filename), and another array of strings that are passed 
in as the environment of the program.

brk(0) = 0x1cf5000: Changes where the program break is, does this by setting the end of the data 
segment to the value of its one argument (0 in this case). Returns 0 on success, -1 on error.

mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f9b72702000: Creates
a new mapping in the virtual address space starting from the address specified by the first argument,
with a length specified by the second argument, so 4096. Since the first argument is NULL in this
case, the kernel chooses the address to start the mapping. PROT_READ|PROT_WRITE are file protection
flags that indicates pages may be read and written, while the MAP_PRIVATE|MAP_ANONYMOUS flags indicates
that a private anonymous mapping should be created. The last two arguments are the file descriptor of
-1, and the offset of 0. On success, return a pointer to the location of the mapping.

access("/etc/ld.so.preload", R_OK) = -1 ENOENT (No such file or directory): This call to access checks
if the calling process can access the filename indicated by the first argument, "/etc/ld.so.preload".
The R_OK flag indicates that this access call will check if the file exists, and then grant read access
if it does. Since this call returns -1, access could not find the file specified by the filename passed.

open("/etc/ld.so.cache", O_RDONLY) = 3: Attempts to open the file specified by the filename passed in
as the first argument, "/etc/ld.so.cache". The second argument is the mode with which it should be
opened, and the O_RDONLY flag indicates it should be opened in read only mode. The return value is
the new file descriptor for the opened file.

fstat(3, {st_mode=S_IFREG|0644, st_size=304676, ...}) = 0: Returns information about the file that is 
specified by the file descriptor table that is passed in as the first argument (3 in this case). It
stores this information in the buffer described by the second argument. Returns 0 on success.

close(3): Closes the file descriptor specified by the value of its argument (3), so it doesn't reference
a file anymore. It does not delete the file descriptor, but instead the descriptor may be reused. Returns
0 on success.

read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0000\356\1\217<\0\0\0"..., 832) = 832: Reads from
the file descriptor specified by the first argument, reading a number of bytes specified by the third
argument into a buffer described by the second argument. Returns the number of bytes successfully read.

mprotect(0x3c8f18b000, 2093056, PROT_NONE) = 0: Changes the access protection of the address range given
by the address in the first argument and the size of the range in the second argument. For example, the 
interval in this case would be [0x3c8f18b000, 0x3c8f18b000 + 2093056 - 1]. The protection flag in this
case is PROT_NONE, indicating the memory in this range will be inaccessible. Returns 0 on success.

arch_prctl(ARCH_SET_FS, 0x7f9b726b5700) = 0: Sets an architecture specific thread state. The second
argument is passed to the subfunction specified by the first argument. In this case, the ARCH_SET_FS
subfunction sets the second argument as the 64 bit base for the FS register. Returns 0 on success.

munmap(0x7f9b726b7000, 304676) = 0: Deletes the mapping in the address range specified by the address
passed as the first argument, and the range length passed as the second argument. In this case, the
range would be [0x7f9b726b7000, 0x7f9b726b7000 + 304676 - 1]. Returns 0 on success.

write(1, "Memory Growth : \n", 17) = 17: Writes into the file specified by the descriptor passed in 
as the first argument, writing a number of bytes indicated by the third argument from the buffer
passed in as the second argument. In this case, all 17 bytes from the second argument are written
into the file indicated by the descriptor with a value of 1. Returns the number of bytes written.

exit_group(0): Terminates calling thread and all threads in the calling processes thread group.
Does not return.

'''
###########################################################
# (2) Debugging Refresher
###########################################################

# (2.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables

# (2.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
numerical["2ai32"] = 4096

# (2.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["2aii32"] = 14147584

# (2.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["2aiii32"] = 1789952

# (2.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["2ai64"] = 4096

# (2.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["2aii64"] = 16252928

# (2.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["2aiii64"] = 3874816

# (2.b) Use gdb to find the program statement that
#   caused the error
wordy["2b"] = '''Errant Line: allocate(count - 1);'''

# (2.c) Explain the cause of this error.
wordy["2c"] = '''The allocate call is trying access memory at the location 0x7fffff36713c, which is out
of the address range of the stack, indicating stack overflow.'''

# (2.d) Examine individual frames in the stack to find each
#   frame's size. Estimate the number of invocations of the
#   recursive function that should be possible. How many
#   invocations occur when you actually execute the program?
wordy["2d"] = '''The size of each stack frame is 1200048 bytes. The total stack size is 12009472 bytes.
Dividing these numbers gives 10.007, so I estimate the program should be able to invoke the function 10
times. Looking at the information for the call stack, the function is recursively invoked 10 times, after
which the program hits a segmentation fault.'''

# (2.e) What are the contents of a frame in general?
#   Which of these are present in a frame corresponding
#   to an invocation of the recursive function and
#   what are their sizes?
wordy["2e"] = '''A stack frame includes the arguments passed to a function, its local variables, its return
address, its instruction pointer, any saved registers,  as well as the address where the function is being 
executed. In this particular program the stack frames include the frame's address, its arguments, its local
variables, its instruction pointers, saved registers, as well as information of its caller. The size of the
invocation is 16 bytes.'''

###########################################################
# (3) More debugging
###########################################################

# (3.a) Observe and report the differences in the following
#   for the 32-bit and 64-bit executables:

# (3.a.i.32) size of compiled code (32-bit)
#   Enter your answer in bytes.
numerical["3ai32"] = 4096

# (3.a.ii.32) size of code during run time (32-bit)
#   Enter your answer in bytes.
numerical["3aii32"] = 447676416

# (3.a.iii.32) size of linked libraries (32-bit)
#   Enter your answer in bytes.
numerical["3aiii32"] = 1961984

# (3.a.i.64) size of compiled code (64-bit)
#   Enter your answer in bytes.
numerical["3ai64"] = 4096

# (3.a.ii.64) size of code during run time (64-bit)
#   Enter your answer in bytes.
numerical["3aii64"] = 44518313984

# (3.a.iii.64) size of linked libraries (64-bit)
#   Enter your answer in bytes.
numerical["3aiii64"] = 6512640

# (3.b) Use valgrind to find the cause of the error
#   including the program statement causing it
wordy["3b"] = '''The errant line of code is memset(ch1,'*',sizeof(b[0])+i). The problem here is that
address 0x0 is not stack'd, malloc'd or (recently) free'd, and access is not within the mapped region 
at address 0x0, as stated in valgrind. This indicates that address 0x0 is an invalid address, not in
the virtual address space, leading to error.'''

# (3.c) How is this error different than the one for prog2?
wordy["3c"] = '''The error in prog2 arises because the program is trying to access an address which is
out of the address range of the stack, due to stack overflow. For prog3, address 0x0 is instead an invalid
address, not in the virtual address space.'''

###########################################################
# (4) And some more
###########################################################

# (4.a) Describe the cause and nature of these errors.
#   How would you fix them?
wordy["4a"] = '''There is significant memory leakage occuring when the program is run, which appears to be
because in the allocate method, the p is freed inside an if statement that doesn't appear to be executing
below the malloc. By taking this free out of the if statement, the memory leakage is resolved.'''

# (4.b) Modify the program to use getrusage for measuring the following:

# (4.b.i) user CPU time used
wordy["4bi"] = '''0.139670697596605 seconds'''

# (4.b.ii) system CPU time used
#   What is the difference between (i) and (ii)?
wordy["4bii"] = '''0.1926009 seconds'''

# (4.b.iii) maximum resident set size
#   what is this?
wordy["4biii"] = '''636 kb'''

# (4.b.iv) signals received
#   Who may have sent these?
wordy["4biv"] = "0"

# (4.b.v) voluntary context switches
wordy["4bv"] = "7"

# (4.b.vi) involuntary context switches
#   what is the difference between (v) and (vi)?
wordy["4bvi"] = "2"

###########################################################
# Sanity Check
# DO NOT MODIFY ANYTHING BELOW HERE
###########################################################
if ID == "":
    print("Please fill out your student ID in the variable ID")
for key in numerical:
    if type(numerical[key]) is not int:
        print("Type error of answer %s (should be a numerical value)" % key)
for key in wordy:
    if type(wordy[key]) is not str:
        print("Type error of answer %s (should be a string)" % key)
