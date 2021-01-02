cython3 --embed src/excel2json.pyx
gcc -Os -I /usr/include/python3.9 src/excel2json.c -lpython3.9 -o excel2json.run