import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;

public class main2 {
    public static void main(String[] args) {
        System.out.println("Cuando finalice de ingresar los datos, digite cualquier valor diferente para terminar el programa");
        ArrayList<String> registroDatosTotales = new ArrayList<String>();
        String vehiculo, registro, bus;
        int i, br, origen, destino, indice, conteoCamionRecto = 0, conteoAutoRecto = 0, conteoMotoRecto = 0, conteoCamionGiro = 0, conteoAutoGiro = 0, conteoMotoGiro = 0;
        Scanner leer = new Scanner(System.in);
        do {
            System.out.println("Ingrese el tipo de vehiculo, escriba A para automovil, C para camión, M para motocicleta. S para salir.");
            vehiculo = leer.next();
            vehiculo = vehiculo.toUpperCase();
            System.out.println("Ingrese origen de Via 1,2 o 3");
            origen = leer.nextInt();
            System.out.println("Ingrese destino de Via 1,2 o 3");
            destino = leer.nextInt();
            if (esRutaCorrecta(origen, destino))  {
                switch (vehiculo) {
                    case "C" :
                        if (origen == destino) {
                            conteoCamionRecto++;
                        } else {
                            conteoCamionGiro++;
                        }
                        registro = vehiculo + Integer.toString(origen) + Integer.toString(destino);
                        registroDatosTotales.add(registro);
                        break;
                    case "A":
                        if (origen == destino) {
                            conteoAutoRecto++;
                        } else {
                            conteoAutoGiro++;
                        }
                        registro = vehiculo + Integer.toString(origen) + Integer.toString(destino);
                        registroDatosTotales.add(registro);
                        break;
                    case "M":
                        if (origen == destino) {
                            conteoMotoRecto++;
                        } else {
                            conteoMotoGiro++;
                        }
                        registro = vehiculo + Integer.toString(origen) + Integer.toString(destino);
                        registroDatosTotales.add(registro);
                        break;
                    default:
                        break;
                }

            } else {
                System.out.println("Desde la via " + origen + " no se pueden hacer giros hacia la via " + destino + ". Por favor revise los datos.");
            }
        } while (vehiculo.equals("C") || vehiculo.equals("A")  || vehiculo.equals("M"));


        System.out.println("Los registros son: " + registroDatosTotales);
        System.out.println("La cantidad de Vehiculos son: " + registroDatosTotales.size());
        System.out.println("Total de Camiones que siguieron recto: " + conteoCamionRecto);
        System.out.println("Total de Camiones que giraron: " + conteoCamionGiro);
        System.out.println("Total de Autos que siguieron recto: " + conteoAutoRecto);
        System.out.println("Total de Autos que giraron: " + conteoAutoGiro);
        System.out.println("Total de Motos que siguieron recto: "+conteoMotoRecto);
        System.out.println("Total de Motos que giraron: " + conteoMotoGiro);
        System.out.println("El numero de registros total es: " + registroDatosTotales.size());
        //System.out.println("Los registros son: " + registroDatosTotales);
        do{
            System.out.println("desea buscar un elemento por su indice? 1: sí");
            bus = leer.next();
            System.out.println("Ingrese el indice del elemento a buscar");
            indice = leer.nextInt();
            System.out.println("el elemento de ese indice es: "+registroDatosTotales.get(indice));
        }while (bus.equals("1"));

        System.out.println("Ingrese el indice del elemento a buscar");
        indice = leer.nextInt();
        System.out.println("el elemento de ese indice es: "+registroDatosTotales.get(indice));
        System.out.println("presione 1 si desea borrarlo o otro número en caso contrario");
       br = leer.nextInt();
        if (br == 1){
            registroDatosTotales.remove(indice);
            System.out.println("ha borrado el elemento ");
        }



        for(int j = 0; j < registroDatosTotales.size(); j++) {
            System.out.println("Dato: " + registroDatosTotales.get(j) + " Correspondiente al indice: " + j);
        }
        System.out.println("Los registros son: " + registroDatosTotales);

    }
    static boolean esRutaCorrecta(int origen, int destino) {
        switch (origen) {
            case 1:
                return true;
            case 2:
                return (destino == 2);
            case 3:
                return (destino == 3 || destino == 1);
            default:
                return false;
        }
    }
}

