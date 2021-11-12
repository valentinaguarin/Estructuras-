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
                if (origen.equals("1") || origen.equals("2") || origen.equals("3")) {
                    //Debemos colocar la condicion 1-2 o 3
                    System.out.println("Ingrese destino");
                    destino = leer.next();
                    if (origen.equals("1") && destino.equals("1") || origen.equals("1") && destino.equals("2")
                            || origen.equals("1") && destino.equals("3") || origen.equals("2") && destino.equals("2")
                            || origen.equals("3") && destino.equals("3") || origen.equals("3") && destino.equals("1")){
                        registro = vehiculo + origen + destino;
                        vehiculos.add(registro);
                    }
                }
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