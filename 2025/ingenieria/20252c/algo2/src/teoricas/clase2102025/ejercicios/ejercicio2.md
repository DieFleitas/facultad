Ejercicio 2 — diseño teórico para app de productividad (almacenar tareas añadidas durante el día, se recorren de principio a fin, solo es necesario una dirección)

Requerimientos clave:

Se agregan tareas durante el día (operación add frecuente).

Se recorren de principio a fin (solo lectura en una dirección).

No se requiere navegar hacia atrás.

Estructura recomendada: lista simplemente enlazada (Singly Linked List) o una cola (Queue) si las tareas se consumen en orden FIFO.

Justificación:

La lista simplemente enlazada es suficiente y más eficiente en memoria que una doblemente enlazada porque no necesita prev.

Si el modelo operativo es "agregar tareas y luego procesarlas/desplegarlas en orden y posiblemente eliminar a medida que se procesan", entonces una Queue (implementada por ejemplo con una lista enlazada con head y tail) es la abstracción correcta: enqueue para añadir y dequeue para consumir.

Si solo las quieres mantener y recorrer sin eliminarlas, una lista simplemente enlazada con referencias a head y tail permite addLast en O(1) y recorrido en O(n).

Complejidad esperada:

addLast: O(1) si tienes puntero tail.

Recorrido completo: O(n).

Búsqueda aleatoria por índice: O(n).