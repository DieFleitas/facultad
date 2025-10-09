package teoricas.clase2102025.ejercicios;

// Carousel.java
public class Carousel<T> {
    private static class Node<T> {
        T data;
        Node<T> next;
        Node<T> prev;
        Node(T d) { data = d; }
    }

    private Node<T> current;
    private int size;

    public Carousel() { current = null; size = 0; }

    public void add(T item) {
        Node<T> n = new Node<>(item);
        if (current == null) {
            current = n;
            n.next = n.prev = n; // apuntan a sí mismos: circular
        } else {
            Node<T> tail = current.prev;
            tail.next = n;
            n.prev = tail;
            n.next = current;
            current.prev = n;
        }
        size++;
    }

    public T current() {
        if (current == null) throw new IllegalStateException("Carousel vacío");
        return current.data;
    }

    public T next() {
        if (current == null) throw new IllegalStateException("Carousel vacío");
        current = current.next; // avanza; si estaba en tail pasa a head
        return current.data;
    }

    public T prev() {
        if (current == null) throw new IllegalStateException("Carousel vacío");
        current = current.prev;
        return current.data;
    }

    public int size() { return size; }
}

