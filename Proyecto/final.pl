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

playa("Playa Juanillo", la_altagracia).
playa("Cabo Engaño", la_altagracia).
playa("Playa Cabeza de Toro", la_altagracia).

% macao, pero queda en punta_cana
playa("Playa Macao", la_altagracia).

/* Uvero Alto, tiene un parque pero tambien playa palmera,
 no encontre una playa llamada asi,
 pues supongo que es el mar, pero queda en punta canta.*/

playa("Playa Uvero Alto", la_altagracia).

% en bávaro, pero queda en punta cana, asi que puede ser: playa(X, punta_cana) :- playa(X, bavaro).
playa("Playa Bávaro", la_altagracia).
playa("Playa Arena Blanca", la_altagracia).
playa("Playa Arena Gorda", la_altagracia).

% en Bayahibe: https://enviajes.cl/republica-dominicana/bayahibe/playas-de-bayahibe/
playa("Playa de Bayahibe", la_altagracia).
playa("Playa Dominicus", la_altagracia).
playa("Playa Palmilla", la_altagracia).
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
playa("Playa Grande", maría_trinidad_sánchez).
playa("Playa Preciosa", maría_trinidad_sánchez).
playa("Playa Caleton", maría_trinidad_sánchez).
playa("Playa de los Minos", maría_trinidad_sánchez).
playa("Playa de los Muertos", maría_trinidad_sánchez).

% lugar\3 es la ciudad cercana, el nombre, y el tipo.
lugar(Provincia, Nombre):-playa(Nombre, Provincia).
lugar(la_vega, "La Vega").
lugar(santiago, "Santiago de los Caballeros").
lugar(santo_domingo, "Santo Domingo").
lugar(puerto_plata, "Puerto Plata").
lugar(santo_domingo, "Zona Colonial").

% weekday https://www.swi-prolog.org/pldoc/doc_for?object=day_of_the_week/2
weekday([],0):-!.
weekday(Fecha,Dia):- day_of_the_week(Fecha,Dia).


en_range_tiempo([],_,_) :- !.%esto es para prevenir un bug en la extracción de lugares.
en_range_tiempo(tiempo(HoraActual,MinActual),tiempo(HoraInicial,MinInicial),tiempo(HoraFinal,MinFinal)) :-
    ValorActual is HoraActual*60+MinActual,
    ValorInicial is HoraInicial*60+MinInicial,
    ValorFinal is HoraFinal*60+MinFinal,
    ValorInicial=<ValorActual,
    ValorActual=<ValorFinal, !.



% restaurantes\7: nombre, lugar\2, tipo, costo, fecha con formato de date(Ano, Mes, Dia), timpo, calificación.
restaurante("Little John at Juanillo Beach", lugar(la_altagracia,"Playa Juanillo"), caribeña, 2000, _, Tiempo, 5) :-
    en_range_tiempo(Tiempo,tiempo(11, 0),tiempo(21,0)).
restaurante("McDonald's", Lugar,comida_rápida, 400, _, Tiempo, 5):-
    en_range_tiempo(Tiempo,tiempo(7, 0),tiempo(22, 0)),
    member(Ciudad,["Santiago de los Caballeros","Santo Domingo","La Vega","Puerto Plata"]),
    lugar(Municipio, Ciudad),
    Lugar = lugar(Municipio, Ciudad).
restaurante("YALLA",lugar(puerto_plata, "Playa Cabarete"),española, 400,_,Tiempo,5) :-
    en_range_tiempo(Tiempo,tiempo(11,0),tiempo(22,0)).
restaurante("Aqua Restaurant",lugar(puerto_plata, "Playa Cabarete"),marisco, 550,_,Tiempo,5) :-
    en_range_tiempo(Tiempo,tiempo(8,0),tiempo(22,0)).
restaurante("Beach Side Italian Restaurant Cabarete",lugar(puerto_plata, "Playa Cabarete"),marisco, 2000,_,Tiempo,5) :-
    en_range_tiempo(Tiempo,tiempo(9,0),tiempo(22,0)).
