import math

# get suvat and which variables are known
sraw = input('displacement:\n>>> ')
sknown = sraw != ''
if sknown:
    s = float(sraw)

uraw = input('initial velocity:\n>>> ')
uknown = uraw != ''
if uknown:
    u = float(uraw)

vraw = input('final velocity:\n>>> ')
vknown = vraw != ''
if vknown:
    v = float(vraw)

araw = input('acceleration:\n>>> ')
aknown = araw != ''
if aknown:
    a = float(araw)

traw = input('time:\n>>> ')
tknown = traw != ''
if tknown:
    t = float(traw)

query = input('''what do you want to find?
s: displacement
u: initial velocity
v: final velocity
a: constant acceleration
t: time
>>> ''')[0].lower()

if query == 's':
    if sknown: print('s =', s)
    elif uknown and tknown and aknown:
        print('s =', u*t + a*t*t/2)
    elif uknown and vknown and tknown:
        print('s =', (u+v)*t/2)
    elif uknown and vknown and aknown:
        print('s =', (v*v + u*u)/2/a)
    elif vknown and tknown and aknown:
        print('s =', v*t - a*t*t/2)
    else:
        print('INSUFFICIENT DATA FOR MEANINGFUL ANSWER.')

if query == 'u':
    if uknown: print('u =', u)
    elif vknown and aknown and tknown:
        print('u =', v-a*t)
    elif sknown and aknown and tknown:
        print('u =', (s-a*t*t)/2/t)
    elif sknown and vknown and tknown:
        print('u =', 2*s/t+v)
    elif vknown and aknown and sknown:
        print('u =', math.sqrt(abs(2*a*s - v*v)))
    else:
        print('INSUFFICIENT DATA FOR MEANINGFUL ANSWER.')

if query == 'v':
    if vknown: print('v =',v)
    elif uknown and aknown and tknown:
        print('v =', u+a*t)
    elif sknown and uknown and tknown:
        print('v =', 2*s/t-u)
    elif uknown and aknown and sknown:
        print('v =', math.sqrt(u*u + 2*a*s))
    elif sknown and tknown and aknown:
        print('v =', (a*t*t + s)/2/t)
    else:
        print('INSUFFICIENT DATA FOR MEANINGFUL ANSWER.')

if query == 'a':
    if aknown: print('a =',a)
    elif vknown and uknown and tknown:
        print('a =', (v-u)/t)
    elif sknown and uknown and tknown:
        print('a =', (s-u*t)*2/t/t)
    elif vknown and uknown and sknown:
        print('a =', (v*v - u*u)/2/s)
    elif sknown and vknown and tknown:
        print('a =', (v*t - s)*2/t/t)
    else:
        print('INSUFFICIENT DATA FOR MEANINGFUL ANSWER.')

if query == 't':
    if tknown: print('t =',t)
    elif vknown and uknown and aknown:
        print('t =', (v-u)/a)
    elif sknown and uknown and aknown:
        print('t =', (math.sqrt(2*a*s + u*u) - u)/a)
    elif sknown and uknown and vknown:
        print('t =', (s*2)/(u+v))
    elif sknown and vknown and aknown:
        print('t =', (v - math.sqrt(v*v - 2*a*s))/a)
    else:
        print('INSUFFICIENT DATA FOR MEANINGFUL ANSWER.')
