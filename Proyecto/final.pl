:-encoding(utf8).
/* playas,
 predicado: playa(Nombre,Localización).
 samana https://viajarviviendo.com/playas-samana/
*/

playa("playa rincón",samana).
playa("playa frontón",samana).
playa("playa madama",samana).
playa("cayo levantado",samana).
playa("playa bonita",samana).
playa("la playita",samana).
playa("playa el portillo",samana).
playa("playa cosón",samana).
playa("playa las ballenas",samana).

% punta cana https://www.cataloniahotels.com/es/blog/mejores-playas-de-punta-cana-y-bavaro/

playa("playa juanillo", punta_cana).
playa("cabo engaño", punta_cana).
playa("playa cabeza de toro", punta_cana).

% macao, pero queda en punta_cana
playa("playa macao", macao).

/* Uvero Alto, tiene un parque pero tambien playa palmera,
 no encontre una playa llamada asi,
 pues supongo que es el mar, pero queda en punta canta.*/

playa("playa uvero alto", uvero_alto).

% en bávaro, pero queda en punta cana, asi que puede ser: playa(X, punta_cana) :- playa(X, bavaro).
playa("playa bávaro", bavaro).
playa("playa arena blanca", bavaro).
playa("playa arena gorda", bavaro).

% en Bayahibe: https://enviajes.cl/republica-dominicana/bayahibe/playas-de-bayahibe/
playa("playa de bayahibe", bayahibe).
playa("playa dominicus", bayahibe).
playa("playa palmilla", bayahibe).
playa("isla saona", bayahibe).
/* segun el articulo esta en bayahibe, pero en google maps
 esta en la romana, lo dejo aqui adentro.
 tambien La Romana queda fuera de higuey (donde esta bayahibe)
playa("playa minitas",romana).
playa("playa caleta",romana).
playa("isla catalina",romana).

Puerto Plata: https://www.senatorpuertoplatasparesort.com/es/playas-puerto-plata/
*/
playa("playa de maimón", puerto_plata).
playa("playa dorada", puerto_plata).
playa("playa cofresí", puerto_plata).
playa("playa sosúa", puerto_plata).
playa("playa cabarete", puerto_plata).
playa("playa punta rucia", puerto_plata).
playa("playa costambar", puerto_plata).
playa("playa cambiaso", puerto_plata).

/* Rio San Juan:
https://www.minube.com/tag/playas-rio-san-juan-c261554
https://www.visitarepublicadominicana.org/rio-san-juan
 */
playa("playa grande", rio_san_juan).
playa("playa preciosa", rio_san_juan).
playa("playa caleton", rio_san_juan).
playa("playa de los minos", rio_san_juan).
playa("playa de los muertos", rio_san_juan).


/* Caminos */
camino(samana, santo_domingo_este, 168).
camino(romana, santo_domingo_este, 112).
camino(santo_domingo, santo_domingo_este, 14).
camino(samana, romana, 238).
camino(samana, rio_san_juan, 127).
camino(romana, punta_cana, 78).
camino(romana, bayahibe, 26).
camino(punta_canta, bayahibe, 69).
camino(macao, bayahibe, 69).
camino(uvero_alto, bayahibe, 69).
camino(punta_canta, bavaro, 19).
camino(bavaro, macao, 13).
camino(samana, macao, 336).
camino(macao, uvero_alto, 10).
camino(puerto_plata, rio_san_juan, 89).
camino(puerto_plata, santiago, 60).
camino(romana, rio_san_juan, 263).
camino(rio_san_juan,santo_domingo_este,194).
camino(rio_san_juan,santiago , 106).
camino(santiago, la_vega, 38).
camino(santo_domingo, la_vega, 128).
