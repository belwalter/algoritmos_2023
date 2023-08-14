$ontext
Nota el identificador de la ecuación va precedido de dos puntos. En las ecuaciones el símbolo =E= significa igual, =G= significa mayor que y =L= significa menor que

Un sastre tiene las siguientes materias primas a disposición: 16 m2 de algodón, 11 m2 de seda y 15 m2 de lana.
Un traje requiere lo siguiente: 2 m2 de algodón, 1 m2 de seda y 1 m2 de lana. Una túnica: 1 m2 de algodón, 2 m2 de seda y 3 m2 de lana.
Si el traje se vende por $30 y la túnica por $50,
¿Cuántas piezas de cada confección debe hacer el sastre para obtener la máxima cantidad de dinero?
Halle la solución gráfica y analítica por el método del simplex. ¿Qué restricciones están saturadas y cuáles no?, ¿Qué significa esto?


2 X1 + 1 X2 + 1 X3 = 16   Algodon
1 X1 + 2 X2 + 1 X4 = 11   Lana
1 X1 + 3 X2 + 1 X5 = 15   Seda
$offtext

Variables x1, x2, F;

Positive Variables
x1,x2;

Equations objective, constr1, constr2, constr3;
objective.. F =E= 30*x1 + 50*x2;
constr1..   2*x1+1*x2=L=16;
constr2..   1*x1+2*x2=L=11;
constr3..   1*x1+3*x2=L=15;

Model EjercicioI /objective, constr1, constr2, constr3/;
Solve EjercicioI Using LP maximizing F;