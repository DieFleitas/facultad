package ejercicios.guia1;

public class ej_4 {
    public static void main(String[] args) {

    }
}


class Rectangulo {
    private int base;
    private int altura;

    public Rectangulo(int base, int altura) {
        this.base = base;
        this.altura = altura;
    }

    public int getBase() {
        return base;
    }

    public void setBase(int base) {
        this.base = base;
    }

    public int getAltura() {
        return altura;
    }

    public void setAltura(int altura) {
        this.altura = altura;
    }

    public int perimetro() {
        return (2*this.getBase()) + (2*this.getAltura());
    }

    public int area() {
        return this.getBase() * this.getAltura();
    }
}
