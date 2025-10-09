package teoricas.clase2102025.ejercicios;

// Task.java
public class Task {
    private String descripcion;
    public Task(String descripcion) { this.descripcion = descripcion; }
    public String getDescripcion() { return descripcion; }
    @Override public String toString() { return descripcion; }
}

