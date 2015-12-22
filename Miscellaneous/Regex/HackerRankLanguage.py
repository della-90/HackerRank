import re
n = int(input())

list = 'C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC'.split(':')
pattern = r'(?P<id>\d{4,5}) (?P<lang>\w+)'
regex = re.compile(pattern, re.I)
for _ in range(0, n):
    s = input()
    res = regex.match(s)
    if (res):
        id, lang = res.groups()
        if (10**4 <= int(id) <= 10**5 and lang in list):
            print('VALID')
            continue
    print('INVALID')
    
