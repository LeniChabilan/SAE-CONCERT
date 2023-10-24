delimiter |
CREATE or replace procedure materielALouer(concId int)
begin
    declare res varchar(5000) default '';
    declare matConcId int;
    declare nomMat varchar(50);
    declare fini boolean default false;
    declare matLouer cursor for 
        select materielId, nomMateriel from Materiel as mat
        natural join Necessiter natural join Concert
        where concertId = concId and mat.nomMateriel != (select nomMateriel from Materiel as mat natural join Necessiter natural join Concert natural join Salle natural join MaterielSalle as matS where mat.nomMateriel=matS.nomMaterielS and matS.disponible=true)
        and mat.nomMateriel != (select nomMateriel from Materiel as mat natural join Necessiter natural join Concert natural join Artiste natural join Utilise natural join MaterielArtiste as matA where mat.nomMateriel=matA.nomMaterielArt and matA.disponible=true) ;
    declare continue handler for not found set fini = true;

    open matLouer;
    while not fini do
        fetch matLouer into matConcId, nomMat;
        if not fini then
            set res=concat(res, matConcId, ' ', nomMat, ' ',', ');
        end if;
    end while;
    close matLouer;
    select res;
end |
delimiter ;
call materielALouer(5);