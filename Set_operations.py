# range in 2.7 that doesn't create lists:
xrange(6)

# get the object and position:
for i, color in enumerate([1,2,3,6])

# pair lists
zip(list1, list2)

# zip without creating a new list
izip(list1,list2)

# Costum sorts:
sorted(colors, cmp=Function_that_says_if_input_1_is_bigger_then_input2)
# or (replace len by any function mapping to comparable objects):
sorted(colors, key=len)

# call function until a sentinel values:
blocks = []
for block in iter(partial(f.read, 32), ''):
   blocks.append(block)

# find if a for loop was broken out of:
for i, value in enumerate(seq):
   if value=tgt:
      break
else:
   return -1
return i

# "cool" dictionary creation:
d = {k : d[k] for k in d if not k.startswith('r') }

#d.keys() creates a copy of keys of dict, so that dict can be mutated safely
for k in d.keys()
   if k.startswith('r'):
      del d[k]

# any bi-tuple iterator is a valid construction source for a dict:
d = dict(izip(names, colors))

# there are better ways to create default values in dicts then if loop:
d = {}
for color in colors:
   d[color] = d.get(color, 0)+1

d = defaultdict(int)
for color in colors:
   d[color] += 1

d = {}
for name in names:
   key = len(name)
   d.setdefault(key, []).append(name)

d = defaultdict(list)
for name in names:
   key = len(name)
   d[key].append(name)

# it is possible chaining dictionnary lookups without replicating the dicts:
d = ChainMap(command_line_args, os.environ, defaults)

# functions with multiple "options" commands are better off clarified upon use:
twitter_search('@obama', retweets=False, numtweets=20, popular=True)

# Named tuples are great to know what is going on in the return of random
# function:
TestResults = namedtuple('TestResults', ['failed', 'attempted'])
TestResults[0]
TestResults[1]

# String concatenation: usual s+=', '+name is quadratic in complexity because
# strings are immutable
print ', '.join(names)

# lists should not be used as queues. this is the function of deque:
names = deque[some_list]

del names[0]
names.popleft()
names.appendleft('mark')

# decorators should be used to factor out administrative logic from methods:
@cache
def web_lookup(url):
   return urllig.urlopen(url).read()

def cache(func):
   saved = {}
   @wraps(func)
   def newfunc(*args):
      if args in saved:
          return saved(*args)
        result = func(*args)
        saved[args] = result
        return result
   return newfunc
   
# factor out context:
with localcontext(Context(prec=50)):
   print Decimal(355) / Decimal(113)

# better file IO: 
with open('data.txt') as f:
   data = f.read()

# threading lock:
lock = threading.Lock()

with lock:
   print 'Critical section 1'
   print 'Critical section 2'

# Ignore specific error type:
with ignored(OSError):
   os.remove('somefile.tmp')

@contextmanager
def ignored(*exceptions):
   try:
      yield
   except exceptions:
      pass

# redirect temporary contexts:
with open('somefile.txt', 'w') as f:
   with redirect_stout(f):
      help(pow)

@ contextmanager
def redirect_stdout(fileobj):
   oldstdout = sys.stdout
   sys.stdout = fileobj
   try:
      yeld fieldobj
   finally:
      sys.stdout = oldstout

