-- create temp table for parsing rubrics array
create table if not exists temptext (
  id bigint generated always as identity primary key,
  rubrics varchar,
  text varchar not null,
  created_date timestamp not null
);

-- create main table for texts
create table if not exists text (
  id bigint generated always as identity primary key,
  rubrics text[],
  text varchar not null,
  created_date timestamp not null
);

-- import csv file into a temp table 
copy temptext (text, created_date, rubrics)
from '/var/lib/postgresql/data/posts.csv'
delimiter ','
csv header;

-- json array to postgres array
create or replace function jsonb_array_to_text_array(p_input jsonb)
 RETURNS text[]
 LANGUAGE sql
 IMMUTABLE
AS $function$;

select array_agg(ary)::text[] from jsonb_array_elements_text(p_input) as ary;
$function$;

-- change format of json array and copy columsn in text table
insert into text (text, rubrics, created_date)
select text, jsonb_array_to_text_array(replace(rubrics, '''', '"')::jsonb) as rubrics,  created_date from temptext
order by id;

-- remove temp table:
drop table temptext;

