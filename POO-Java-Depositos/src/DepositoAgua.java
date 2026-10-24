package src;

public class DepositoAgua {
    private String ubicacion;
    private double capacidadMaxima;
    private double nivelActual;

    public DepositoAgua(String ubicacion, double capacidadMaxima) {
        if (ubicacion == null || ubicacion.trim().isEmpty()) {
            throw new IllegalArgumentException("La ubicación no puede ser nula ni estar vacía.");
        }
        if (capacidadMaxima <= 0 || Double.isInfinite(capacidadMaxima) || Double.isNaN(capacidadMaxima)) {
            throw new IllegalArgumentException("La capacidad máxima debe ser positiva y finita.");
        }

        this.ubicacion = ubicacion;
        this.capacidadMaxima = capacidadMaxima;
        this.nivelActual = 0.0;
    }

    public boolean agregarAgua(double litros) {
        if (!esCantidadValida(litros)) {
            return false;
        }
        if (this.nivelActual + litros > this.capacidadMaxima) {
            return false;
        }

        this.nivelActual += litros;
        return true;
    }

    public boolean servirAgua(double litros) {
        if (!esCantidadValida(litros)) {
            return false;
        }
        if (this.nivelActual - litros < 0) {
            return false;
        }

        this.nivelActual -= litros;
        return true;
    }

    private boolean esCantidadValida(double litros) {
        return litros > 0 && !Double.isInfinite(litros) && !Double.isNaN(litros);
    }

    public String getUbicacion() {
        return this.ubicacion;
    }

    public double getCapacidadMaxima() {
        return this.capacidadMaxima;
    }

    public double getNivelActual() {
        return this.nivelActual;
    }

    public void mostrarEstado() {
        System.out.printf("Depósito: %s | Nivel: %.2f / %.2f litros%n",
                          this.ubicacion, this.nivelActual, this.capacidadMaxima);
    }
}
