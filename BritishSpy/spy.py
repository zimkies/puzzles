code = '''
eb 04 af c2 bf a3 81 ec
0c fe c1 75 f9 31 c0 ba 
d0 c1 ca 08 8a 1c 0c 8a 
fe c1 75 e8 39 5c 00 00 
00 5c 58 3d 41 41 41 41 
75 3b 5a 89 d1 89 36 89 
d1 89 df 29 cf 31 c0 31 
8a 14 06 8a 34 1e 88 34 
8a 1c 16 8a 17 30 da 88 
d8 fe c0 cd 80 90 90 e8

00 01 00 00 31 c9 88 0c
ef be ad de 02 04 0c 00
3c 04 88 1c 04 88 3c 0c
00 89 e3 81 c3 04 00 00
75 43 58 3d 42 42 42 42 
df 29 cf f3 a4 89 de 89
db 31 d2 fe c0 02 1c 06
06 88 14 1e 00 f2 30 f6
17 47 49 75 de 31 db 89
9d ff ff ff 41 41 41 41
'''


code2 = '''
eb 04 af c2 bf a3 81 ec 00 01 00 00 31 c9 88 0c
0c fe c1 75 f9 31 c0 ba ef be ad de 02 04 0c 00
d0 c1 ca 08 8a 1c 0c 8a 3c 04 88 1c 04 88 3c 0c
fe c1 75 e8 39 5c 00 00 00 89 e3 81 c3 04 00 00
00 5c 58 3d 41 41 41 41 75 43 58 3d 42 42 42 42 
75 3b 5a 89 d1 89 36 89 df 29 cf f3 a4 89 de 89
d1 89 df 29 cf 31 c0 31 db 31 d2 fe c0 02 1c 06
8a 14 06 8a 34 1e 88 34 06 88 14 1e 00 f2 30 f6
8a 1c 16 8a 17 30 da 88 17 47 49 75 de 31 db 89
d8 fe c0 cd 80 90 90 e8 9d ff ff ff 41 41 41 41
'''


def straightcode(string=code):
    return reduce(lambda f1, f2: f1+f2, reduce(lambda z1, z2: z1+z2,  [y.split(' ') for y in string.split('\n')]))
