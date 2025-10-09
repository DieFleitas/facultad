package teoricas.clase2102025.ejercicios;

// ListaDE.java
public class ListaDE<T> {
    private Nodo<T> head;
    private Nodo<T> tail;
    private int size;

    public ListaDE() {
        head = null;
        tail = null;
        size = 0;
    }

    public int size() { return size; }
    public boolean isEmpty() { return size == 0; }

    // Método pedido: alta
    public void alta(T dato, int posicion) {
        if (posicion < 1 || posicion > size + 1) {
            throw new IndexOutOfBoundsException("Posición inválida: " + posicion);
        }

        Nodo<T> nuevo = new Nodo<>(dato);

        if (isEmpty()) {
            // Solo permitido posicion == 1
            head = tail = nuevo;
            size = 1;
            return;
        }

        if (posicion == 1) {
            // Insertar al inicio
            nuevo.setNext(head);
            head.setPrev(nuevo);
            head = nuevo;
            size++;
            return;
        }

        if (posicion == size + 1) {
            // Insertar al final
            tail.setNext(nuevo);
            nuevo.setPrev(tail);
            tail = nuevo;
            size++;
            return;
        }

        // Insertar en medio: elegir recorrido desde head o tail según distancia
        Nodo<T> actual;
        int medio = size / 2;
        if (posicion - 1 <= medio) {
            // recorrer desde head hasta el nodo anterior a la posición
            actual = head;
            for (int i = 1; i < posicion - 1; i++) {
                actual = actual.getNext();
            }
            // actual = nodo en (posicion-1)
            Nodo<T> siguiente = actual.getNext();
            actual.setNext(nuevo);
            nuevo.setPrev(actual);
            nuevo.setNext(siguiente);
            siguiente.setPrev(nuevo);
        } else {
            // recorrer desde tail hacia atrás hasta el nodo en posicion (porque estamos cerca del final)
            actual = tail;
            for (int i = size; i > posicion - 1; i--) {
                actual = actual.getPrev();
            }
            // actual = nodo en (posicion-1)
            Nodo<T> siguiente = actual.getNext();
            actual.setNext(nuevo);
            nuevo.setPrev(actual);
            nuevo.setNext(siguiente);
            siguiente.setPrev(nuevo);
        }

        size++;
    }

    // Métodos auxiliares (para pruebas)
    public String toString() {
        StringBuilder sb = new StringBuilder("[");
        Nodo<T> cur = head;
        while (cur != null) {
            sb.append(cur.getDato());
            if (cur.getNext() != null) sb.append(", ");
            cur = cur.getNext();
        }
        sb.append("]");
        return sb.toString();
    }
}

