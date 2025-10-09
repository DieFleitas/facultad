package ejercicios.guia1;

public class ej_6 {
    public static void main(String[] args) {

    }
}


/**
 * Clase Ticket: acumula items (cantidad × precio unitario), permite aplicar
 * un único descuento y cerrar el ticket obteniendo el total.
 *
 * Comportamiento:
 * - El ticket se inicia con importe 0 y abierto.
 * - agregarItem suma cantidad*precioUnitario al importe si el ticket está abierto.
 * - aplicarDescuento aplica un único descuento sobre el importe acumulado al momento
 *   de la llamada. No puede aplicarse más de una vez y no se puede si el ticket está cerrado.
 * - calcularSubtotal devuelve el importe vigente (si ya se aplicó descuento, devuelve el importe ya reducido).
 * - calcularTotal cierra el ticket (abierto -> cerrado) y devuelve el importe final.
 * - contarProductos devuelve la suma de las cantidades agregadas.
 */
class Ticket {

    private double importe;            // importe acumulado (puede incluir descuento después de aplicarlo)
    private int cantidadTotal;         // cantidad total de productos
    private boolean abierto;           // true si el ticket está abierto
    private boolean descuentoAplicado; // true si ya se aplicó descuento

    /**
     * post: el Ticket se inicializa con importe 0.
     */
    public Ticket() {
        this.importe = 0.0;
        this.cantidadTotal = 0;
        this.abierto = true;
        this.descuentoAplicado = false;
    }

    /**
     * pre : cantidad y precio son mayores a cero . El ticket está abierto .
     * post : suma al Ticket un item a partir de la cantidad de productos y su precio unitario .
     *
     * @param cantidad número de unidades (>0)
     * @param precioUnitario precio unitario (>0)
     * @throws IllegalArgumentException si cantidad <= 0 o precioUnitario <= 0
     * @throws IllegalStateException si el ticket está cerrado
     */
    public void agregarItem(int cantidad, double precioUnitario) {
        if (!abierto) {
            throw new IllegalStateException("No se puede agregar items: el ticket está cerrado.");
        }
        if (cantidad <= 0) {
            throw new IllegalArgumentException("La cantidad debe ser mayor a cero.");
        }
        if (precioUnitario <= 0.0) {
            throw new IllegalArgumentException("El precio unitario debe ser mayor a cero.");
        }
        this.importe += cantidad * precioUnitario;
        this.cantidadTotal += cantidad;
    }

    /**
     * pre : el Ticket está abierto y no se ha aplicado un descuento previamente .
     * post : aplica un descuento sobre el total del importe .
     *
     * Nota: el descuento se aplica sobre el importe acumulado en el momento de la llamada.
     * Items agregados después de aplicar el descuento NO quedan afectados por ese descuento.
     *
     * @param porcentaje porcentaje de descuento en [0,100]
     * @throws IllegalStateException si el ticket está cerrado o ya se aplicó un descuento
     * @throws IllegalArgumentException si el porcentaje está fuera del rango [0,100]
     */
    public void aplicarDescuento(double porcentaje) {
        if (!abierto) {
            throw new IllegalStateException("No se puede aplicar descuento: el ticket está cerrado.");
        }
        if (descuentoAplicado) {
            throw new IllegalStateException("El descuento ya fue aplicado previamente.");
        }
        if (porcentaje < 0.0 || porcentaje > 100.0) {
            throw new IllegalArgumentException("Porcentaje de descuento inválido. Debe estar entre 0 y 100.");
        }
        // Aplica descuento sobre el importe actual
        double factor = 1.0 - (porcentaje / 100.0);
        this.importe = this.importe * factor;
        this.descuentoAplicado = true;
    }

    /**
     * post : devuelve el importe acumulado hasta el momento sin cerrar el Ticket .
     *
     * @return importe vigente (si ya se aplicó descuento devuelve el importe reducido)
     */
    public double calcularSubtotal() {
        return this.importe;
    }

    /**
     * post : cierra el Ticket y devuelve el importe total .
     *
     * @return importe final
     */
    public double calcularTotal() {
        // cerrar el ticket (idempotente)
        this.abierto = false;
        return this.importe;
    }

    /**
     * post : devuelve la cantidad total de productos .
     *
     * @return cantidad total agregada
     */
    public int contarProductos() {
        return this.cantidadTotal;
    }

    // métodos auxiliares de consulta de estado (opcionales)
    /**
     * Indica si el ticket está abierto.
     * @return true si está abierto
     */
    public boolean estaAbierto() {
        return this.abierto;
    }

    /**
     * Indica si ya se aplicó un descuento.
     * @return true si ya se aplicó descuento
     */
    public boolean isDescuentoAplicado() {
        return this.descuentoAplicado;
    }
}
