drop table gbook;

create table gbook (
	num int primary key auto_increment,
	title varchar(50) not null,
	author varchar(50) not null,
	email varchar(50) not null,
	content text,
	password varchar(20) not null,
	writeday date not null,
	readnum int
);

select * from GBOOK;
