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
		System.out.println();
		for (int x=0; x < filas; x++) {
			for (int y=0; y < columnas; y++) {
				if (this.tablero[x][y]==0) {
					System.out.print("-  ");
				}
				else {
					System.out.print(this.tablero[x][y]+"  ");
				}
				
			}
			System.out.println();
		}
	}
	
	

	
	public int [][] getTablero() throws IllegalArgumentException {
		return this.tablero;
		
	}
	
	
	@Override
	public void eliminarCasillas(int y, int x, int color) throws IllegalArgumentException {
		// TODO Auto-generated method stub
		int [] moverX= {-1,0,0,1}; 
		int [] moverY= {0,1,-1,0};
		this.tablero[y][x]=0;
		for(int i =0;i<4;i++) {
			boolean a=(x+moverX[i])!=getColumnas();
			boolean b=(x+moverX[i])!=-1;
			boolean c=(y+moverY[i])!=getFilas();
			boolean d=(y+moverY[i])!=-1;
			if(a && b && c && d) {
				int ySig=y+moverY[i];
				int xSig=x+moverX[i];
				if(this.tablero[ySig][xSig]==color) {
					this.eliminarCasillas(ySig, xSig,color);
				}
			}
		}
	}

	@Override
	public boolean bajarCasillas() throws IllegalArgumentException {
		// TODO Auto-generated method stub
		boolean columnaVacia=false;
		
		
		for (int j = 0; j < this.getColumnas(); j++){
			int descuento=0;
			boolean ya= false;
			for(int i=this.getFilas()-1;i>=0;i--) {
				this.tablero[i+descuento][j]=this.tablero[i][j];
				if(ya==false) {
					if(this.tablero[i][j]==0) {
						descuento++;
						if(i-1>=0 && this.tablero[i-1][j]!=0 ) {
							ya=true;
						}
					}
				} 
				
				
				if(i<= descuento-1) {
					this.tablero[i][j]=0;
				}
			}
			if(descuento==this.getFilas())
				columnaVacia=true;
		}
		return columnaVacia;
	}

	@Override
	public void moverCasillasIzquierda() throws IllegalArgumentException {
		int cantidadMover=0;
		int pos=0;
		boolean entra=false;
		boolean leyopos=false;
		for(int i=1; i<this.getColumnas(); ++i) {
			if(!entra) {
				if(!leyopos) {
					pos=i;
					leyopos=true;
				}
				if(this.tablero[this.getFilas()-1][i]==0) {
					cantidadMover++;
					if(i+1<this.getColumnas() && this.tablero[this.getFilas()-1][i+1]!=0 ) {
						entra=true;
					}
				}
			}
			
		}
		
		for(int i=0;i<this.getFilas();i++) {
			for(int j=pos;j<this.getColumnas()-1;j++) {
				for(int k=0;k<cantidadMover;k++) {
					this.tablero[i][j]=this.tablero[i][j+1];
				}
			}
		}
//		int posiMover=this.getColumnas()+1;
//		int casillasAmover=0;
//		boolean vacias=false;
//		boolean llenas= false;
//		for(int i =this.getFilas()-1;i>=0;i--) {
//			for(int j=0;j<this.getColumnas();j++) {
//				if(i==this.getFilas()-1) {
//					if(this.tablero[i][j]==0) {
//						if (llenas==false) {
//							vacias =true;
//							casillasAmover++;
//						}
//						
//						if(j<posiMover) {
//							
//							posiMover=j;
//						}
//					}	
//				}
//				else {
//				
//					if (vacias==true) {
//						llenas =true;
//					}
//				}
//				if(j>posiMover) {
//					//System.out.println("estooo: "+ (j-casillasAmover));
//					if(j-casillasAmover >0) {
//						this.tablero[i][j-casillasAmover]=this.tablero[i][j];
//						this.tablero[i][j]=0;
//					}
//					
//				}
//			}
//		}
//		
		
	}
	
	
	
	@Override
	public void efectuarJugada(int i, int j) throws IllegalArgumentException {
		
		this.eliminarCasillas(i, j, this.colorCasilla(i, j));
		
		if (this.bajarCasillas()) {
			this.moverCasillasIzquierda();
		}
		System.out.println("Ha sido eliminada");
		
	}
	
	public int efectuarJugada(Casilla jugada) throws IllegalArgumentException {
		int y=jugada.getColumna();
		int x=jugada.getFila();
		this.eliminarCasillas(y, x, this.colorCasilla(y, x));
		if (bajarCasillas()) {
			this.moverCasillasIzquierda();
		}
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
		return this.tablero[i][j];
	}

	@Override
	public int[][] coloresTablero() {
		// TODO Auto-generated method stub
		return null;
	}





}
