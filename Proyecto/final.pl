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


% actividad\5 es nombre, lugar, tipo, costo, fecha con formato de date(Ano, Mes, Dia).
actividad(X,Y, playa,0, date(_,_,_)):-playa(X,Y).
actividad("el carnaval",la_vega, celebración,0, date(_,2,27)).

/* grafo de las localizaciones */
:- dynamic arista/3.
arista(samana, santo_domingo_este, 168).
arista(romana, santo_domingo_este, 112).
arista(santo_domingo, santo_domingo_este, 14).
arista(samana, romana, 238).
arista(samana, rio_san_juan, 127).
arista(romana, punta_cana, 78).
arista(romana, bayahibe, 26).
arista(punta_cana, bayahibe, 69).
arista(macao, bayahibe, 69).
arista(uvero_alto, bayahibe, 69).
arista(punta_cana, bavaro, 19).
arista(bavaro, macao, 13).
arista(samana, macao, 336).
arista(macao, uvero_alto, 10).
arista(puerto_plata, rio_san_juan, 89).
arista(puerto_plata, santiago, 60).
arista(romana, rio_san_juan, 263).
arista(rio_san_juan,santo_domingo_este,194).
arista(rio_san_juan,santiago , 106).
arista(santiago, la_vega, 38).
arista(santo_domingo, la_vega, 128).
% definiendo la bidirecionaliodad de las arista, ya que es un grafo bidirecional
biarista(X,Y,D):-arista(X,Y,D);arista(Y,X,D).
% caminos compuestos, camino(Desde, Hasta, Camino, Peso)

showall([]).
showall([H|T]):-write(H),nl,showall(T).
