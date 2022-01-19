create table public_teams (
    Name   varchar(120),
    Discipline    varchar(60),
    NOC     varchar(60),
    Event   varchar(100)
);


create table public_entries_gender(
Discipline varchar(60),
Female  int,
Male int,
Total   int
);


create table public_coaches(
    Name   varchar(120),
    Discipline    varchar(60),
    NOC     varchar(60),
    Event   varchar(100)
);

select pc.discipline, pc.noc from public_coaches pc
left join public_teams pt on pt.discipline=pc.discipline and pt.noc=pc.noc


select pc.discipline, pc.noc from public_coaches pc
cross join public_entries_gender



select * from public_entries_gender
select * from public_teams
