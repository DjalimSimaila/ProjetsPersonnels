id_dev = (SELECT id_dev FROM devices where token = {token})
id_user = (SELECT id_user FROM devices where token = {token})
liste_id_dev = SELECT DISTINCT id_dev FROM device where id_user = {id_user}

-- get latest
Select last_clip FROM users WHERE id_user = (SELECT id_user FROM devices where token = {token});
-- set latest

insert into clipboards(null, {id_dev}, {timestamp}, {value})
update users set last_clip = {last_clip} where id_user = {id_user}

SELECT * FROM clipboard      --         ( min date)                (max date)
WHERE id_dev in {liste_id_dev} AND timestamp > {min_date} AND timestamp < {max_date}
-- limite
ORDER BY id_dev



SELECT max(id_clip) FROM clipboard      --         ( min date)                (max date)
WHERE id_dev in {liste_id_dev}
