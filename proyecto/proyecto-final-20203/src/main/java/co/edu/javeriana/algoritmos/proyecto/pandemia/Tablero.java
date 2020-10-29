package co.edu.javeriana.algoritmos.proyecto.pandemia;
import java.util.Random;
public class Tablero implements TableroI {
	
	
	private static int [][]tablero;
	private static int filas;
	private static int columnas;
	private static int dificultad;
	
	public Tablero(int filas, int columnas, int dificultad) {
		super();
		this.filas=filas;
		this.columnas= columnas;
		this.tablero= new int[filas][columnas];
		this.dificultad=dificultad+3;
		this.generarTablero();
	}
	
	private static void generarTablero() {
		
		for (int x=0; x < filas; x++) {
			for (int y=0; y < columnas; y++) {
				tablero[x][y] = (int) (Math.random()*dificultad+1);
			}
		}
		
	}
	public void imprimirTablero()throws IllegalArgumentException {
		System.out.println(this.dificultad);
		for (int x=0; x < filas; x++) {
			for (int y=0; y < columnas; y++) {
				System.out.print(this.tablero[x][y]+" ");
			}
			System.out.println();
		}
	}
	
	
	public void eliminarSubconjunto(int fila, int columna) throws IllegalArgumentException{
		System.out.print("");
	}
	
	public int [][] getTablero() throws IllegalArgumentException {
		return this.tablero;
		
	}

	@Override
	public int efectuarJugada(Casilla jugada) throws IllegalArgumentException {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int simularJugada(Casilla jugada) throws IllegalArgumentException {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int getNumeroColores() {
		// TODO Auto-generated method stub
		return this.dificultad;
	}

	@Override
	public int getFilas() {
		// TODO Auto-generated method stub
		return this.filas;
	}

	@Override
	public int getColumnas() {
		// TODO Auto-generated method stub
		return this.columnas;
	}

	@Override
	public int colorCasilla(int i, int j) {
		// TODO Auto-generated method stub
		return 0;
	}

	@Override
	public int[][] coloresTablero() {
		// TODO Auto-generated method stub
		return null;
	}

}
