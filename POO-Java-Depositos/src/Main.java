package src;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        DepositoAgua laboratorio = new DepositoAgua("Laboratorio", 10.0);
        DepositoAgua taller = new DepositoAgua("Taller", 6.0);

        Scanner scanner = new Scanner(System.in);
        int operacionesCompletadas = 0;

        System.out.println("=== SISTEMA DE GESTIÓN DE DEPÓSITOS DE AGUA ===");

        while (operacionesCompletadas < 4) {
            System.out.println("\nOperación " + (operacionesCompletadas + 1) + " de 4");
            System.out.println("Seleccione el depósito:");
            System.out.println("1. Laboratorio (Capacidad: 10L)");
            System.out.println("2. Taller (Capacidad: 6L)");
            System.out.print("Opción: ");

            String opDep = scanner.nextLine();
            DepositoAgua depositoSeleccionado = null;

            if (opDep.equals("1")) {
                depositoSeleccionado = laboratorio;
            } else if (opDep.equals("2")) {
                depositoSeleccionado = taller;
            } else {
                System.out.println("Error: Opción de depósito inválida. Intente de nuevo.");
                continue;
            }

            System.out.println("Seleccione la acción:");
            System.out.println("1. Agregar agua");
            System.out.println("2. Servir agua");
            System.out.print("Opción: ");

            String opAccion = scanner.nextLine();
            int accion = 0;

            if (opAccion.equals("1")) {
                accion = 1;
            } else if (opAccion.equals("2")) {
                accion = 2;
            } else {
                System.out.println("Error: Acción inválida. Intente de nuevo.");
                continue;
            }

            System.out.print("Ingrese la cantidad de litros: ");
            String cantStr = scanner.nextLine();
            double cantidad = 0.0;

            try {
                cantidad = Double.parseDouble(cantStr);
            } catch (NumberFormatException e) {
                System.out.println("Error: Debe ingresar un número válido (ej: 5.5).");
                continue;
            }

            if (cantidad <= 0 || Double.isInfinite(cantidad) || Double.isNaN(cantidad)) {
                 System.out.println("Error: La cantidad debe ser un número positivo, mayor a cero y finito.");
                 continue;
            }

            boolean exito = false;
            if (accion == 1) {
                exito = depositoSeleccionado.agregarAgua(cantidad);
                if (exito) {
                    System.out.println("Resultado: true. Se han agregado " + cantidad + " litros al depósito de " + depositoSeleccionado.getUbicacion() + ".");
                } else {
                    System.out.println("Resultado: false. No se puede agregar agua. Se superaría la capacidad máxima.");
                }
            } else {
                exito = depositoSeleccionado.servirAgua(cantidad);
                if (exito) {
                    System.out.println("Resultado: true. Se han servido " + cantidad + " litros del depósito de " + depositoSeleccionado.getUbicacion() + ".");
                } else {
                    System.out.println("Resultado: false. No hay suficiente agua disponible.");
                }
            }

            operacionesCompletadas++;
        }

        System.out.println("\n=== ESTADO FINAL DE LOS DEPÓSITOS ===");
        laboratorio.mostrarEstado();
        taller.mostrarEstado();

        scanner.close();
    }
}
