Instrucciones generales para el assembler:
1.-Correr el archivo Assembler.py con Python 3
2.-Escribir el nombre de el archivo a compilar sin el .ass 
    (utiliza el file opener de python por tanto el archivo debe estar en el mismo directorio, o con la direccion relativa)
3.-Ambos archivos de salida se generan en el directorio actual, o el especificado.

Notas para el código assembly:
-Cada funcion debe estar identada al menos una vez, pero las etiquetas no deben estar identadas ninguna vez.
-Las identaciones deben ser por espacios y no con el tabulado "\t" que poseen algunos programas (esto puede causar errores)
-No acepta dos atiquetas seguidas sin ninguna funcion entre ellas.
-No acepta como nombres de variables argumentos especiales (A,B,nada con parentesis).
-Todas las variables necesitan un valor inicial.
-Requiere la linea CODE para procesar las instrucciones por mucho que no haya DATA.
-No acepta lineas vacias, todas las líneas deben tener como mínimo, una variable, una etiqueta, una función o DATA,CODE.  

Opcodes de funciones nuevas:
-CALL (Dir): 1011100
-RET: 1011101
-PUSH A: 1011110
-PUSH B: 1011111
-POP A: 1100000
-POP B: 1100001