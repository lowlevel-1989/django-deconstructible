## test1.py
~~~
- A
__init__ () {}
__call__ () {}
- B
__init__ () {}
__call__ ('hello',) {}
- C
__init__ ('hello',) {}
__call__ () {}
compare A == B   True
compare A == C   True
compare C == str False
~~~
## test2.py
~~~
- A
__init__ ('vinicio',) {'job': 'dev'}
__main__.T2
('vinicio',)
{'job': 'dev'}
_T2
- B
__init__ ('vinicio',) {'job': 'dev'}
- C
__init__ ('vicky',) {'job': 'design'}
compare A == B   True
compare A == C   True
~~~
