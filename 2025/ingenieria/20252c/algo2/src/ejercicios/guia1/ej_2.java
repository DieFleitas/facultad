package ejercicios.guia1;

public class ej_2 {
    public static void main(String[] args) {

    }
}


class Nota_2 {
    private int valor;

    Nota_2(int valor){
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

    void recuperar(int nuevoValor) {
        if(nuevoValor > this.valor) {
            this.valor = nuevoValor;
        }

    }
}