restaurante("Front Loop Café and Grill",lugar(puerto_plata, "Playa Cabarete"),asador, 500,_,Tiempo, 5) :-
    en_range_tiempo(Tiempo,tiempo(7,30),tiempo(21,0)).
restaurante("La Casita de Papi",lugar(puerto_plata, "Playa Cabarete"),marisco, 1000,Fecha,Tiempo,5) :-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=2,
            en_range_tiempo(Tiempo,tiempo(13,0),tiempo(23,0))
        );
        (
            Dia>5 ,
            en_range_tiempo(Tiempo,tiempo(13,0),tiempo(21,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

restaurante("Restaurant Le Bistro",lugar(puerto_plata, "Playa Cabarete"),francesa, 1500,Fecha,Tiempo,5) :-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(12,0),tiempo(22,0))
        );
        (
            Dia=6,
            en_range_tiempo(Tiempo,tiempo(12,0),tiempo(21,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).





%------------Bares----------------

% bar\4: nombre, lugar\2, costo, calificacion

bar("Taringa Bar",lugar(santiago,"Santiago de los Caballeros"),1000,4,Fecha,Tiempo) :-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("Marraya Drink",lugar(santiago,"Santiago de los Caballeros"),2000,4,Fecha,Tiempo) :-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("Ahi-Bar",lugar(santiago,"Santiago de los Caballeros"),1000,5,Fecha,Tiempo) :-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("Bajarrando Bar",lugar(santiago,"Santiago de los Caballeros"),700,4,Fecha,Tiempo) :-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("La Posta Bar",lugar(santo_domingo,"Santo Domingo"),1200,5,Fecha,Tiempo):-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("Onno's Bar",lugar(santo_domingo,"Santo Domingo"),1500,4,Fecha,Tiempo):-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("Sabina Bar",lugar(santo_domingo,"Santo Domingo"),2000,4,Fecha,Tiempo):-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("Merengue Club",lugar(santo_domingo,"Santo Domingo"),1000,4,Fecha,Tiempo):-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("Cacique Bar",lugar(la_vega,"La Vega"),1300,4,Fecha,Tiempo):-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("Gabbana Bebidas",lugar(la_vega,"La Vega"),1300,3,Fecha,Tiempo):-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("Lite Lounge",lugar(la_vega,"La Vega"),1300,5,Fecha,Tiempo):-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

bar("6 Grados",lugar(la_vega,"La Vega"),1300,4,Fecha,Tiempo):-
    weekday(Fecha,Dia),
    (
        (
            Dia=<5,
            Dia>=1,
            en_range_tiempo(Tiempo,tiempo(15,0),tiempo(23,0))
        );
        (
            Dia>5,
            en_range_tiempo(Tiempo,tiempo(14,0),tiempo(23,0))
        );
        Dia = 0 %esto esta para poder coger todos los tipos de resturante
    ).

% actividad_cultural\4: nombre, lugar\2, tipo_actividad, costo
actividad_cultural("Centro Cultural Banreservas", lugar(santo_domingo,"Santo Domingo"), "Centro cultural", 0).
actividad_cultural("Centro Cultural de España", lugar(santo_domingo,"Santo Domingo"), "Centro cultural", 0).
actividad_cultural("Museo del Hombre Dominicano", lugar(santo_domingo,"Santo Domingo"), "Museo", 500).
actividad_cultural("Teatro Guloya", lugar(santo_domingo,"Santo Domingo"), "Obra de teatro", 700).

% actividad\7 es nombre, lugar\2, tipo, costo, fecha con formato de date(Ano, Mes, Dia), timpo, calificación.
% actividad(Nombre,Lugar,Tipo,Precio,Fecha,Tiempo,Calificacion).
actividad("El Carnaval Vegano",lugar(la_vega, "La Vega"),evento,0,date(_,2,27),_,5).