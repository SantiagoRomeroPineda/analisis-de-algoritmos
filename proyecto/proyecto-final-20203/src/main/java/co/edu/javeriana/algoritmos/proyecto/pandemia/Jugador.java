package co.edu.javeriana.algoritmos.proyecto.pandemia;

import java.util.List;

public class Jugador implements JugadorI {

	
	
	public Jugador() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 *

	 */
	@Override
	public List<Casilla> jugar(TableroI tablero){
		return null;
	}
//	public List<Casilla> jugar(TableroI tablero) {
//		// TODO Auto-generated method stub
//		//inicializar un mapa de enteros con la cantidad de colores que tenga el tablero
//		//la llave del mapa será el id del color
//		//Los valores del mapa serán las coordenadas X  y Y
//		//es valido aclarar que el mapa representa las prioridades para la eleccion de las jugadas
//		Boolean seguirJugando=true;
//		while(seguirJugando){
//			Boolean realizaJugada=false;
//			for(int i =0;i<tablero.getFilas();++i){
//				for (int j=tablero.getColumnas()-1; j>=0;--j){
//					int color=tablero.colorCasilla(i, j);
//					//si el color no ha sido registtrado en el mapa, se debe registrar
//					//si el color en esa posicion es prioridad 
//						//si tiene vecinos vecinos, 
//						//invocar tablero para realizar jugada
//							//se agregar a la lista de jugadas
//							//realizaJugada=true
//					//registrar la posicion de la primera jugada que puede realizar respecto al color
//					
//				}
//			}
//			
//			for(Map llave: mapa){
//				//la primera jugada que encuentre y si jugada = false
//					//agregar jugada a la lista
//					//realizaJugada= true
//				//reiniciamos los valores a nulo, para despues poder volver a darles un valor
//			}
//			//si no realiza una jugada retorno la lista de jugadas
//		}
//		return null;
//	}

	@Override
	public String identificacionJugador() {
		// TODO Auto-generated method stub
		return null;
	}

}
