:-encoding(utf8).
/* playas,
 predicado: playa(Nombre,Localización).
 samana https://viajarviviendo.com/playas-samana/
*/

playa("Playa Rincón",samana).
playa("Playa Frontón",samana).
playa("Playa Madama",samana).
playa("Cayo Levantado",samana).
playa("Punta Bonita",samana).
playa("La Playita",samana).
playa("Playa el Portillo",samana).
playa("Playa Cosón",samana).
playa("Playa las Ballenas",samana).

% punta cana https://www.cataloniahotels.com/es/blog/mejores-playas-de-punta-cana-y-bavaro/

playa("Playa Juanillo", punta_cana).
playa("Cabo Engaño", punta_cana).
playa("Playa Cabeza de Toro", punta_cana).

% macao, pero queda en punta_cana
playa("Playa Macao", macao).

/* Uvero Alto, tiene un parque pero tambien playa palmera,
 no encontre una playa llamada asi,
 pues supongo que es el mar, pero queda en punta canta.*/

playa("Playa Uvero Alto", uvero_alto).

% en bávaro, pero queda en punta cana, asi que puede ser: playa(X, punta_cana) :- playa(X, bavaro).
playa("Playa Bávaro", bavaro).
playa("Playa Arena Blanca", bavaro).
playa("Playa Arena Gorda", bavaro).

% en Bayahibe: https://enviajes.cl/republica-dominicana/bayahibe/playas-de-bayahibe/
playa("Playa de Bayahibe", bayahibe).
playa("Playa Dominicus", bayahibe).
playa("Playa Palmilla", bayahibe).
%playa("Isla Saona", bayahibe).
/* segun el articulo esta en bayahibe, pero en google maps
 esta en la romana, lo dejo aqui adentro.
 tambien La Romana queda fuera de higuey (donde esta bayahibe)
playa("Playa Minitas",romana).
playa("Playa Caleta",romana).
playa("Isla Catalina",romana).

Puerto Plata: https://www.senatorpuertoplatasparesort.com/es/playas-puerto-plata/
*/
playa("Playa de Maimón", puerto_plata).
playa("Playa Dorada", puerto_plata).
playa("Playa Cofresí", puerto_plata).
playa("Playa Sosúa", puerto_plata).
playa("Playa Cabarete", puerto_plata).
playa("Playa Punta Rucia", puerto_plata).
playa("Playa Costambar", puerto_plata).
playa("Playa Cambiaso", puerto_plata).

/* Rio San Juan:
https://www.minube.com/tag/playas-rio-san-juan-c261554
https://www.visitarepublicadominicana.org/rio-san-juan
 */
playa("Playa Grande", rio_san_juan).
playa("Playa Preciosa", rio_san_juan).
playa("Playa Caleton", rio_san_juan).
playa("Playa de los Minos", rio_san_juan).
playa("Playa de los Muertos", rio_san_juan).

% lugar\3 es la ciudad cercana, el nombre, y el tipo.
lugar(Ciudad, Nombre):-playa(Nombre, Ciudad).


% actividad\6 es nombre, lugar\2, tipo, costo, fecha con formato de date(Ano, Mes, Dia), calificación.
actividad("El carnaval",lugar(la_vega, "Ciudad"), celebración,0, date(_,2,27),5).
actividad("Little John at Juanillo Beach",lugar(punta_cana,"Playa Juanillo"),restaurante,2000,date(_,_,_),5).
actividad("McDonald's",lugar(Ciudad, "Ciudad"),restaurante,400,date(_,_,_),4):-
    member(Ciudad,[santiago,santo_domingo_de_este,santo_domingo,la_vega,puerto_plata]).