package teoricas.clase2102025.ejercicios;

// HistoryExample.java
public class HistoryExample {

    // Pila simple genérica basada en lista enlazada
    public static class Stack<T> {
        private static class Node<E> {
            E value;
            Node<E> next;
            Node(E v, Node<E> n) { value = v; next = n; }
        }

        private Node<T> top;
        private int size;

        public Stack() {
            top = null;
            size = 0;
        }

        public void push(T item) {
            top = new Node<>(item, top);
            size++;
        }

        public T pop() {
            if (isEmpty()) throw new IllegalStateException("Stack vacío");
            T val = top.value;
            top = top.next;
            size--;
            return val;
        }

        public T peek() {
            if (isEmpty()) throw new IllegalStateException("Stack vacío");
            return top.value;
        }

        public boolean isEmpty() { return top == null; }

        public int size() { return size; }

        public void clear() {
            top = null;
            size = 0;
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder("[");
            Node<T> cur = top;
            while (cur != null) {
                sb.append(cur.value);
                if (cur.next != null) sb.append(", ");
                cur = cur.next;
            }
            sb.append("]");
            return sb.toString();
        }
    }

    // Clase History usando SimpleStack
    public static class History<T> {
        private final Stack<T> backStack;
        private final Stack<T> forwardStack;
        private T current;

        public History() {
            backStack = new Stack<>();
            forwardStack = new Stack<>();
            current = null;
        }

        // Visitar nueva "página"
        public void visit(T page) {
            if (current != null) {
                backStack.push(current);
            }
            current = page;
            forwardStack.clear(); // al visitar una nueva página se elimina el "adelante"
        }

        // Volver atrás; devuelve el nuevo current
        public T back() {
            if (backStack.isEmpty()) {
                throw new IllegalStateException("No hay historial atrás");
            }
            forwardStack.push(current);
            current = backStack.pop();
            return current;
        }

        // Ir adelante; devuelve el nuevo current
        public T forward() {
            if (forwardStack.isEmpty()) {
                throw new IllegalStateException("No hay historial adelante");
            }
            backStack.push(current);
            current = forwardStack.pop();
            return current;
        }

        public T current() { return current; }

        // Métodos auxiliares para depuración / UI
        public String debugStacks() {
            return "back=" + backStack.toString() + " current=" + current + " forward=" + forwardStack.toString();
        }
    }

    // Prueba simple en main
    public static void main(String[] args) {
        History<String> h = new History<>();

        h.visit("Home");
        h.visit("Película A");
        h.visit("Película B");
        h.visit("Película C"); // actual = C
        System.out.println("Después de visitas: " + h.debugStacks());

        h.back(); // vuelve a B
        System.out.println("Back 1 -> current: " + h.current() + " | " + h.debugStacks());

        h.back(); // vuelve a A
        System.out.println("Back 2 -> current: " + h.current() + " | " + h.debugStacks());

        h.forward(); // vuelve a B
        System.out.println("Forward 1 -> current: " + h.current() + " | " + h.debugStacks());

        // Visitar nueva página después de haber hecho back: debe limpiar forward
        h.visit("Película D");
        System.out.println("Visit D -> current: " + h.current() + " | " + h.debugStacks());

        // Intentar forward ahora debe fallar
        try {
            h.forward();
        } catch (IllegalStateException e) {
            System.out.println("forward() falló como se esperaba: " + e.getMessage());
        }
    }
}

