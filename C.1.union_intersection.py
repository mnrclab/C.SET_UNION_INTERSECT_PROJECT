A = {2, 3, 5, 7}
B = {5, 7, 9}

#a. Tentukan A
print('A: ', A)

#b. Tentukan B
print('B:', B)

#c. Tentukan (A n B)
c = A & B
print('A n B:', c)

#d. Tentukan (A u B)
d = A | B
print('A u B:', d)

#e. Tentukan A n (A u B)
print('A n (A u B):', A & d)

#f. Tentukan B n (A u B)
print('B n (A u B):', B & d)

#g. Tentukan (A u B) n (A u B)
print('(A u B) n (A u B)', d & d)

#h. Tentukan (A n B) u (A n B)
print('(A n B) u (A n B):', c | c)
