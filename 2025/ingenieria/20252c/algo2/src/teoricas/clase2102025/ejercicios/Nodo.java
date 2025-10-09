package teoricas.clase2102025.ejercicios;

// Nodo.java (ejemplo, por si querés compilar)
public class Nodo<T> {
    private T dato;
    private Nodo<T> next;
    private Nodo<T> prev;

    public Nodo(T dato) {
        this.dato = dato;
    }

    public T getDato() { return dato; }
    public Nodo<T> getNext() { return next; }
    public Nodo<T> getPrev() { return prev; }

    public void setNext(Nodo<T> n) { this.next = n; }
    public void setPrev(Nodo<T> p) { this.prev = p; }
}
