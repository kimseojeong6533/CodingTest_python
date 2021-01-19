from sys import stdin

sik=stdin.readline()

plma=['-','+']

sub_alpha=''
alphas=[]
sub_plma=[]
for i in range(len(sik)):
    if sik[i] in plma:
        alphas.append(int(sub_alpha))
        sub_alpha=''
        sub_plma.append(sik[i])
    else:
        sub_alpha+=sik[i]

alphas.append(int(sub_alpha))

print(alphas, sub_plma)




