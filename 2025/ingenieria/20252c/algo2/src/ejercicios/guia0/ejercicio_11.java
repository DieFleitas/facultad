package ejercicios.guia0;

import java.util.Scanner;

public class ejercicio_11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingrese un número: ");
        int a = sc.nextInt();

        System.out.println("Ingrese otro número");
        int b = sc.nextInt();

        System.out.println("La suma es: "+ (a+b));
        System.out.println("El producto es: "+ (a*b));
        System.out.println("La resta es: "+ (a-b));
        System.out.println("La division es: "+ (a/b));

    }
}
