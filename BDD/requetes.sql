
-- procedure pour trouver le materiel que l'on doit louer, à tester
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


-- procedure pour ajouter un musicien au groupe
delimiter |
CREATE or replace PROCEDURE AjouterMusicienAuGroupe( mus_id INT,  grp_id INT,  ram BOOLEAN)
begin
    INSERT INTO MUSICIENADDITIONEL (musicienID, groupeId, ramene)
    VALUES (mus_id, grp_id, ram);
end |
delimiter ;

delimiter |
CREATE or replace function CalculerCapaciteTotaleLieu(lieu_id INT)
RETURNS INT
begin
    DECLARE capacite_totale INT;
    SELECT SUM(capaciteTotaleSalle) INTO capacite_totale
    FROM SALLE
    WHERE lieuID = lieu_id;
    RETURN capacite_totale;
end |
delimiter ;

delimiter |
CREATE or replace function MusicienDansGroupe(musicien_id INT, groupe_id INT)
RETURNS BOOLEAN
begin
    DECLARE musicien_count INT;
    SELECT COUNT(*) INTO musicien_count
    FROM MUSICIENADDITIONEL
    WHERE musicienID = musicien_id AND groupeId = groupe_id;
    IF musicien_count > 0 THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
end |
delimiter ;