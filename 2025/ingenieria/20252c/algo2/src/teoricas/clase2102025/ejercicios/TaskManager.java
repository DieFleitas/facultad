package teoricas.clase2102025.ejercicios;

// TaskManager.java (lista simplemente enlazada con head/tail)
public class TaskManager {
    private static class Node {
        Task task;
        Node next;
        Node(Task t) { task = t; }
    }

    private Node head;
    private Node tail;
    private int size;

    public TaskManager() { head = tail = null; size = 0; }

    // Agrega al final en O(1)
    public void addTask(Task t) {
        Node n = new Node(t);
        if (head == null) {
            head = tail = n;
        } else {
            tail.next = n;
            tail = n;
        }
        size++;
    }

    // Recorre de principio a fin
    public void listarTareas() {
        Node cur = head;
        while (cur != null) {
            System.out.println(cur.task);
            cur = cur.next;
        }
    }

    public int size() { return size; }
}

