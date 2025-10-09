package ejercicios.guia1;

public class ej_5 {
    public static void main(String[] args) {

    }
}


class TarjetaBaja {
    private double saldo;
    private int cantViajesSubte;
    private int cantViajesColectivo;

    public TarjetaBaja ( double saldoInicial ) {
        this.saldo = saldoInicial;
    }

    public double obtenerSaldo () {
        return this.saldo;
    }
    public void cargar ( double monto ) {
        this.saldo += monto;
    }
    /* Las secciones son 1, 2 o 3, y los valores correspondientes son
     * $408.24, $454.78 y $489.82
     */
    public void pagarViajeEnColectivo (int seccion) {
        double precio = 0.0;

        if (seccion == 1) {
            precio = 408.24;
        } else if (seccion == 2) {
            precio = 454.78;
        } else if (seccion == 3) {
            precio = 489.82;
        }
        this.saldo -= precio;
        this.cantViajesColectivo += 1;
    }
    /* El subte cuesta $832.
     */
    public void pagarViajeEnSubte () {
        this.saldo -= 832.0;
        this.cantViajesSubte += 1;
    }
    public int viajesRealizadosSubte () {
        return cantViajesSubte;
    }
    public int viajesRealizadosColectivo () {
        return cantViajesColectivo;
    }
}

