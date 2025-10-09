package ejercicios.guia1;

public class ej_3 {
    public static void main(String[] args) {

    }
}


class Punto() {
    double x;
    double y;

    public Punto(){

    }

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double obtenerX() {
        return this.x;
    }

    public double obtenerY() {
        return this.y;
    }

    public void cambiarX(double valor) {
        this.x = valor;
    }

    public void cambiarY(double valor) {
        this.y = valor;
    }

    public boolean esOrigen() {
        return (this.x == 0.0) && (this.y == 0.0);
    }

    public boolean estaEnEjeX() {
        return this.y == 0.0;
    }

    public boolean estaEnEjeY() {
        return this.x == 0.0;
    }

    public double distanciaAlOrigen() {
        return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2));
    }

}
