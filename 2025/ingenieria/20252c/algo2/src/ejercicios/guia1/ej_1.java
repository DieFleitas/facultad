package ejercicios.guia1;

public class ej_1 {
    public static void main(String[] args) {

    }
}


class Nota_1 {
    private final int valor;

    Nota_1(int valor){
        this.valor = valor;
    }

    int obtenerValor() {
        return this.valor;
    }

    boolean aprobado() {
        return this.obtenerValor() >= 4;
    }

    boolean desaprobado() {
        return this.obtenerValor() < 4;
    }
}