create database Cognitiva

CREATE table Alunos(
	 ra int identity(1800000,1) not null
	,nome varchar(50) not null
	,curso varchar(50) not null
	,turma varchar(5)

	constraint pk_raAlunos primary key (ra)
);

insert into alunos values ('WesleyChatãoooooooo','Banco de dados','4A')
('Wesley','Banco de dados','4A'), ('Guilherme','Banco de dados','4A'), ('Neri','Banco de dados','4A'),
('Henrique','Banco de dados','4A'),('Mayara','Banco de dados','4A');

CREATE TABLE sala (
	numero int

	constraint pk_SalaNumero primary key (numero)
);

insert into sala values (100),(101),(102),(103)

CREATE TABLE Chamada(
	 sala int
	,ra int
	,status varchar(50) default 'Falta'
	,data date default convert(date,getdate())
	
	constraint pk_salaChamada primary key (sala,ra),
 	constraint fk_raAluno foreign key (ra) references Alunos(ra)
);

insert into chamada (sala,ra,status)values (100,1800000,'Presente')

ALTER PROCEDURE VerificaPresenca
@ra int, @status varchar(50),@sala int
as
begin
	declare @data date = convert(date,getdate())
	if (select count(*) from Chamada) = (select count(*) from Alunos) and (select top 1 data from Chamada) = @data 
		GOTO siga
	else
	begin
		truncate table chamada
		insert into chamada (sala,ra)
		select
			 @sala
			,ra
		from
			alunos
	end
	siga:
		if (select status from chamada where ra = @ra) = @status and (select data from chamada where ra = @ra) = @data
			return
		else
		begin
			update chamada 
			set status = @status
			where ra = @ra
		end
end