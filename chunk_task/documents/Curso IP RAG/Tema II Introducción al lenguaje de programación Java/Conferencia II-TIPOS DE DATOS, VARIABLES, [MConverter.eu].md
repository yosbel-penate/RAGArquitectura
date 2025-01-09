1972

UNIVERSIDAD

DE MATANZAS

TIPOS DE DATOS, VARIABLES, CONSTANTES, IDENTIFICADORES

Julio / 2019

INTRODUCCI ÓN A LA PROGRAMACI ÓN

INGENIERÍA EN INFORMÁTICA

Objetivos I Caracterizar las variables como parte de la construcción de un programa computacional. 

I Caracterizar los tipos de datos como parte de la construcción de un programa computacional. 

Objetivos I Caracterizar los identificadores como parte de la construcción de un programa computacional. 

I Caracterizar las constantes como parte de la construcción de un programa computacional. 

Sumario I Variables. 

I Tipos de datos. 

I Constantes. 

I Identificadores. 

Bibliografia I La Esencia de la Lógica de Programación. 

I Manual algoritmos. 

I Aprenda Java como si estuviera en primero. 

Variables Informalmente algo variable es algo que puede cambiar de un momento a otro. 

Técnicamente una variable es un campo de memoria al que se le puede cambiar su contenido cuantas veces sea necesario. 

Variables Para poder utilizar variables en el desarrollo de un programa de computador se debe primero decir qué tipo de dato van a almacenar pues las variables son como unas cajitas de diferentes tama˜

nos y por tal motivo

se deben declarar previamente para que el computador las dimensiones de acuerdo a las necesidades. 

Variables Una variable se define especificando el tipo y el nombre de dicha variable. Estas variables pueden ser tanto de tipos primitivos como referencias a objetos de alguna clase perteneciente al API de Java o generada por el programador. 

Variables Si no se especifica un valor en su declaración, las variable primitivas se inicializan a cero \(salvo boolean y char\). Análogamente las variables de tipo referencia son inicializadas por defecto a un valor especial: null. 

Variables Ejemplos

int x ; /\* D e c l a r a c i o n de la v a r i a b l e p r i m i t i v a x

. Se i n i c i a l i z a a 0 \*/

int y = 5; /\* D e c l a r a c i o n de la v a r i a b l e p r i m i t i v a y . Se i n i c i a l i z a a 5 \*/

int \[\] v e c t o r ; /\* D e c l a r a c i o n n de un a r r a y . Se i n i c i a l i z a a n u l l \*/

v e c t o r = new int \[ 1 0 \] ; /\*

V e c t o r de 10 enteros , i n i c i a l i z a d o s a 0 \*/

d o u b l e \[\] v = \{1.0 , 2.65 , 3 . 1 \} ; /\* D e c l a r a c i o n e i n i c i a l i z a c i o n de un v e c t o r de 3 e l e m e n t o s con los v a l o r e s e n t r e l l a v e s \*/

Variables Visibilidad

Se entiende por visibilidad, ámbito o scope de una variable, la parte de la aplicación donde dicha variable es accesible y por lo tanto puede ser utilizada en una expresión. 

Variables Visibilidad

En general las variables declaradas dentro de unas llaves \{\}, es decir dentro de un bloque, son visibles y existen dentro de estas llaves. 

Tipo de datos Todos los datos o variables tienen un tipo asociado con ellos. El tipo de dato determina la naturaleza del conjunto de valores que puede tomar una variable y las posibles operaciones que puede soportar. 



Tipo de datos

Tipo de datos Númericos

Permiten representar valores escalares de forma numérica, esto incluye a los números enteros y los reales. Este tipo de datos permiten realizar operaciones aritméticas comunes. 

Tipo de datos Númericos

Un dato de tipo entero es un número que no tiene punto decimal, por lo tanto en sus operaciones jamás va a generar decimales. 

Por ejemplo 25, -96 y 0. 

Tipo de datos Númericos

Un dato de tipo real es un número que tiene punto decimal, por lo tanto en sus operaciones puede generar decimales. Por ejemplo 12.3, -78.56 o 45.0. 

Tipo de datos Lógicos

