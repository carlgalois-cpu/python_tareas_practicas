package pruebas;

import src.DepositoAgua;

public class TestDepositoAgua {

    public static void main(String[] args) {
        testCreacionDeposito();
        testAgregarCantidadValida();
        testAgregarSuperandoCapacidad();
        testAgregarCeroONegativo();
        testAgregarNaNONulo();
        testExtraerCantidadValida();
        testExtraerMasDeLoDisponible();
        testExtraerCeroONegativo();
        testOperacionRechazadaConservaNivel();
        testLimitesNivel();
        testIndependenciaDepositos();

        System.out.println("¡Todas las pruebas pasaron exitosamente!");
    }

    private static void testCreacionDeposito() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        assert d.getNivelActual() == 0.0 : "El nivel inicial no es 0";
    }

    private static void testAgregarCantidadValida() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        assert d.agregarAgua(5.0) == true : "Falló al agregar cantidad válida";
        assert d.getNivelActual() == 5.0 : "El nivel no se actualizó correctamente al agregar";
    }

    private static void testAgregarSuperandoCapacidad() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        assert d.agregarAgua(11.0) == false : "Permitió agregar más de la capacidad";
        assert d.getNivelActual() == 0.0 : "El nivel cambió al rechazar la operación";
    }

    private static void testAgregarCeroONegativo() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        assert d.agregarAgua(0.0) == false : "Permitió agregar 0";
        assert d.agregarAgua(-5.0) == false : "Permitió agregar negativo";
    }

    private static void testAgregarNaNONulo() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        assert d.agregarAgua(Double.NaN) == false : "Permitió agregar NaN";
        assert d.agregarAgua(Double.POSITIVE_INFINITY) == false : "Permitió agregar infinito";
    }

    private static void testExtraerCantidadValida() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        d.agregarAgua(8.0);
        assert d.servirAgua(5.0) == true : "Falló al servir cantidad válida";
        assert d.getNivelActual() == 3.0 : "El nivel no se redujo correctamente";
    }

    private static void testExtraerMasDeLoDisponible() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        d.agregarAgua(5.0);
        assert d.servirAgua(6.0) == false : "Permitió servir más agua de la disponible";
        assert d.getNivelActual() == 5.0 : "El nivel cambió al rechazar la extracción";
    }

    private static void testExtraerCeroONegativo() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        d.agregarAgua(5.0);
        assert d.servirAgua(0.0) == false : "Permitió extraer 0";
        assert d.servirAgua(-2.0) == false : "Permitió extraer negativo";
    }

    private static void testOperacionRechazadaConservaNivel() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        d.agregarAgua(5.0);
        d.agregarAgua(20.0); // Debería ser rechazada
        assert d.getNivelActual() == 5.0 : "El nivel no se conservó tras una operación rechazada";
    }

    private static void testLimitesNivel() {
        DepositoAgua d = new DepositoAgua("Test", 10.0);
        d.agregarAgua(10.0);
        assert d.getNivelActual() <= d.getCapacidadMaxima() : "Nivel superó la capacidad máxima";
        d.servirAgua(10.0);
        assert d.getNivelActual() >= 0 : "Nivel quedó por debajo de cero";
    }

    private static void testIndependenciaDepositos() {
        DepositoAgua d1 = new DepositoAgua("Lab", 10.0);
        DepositoAgua d2 = new DepositoAgua("Taller", 6.0);
        d1.agregarAgua(5.0);
        assert d1.getNivelActual() == 5.0 : "Estado de D1 incorrecto";
        assert d2.getNivelActual() == 0.0 : "D2 se vio afectado por D1";
    }
}
