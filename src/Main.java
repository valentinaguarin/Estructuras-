import java.util.ArrayList;
import java.util.Scanner;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Cuando finalice de ingresar los datos,ingrese cero o cualquier valor diferente para terminar el programa");
        ArrayList<String> vehiculos = new ArrayList<String>();
        String vehiculo, origen, destino, registro;

        do{
            System.out.println("Ingrese el tipo de vehiculo, escriba A para automovil,C para camión  M para motocicleta ");
            vehiculo = leer.next();
            vehiculo=vehiculo.toUpperCase();
            if(vehiculo.equals("C") || vehiculo.equals("A")  || vehiculo.equals("M")) {
                //Debemos colocar la condicion 1-2 o 3
                System.out.println("Ingrese origen");
                origen = leer.next();
                //Debemos colocar la condicion 1-2 o 3
                System.out.println("Ingrese destino");
                destino = leer.next();
                registro = vehiculo + origen + destino;
                //System.out.println(miarray[0]);

                vehiculos.add(registro);
            }
        }while (vehiculo.equals("C") || vehiculo.equals("A")  || vehiculo.equals("M"));
        System.out.println("La cantidad de Vehiculos son" + vehiculos.size());
        System.out.println("Los registros son");
        System.out.println(vehiculos);
        String[] miarray = new String[vehiculos.size()];
        miarray = vehiculos.toArray(miarray);
        //visualizacion de datos
        for(int j=0;j<miarray.length;j++) {
            System.out.println("Dato:"+ miarray[j]+" Correspondiente al indice: "+j);}
    }
}