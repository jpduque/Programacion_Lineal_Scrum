from cvxopt.modeling import variable, op

x1= variable()
x2= variable()
x3= variable()
x4= variable()
x5= variable()
x6= variable()
x7= variable()
x8 = variable()

def model(seniorDevCost,techDevCost, juniorDevCost, internDevCost, seniorQACost, techQACost, juniorQACost, internQACost, seniorDevDeliver, techDevDeliver, juniorDevDeliver, internDevDeliver, seniorQADeliver, techQADeliver, juniorQADeliver, internQADeliver, sprintPoints, projectPoints, projectBudget):
    global x1
    global x2
    global x3
    global x4
    global x5
    global x6
    global x7
    global x8
    c1 = (int(seniorDevDeliver)*x1 + int(techDevDeliver)*x2 + int(juniorDevDeliver)*x3 + int(internDevDeliver)*x4 + int(seniorQADeliver)*x5 + int(techQADeliver)*x6 + int(juniorQADeliver)*x7 + int(internQADeliver)*x8 >= int(sprintPoints))
    c2 = ((int(seniorDevDeliver)*x1 + int(techDevDeliver)*x2 + int(juniorDevDeliver)*x3 + int(internDevDeliver)*x4 + int(seniorQADeliver)*x5 + int(techQADeliver)*x6 + int(juniorQADeliver)*x7 + int(internQADeliver)*x8)/int(sprintPoints) <= int(projectPoints))
    c3 = (x1 + x2 + x3 + x4 >= 1)
    c4 = (x5 + x6 + x7 + x8 >= 1)
    c5 = (3*(x1+x2+x3+x4) <= (x5+x6+x7+x8) )
    c6 = ((int(seniorDevCost)*x1 + int(techDevCost)*x2 + int(juniorDevCost)*x3 + int(internDevCost)*x4 + int(seniorQACost)*x5 + int(techQACost)*x6 + int(juniorQACost)*x7 + int(internQACost)*x8)*(int(projectPoints)/int(sprintPoints)) == int(projectBudget))
    c7 = (x1 >= 0)
    c8 = (x2 >= 0)
    c9 = (x3 >= 0)
    c10 = (x4 >= 0)
    c11 = (x5 >= 0)
    c12 = (x6 >= 0)
    c13 = (x7 >= 0)
    c14 = (x8 >= 0)
    lp1 = op(int(seniorDevCost)*x1 + int(techDevCost)*x2 + int(juniorDevCost)*x3 + int(internDevCost)*x4 + int(seniorQACost)*x5 + int(techQACost)*x6 + int(juniorQACost)*x7 + int(internQACost)*x8, [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14])
    lp1.solve('glpk')
    print('\nEstado: {}'.format(lp1.status))
    print('Óptimo x1: {}'.format(round(x1.value[0])))
    print('Óptimo x2: {}'.format(round(x2.value[0])))
    print('Óptimo x3: {}'.format(round(x3.value[0])))
    print('Óptimo x4: {}'.format(round(x4.value[0])))
    print('Óptimo x5: {}'.format(round(x5.value[0])))
    print('Óptimo x6: {}'.format(round(x6.value[0])))
    print('Óptimo x7: {}'.format(round(x7.value[0])))
    print('Óptimo x8: {}'.format(round(x8.value[0])))