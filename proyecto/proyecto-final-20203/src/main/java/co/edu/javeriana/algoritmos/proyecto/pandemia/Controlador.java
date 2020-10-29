	package co.edu.javeriana.algoritmos.proyecto.pandemia;

public class Controlador {
	
	static TableroI tablero;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		tablero = new Tablero(10,10,1);
		tablero.getTablero();
		tablero.imprimirTablero();
	}

}