Son aquellos que solo pueden tener dos valores \(cierto o falso\) ya que representan el resultado de una comparación entre otros datos \(numéricos o alfanuméricos\). 

Tipo de datos Cáracter

Un dato tipo carácter es un equivalente del Código ASCII\(American Standard Code for Interchange Information\). El código ASCII es el Código Internacional de equivalencias Internas en el Sistema Binario. 

Tipo de datos Cadena de caracteres

Es una secuencia de caracteres alfanuméricos que permiten representar valores identificables de forma descriptiva, esto incluye nombres de personas, direcciones, etc. 

Tipo de datos Cadena de caracteres

Es posible representar números como alfanuméricos, pero estos pierden su propiedad matemática, es decir no es posible hacer operaciones con ellos. Este tipo de datos se representan encerrados entre comillas. 

Tipo de datos Java

boolean true - false

byte

\[-128 .. 127\]

short

\[-32,768 .. 32,767\]

int

\[-231 .. 231-1\]

long

\[-263 .. 263-1\]

Tipo de datos Java

float

\[±3,4 ∗ 10−38 .. ±3,4 ∗ 1038\]

double

\[±1,7 ∗ 10−308 .. ±1,7 ∗ 10308\]

char

\[ú0000’.. úffff’\] o \[0 .. 65.535\]

String

Secuencia de carácteres

Constantes En programación, una constante es un valor que no puede ser alterado/modificado durante la ejecución de un programa, únicamente puede ser le´ıdo. 

Constantes Una constante corresponde a una longitud fija de un área reservada en la memoria principal del ordenador, donde el programa almacena valores fijos. 

Constantes Java

Una variable final tiene como caracter´ıstica el que su valor no puede ser modificado, o lo que es lo mismo, es una constante. Ejemplo: f i n a l d o u b l e PI = 3 . 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 ; 

Identificadores El identificador es una secuencia de caracteres que sirve para nombrar entidades del lenguaje. Algunas de las de entidades que un identificador puede denotar son las variables, las constantes, los tipos de datos, las constantes, los métodos y los paquetes. 

Identificadores Existen reglas para formar un identificador, y que no pueden ser violadas porque ocasionar´ıa errores en el proceso de compilación del programa: I La longitud puede ser hasta de 31

caracteres. 

Identificadores I Se hace distinción entre letras mayúsculas y minúsculas. As´ı, Masa es considerado como un identificador distinto de masa y de MASA. 

Identificadores I El primer carácter de un identificador debe ser siempre una letra o un \( \), es decir,no puede ser un d´ıgito. 

Identificadores I Los caracteres admitidos en un identificador son las letras minúsculas de la a a la z, las letras mayúsculas de la A a la Z, los d´ıgitos del 0 al 9 y el carácter subrayado o underscore\( \). 

Identificadores I Un identificador no puede contener espacios en blanco, ni otros caracteres distintos de los citados, como por ejemplo \(\#, $, %, \*, &, etc.\). 

Identificadores Existen palabras que tienen un significado predefinido en el lenguaje, son las llamadas palabras reservadas y no pueden ser utilizadas como identificadores. 

Identificadores Ejemplos: class, private, public, void, int, float, char, long, short, unsigned, signed, break, continues, if, else, for, while, do, const, return. 

Identificadores Los identificadores deben no solo ser válidos sino que deben autodocumentar el programa, es decir, tener nombres que permitan conocer a simple vista qué representan, utilizando para ello tantos caracteres como sean necesarios. 

Conclusiones I Para declarar una variable se necesita definir su tipo de dato e identificador. 

I En un programa puede existir varias variables del mismo tipo de dato, pero no con el mismo identificador \(exceptuando aquellas que tengan un ámbito de vida diferente\). 

Estudio independiente I Defina el tipo de dato y el identificador de las variables para almacenar los siguientes datos de una persona. 

I CI. 

I Nombre. 

I Edad. 

I Estatura. 

I Color de piel. 

UNIVERSIDAD

DE MATANZAS

cosechando el saber

**FIN**


# Document Outline

+ Objetivos 
+ Sumario 
+ Biliografía 
+ Variables 
+ Tipos de datos 
+ Constantes 
+ Identificadores 
+ Conclusiones 
+ Estudio Independiente



