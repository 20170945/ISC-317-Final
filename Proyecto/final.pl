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

minutos_en_total(tiempo(Hora,Minutos),Total) :- Total is Hora*60+Minutos.

en_range_tiempo([],_,_) :- !.%esto es para prevenir un bug en la extracción de lugares.
en_range_tiempo(Actual,Inicial,Final) :-
    minutos_en_total(Actual, ValorActual),
    minutos_en_total(Inicial, ValorInicial),
    minutos_en_total(Final, ValorFinal),
    ValorInicial=<ValorActual,
    ValorActual=<ValorFinal, !.

antes_de_tiempo(Antes,Despues):-
    minutos_en_total(Antes, ValorAntes),
    minutos_en_total(Despues, ValorDespues),
    ValorAntes =< ValorDespues.

horario_disponible(Actual, [H|_]) :-
    antes_de_tiempo(Actual,H),!.
horario_disponible(Actual, [_|T]) :- horario_disponible(Actual, T).

comparten([H|_],Otra):- member(H,Otra), !.
comparten([H|T],Otra):- comparten(T,Otra).


% cine y peliculas
cine("Cinema Boreal",lugar(santo_domingo, "Zona Colonial"), 4).
% cerrado : cine("Cine Lido",lugar(santo_domingo, "Zona Colonial"), 3).
% pelicula: pelicula\3 Titulo, calificacion y generos

cine_pelicula(cine("Cinema Boreal",lugar(santo_domingo, "Zona Colonial"), 4),Pelicula):-
    member(Pelicula, [
        pelicula("hola",500,3,[1,3,5],[tiempo(15,0),tiempo(17,0)],tiempo(2,0),[a]),
        pelicula("Zombie Ride",500,3,[1,3,5],[tiempo(15,0),tiempo(17,0)],tiempo(2,0),[terror])
    ]).


cine_pelicula(cine("The Colonial Gate 4D Cinema",lugar(santo_domingo, "Zona Colonial"), 5),Pelicula):-
    member(Pelicula, [
        pelicula("The Battle of Santo Domingo",500,3,[1,3,5],[tiempo(15,0),tiempo(17,0)],tiempo(1,50), [histórico]),
        pelicula("The Adventure of Ali Baba: JewelQuest",300,4,[2,4,6],[tiempo(14,0),tiempo(18,0)],tiempo(2,10),[aventura]),
        pelicula("The Great Wall of China",300,1,[1,3,5],[tiempo(14,0),tiempo(18,30)],tiempo(2,0),[aventura, oriental]),
        pelicula("Pirates 7D",600,5,[2,4,6],[tiempo(15,0),tiempo(19,0)],tiempo(2,30),[piratas, aventura]),
        pelicula("Toy Ride",700,3,[1,3,5],[tiempo(14,30),tiempo(17,45)],tiempo(2,0),[aventura]),
        pelicula("Planetarium",700,4,[2,4,6],[tiempo(15,15),tiempo(17,0)],tiempo(3,0),[ciencia_fricción]),
        pelicula("Dracula 4D",650,2,[1,3,5],[tiempo(2,30)],tiempo(4,0),[terror]),
        pelicula("Journey to the West",500,1,[2,4,6],[tiempo(11,0)],tiempo(1,52),[aventura]),
        pelicula("Asylum",400,5,[1,3,5],[tiempo(15,0),tiempo(17,0)],tiempo(2,5),[terror]),
        pelicula("Dino Adventure",650,4,[2,4,6],[tiempo(16,0)],tiempo(2,50),[aventura]),
        pelicula("Afterlife",500,3,[1,3,5],[tiempo(16,30)],tiempo(4,0),[horror]),
        pelicula("Zombie Ride",600,5,[2,4,6],[tiempo(14,0),tiempo(16,0)],tiempo(1,32),[terror]),
        pelicula("Alien Zoo",500,4,[1,3,5],[tiempo(14,0),tiempo(16,0)],tiempo(1,20),[ciencia_fricción]),
        pelicula("The Chase",200,2,[2,4,6],[tiempo(14,30),tiempo(16,30)],tiempo(1,11),[aventura]),
        pelicula("Sleigh Ride",400,3,[1,3,5],[tiempo(14,0),tiempo(16,0)],tiempo(1,23),[aventura, navideño])
    ]).

cines(L) :- setof(X,A^cine_pelicula(X,A),L).
cines(L, Lugar) :- setof(cine(A,Lugar,C),D^cine_pelicula(cine(A,Lugar,C),D),L).
generos_de_peliculas(L) :- setof(X,A^G^D^H^N^C^P^W^ (cine_pelicula(A,pelicula(N,P,C,W,H,D,G)),member(X,G)),L).

generos_de_cine(Cine,L) :- setof(X,G^N^C^D^H^P^W^ (cine_pelicula(Cine,pelicula(N,P,C,W,H,D,G)),member(X,G)),L).

peliculas_de_cine(Cine, Peliculas,Calificaciones, Presupuesto, Weekday, Hora, Generos) :-
    setof(
        pelicula(N,P,C,W,H,D,G),
        (
            cine_pelicula(Cine,pelicula(N,P,C,W,H,D,G)),
            comparten(G, Generos),
            horario_disponible(Hora, H),
            member(Weekday, W),
            member(C,Calificaciones),
            (
                Presupuesto = inf ;
                Presupuesto >= P
            )
        ),
        Peliculas
    ).

cines_disponibles(L, Lugar, Calificaciones, Presupuesto, Dia, Hora, TargetGeneros) :-
    setof(cine(A,Lugar,C), Generos^ (generos_de_cine(cine(A,Lugar,C),Generos), comparten(Generos,TargetGeneros)),Cines),
    weekday(Dia, Weekday),
    setof(Cine,A^B^ (member(Cine, Cines),peliculas_de_cine(Cine,[A|B], Calificaciones, Presupuesto, Weekday, Hora, TargetGeneros)),L).





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
tipos_de_restaurantes(L):-setof(X,A^B^C^D^E^restaurante(A,B,X,C,D,[],E),L).



%------------Bares----------------

% bar\4: nombre, lugar\2, costo, calificacion

bar("Taringa Bar",lugar(santiago,"Santiago de los Caballeros"),1000,4,Fecha,Tiempo) :-
    weekday(Fecha, Dia),
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
actividad("El Carnaval",lugar(_, _),evento,0,date(_,2,27),_,5).

tipos_de_otros(L):-setof(X,A^B^C^D^E^F^actividad(A,B,X,C,D,E,F),L).