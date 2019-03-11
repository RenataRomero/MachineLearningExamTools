import copy
 
def gauss(a, b):
    a = copy.deepcopy(a)
    b = copy.deepcopy(b)
    n = len(a)
    p = len(b[0])
    det = 1
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]
            b[i], b[k] = b[k], b[i]
            det = -det
 
        for j in range(i + 1, n):
            t = a[j][i]/a[i][i]
            for k in range(i + 1, n):
                a[j][k] -= t*a[i][k]
            for k in range(p):
                b[j][k] -= t*b[i][k]
 
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            t = a[i][j]
            for k in range(p):
                b[i][k] -= t*b[j][k]
        t = 1/a[i][i]
        det *= a[i][i]
        for j in range(p):
            b[i][j] *= t
    return det, b
 
a = [[3, 4, -1], [0, -2, 10], [0, 4, -2]]
b = [[-6],[-8], [-2]]
det, c = gauss(a, b)


#Se imprime el vector b
print(c)


def predict_y(b, x):

    y = b[0] + (b[1]*x[0]) + (b[2]*x[1]) + (b[3]*x[2]) + (b[4]*x[3]) + (b[5]*x[4])
    return y

#Obtiene el error con la formula
def error(y_test, y_prediction):

    y_yp_sum = 0

    #Sumatoria en la raíz
    for n in y_test:
        dif = n - y_prediction
        y_yp_sum += dif

#Recorre cada una de las filas de la información de teste y hace la prediccion
for n in filetest:
    y_predictions += predict_y(b,n)

#Una vez que se tienen todas las predicciones se calcula el error en base a el número real
print(error(filetest_y, y_predictions)) #Se imprime el error


