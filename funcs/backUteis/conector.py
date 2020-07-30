import sqlite3

class Conector:
    def conecta_Glac(self):
        self.conn = sqlite3.connect("glac.db")
        self.cursor = self.conn.cursor()
    def desconecta_Glac(self):
        self.conn.close()
    def montaTabelas(self):
        self.conecta_Glac()
        ### Cria tabela servprod
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS servprod (
                cod_sp INTEGER PRIMARY KEY,
                servprod CHAR(40) NOT NULL,
    			tiposerv CHAR(20),
    			sistemaserv CHAR(20),
    			id_marcaprod INTEGER,
    			id_fornec INTEGER,
                hor INTEGER(2,2),
                custo MONEY NOT NULL,
                valor MONEY NOT NULL,
    			sp CHAR(2) NOT NULL,
                descricao VARCHAR(200) NOT NULL

            );
        """)
        ### Automoveis
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS automoveis (
                cod_aut INTEGER PRIMARY KEY,
                automovel CHAR(40) NOT NULL,
                ano INTEGER NOT NULL,
    			marca CHAR NOT NULL


            );
        """)
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS fornecedores (
                cod_forn INTEGER PRIMARY KEY,
                fornecedor CHAR(20) NOT NULL,
    			fone SMALLINT NOT NULL,
    			cnpj SMALLINT NOT NULL,
                cep SMALLINT NOT NULL,
    			endereco CHAR(20) NOT NULL,
                municipio CHAR(15) NOT NULL,
                descricao VARCHAR(200) NOT NULL

            );
        """)
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS marcaprod (
                cod_marca INTEGER PRIMARY KEY,
                marca CHAR(20) NOT NULL,
    			descricao VARCHAR(200) NOT NULL

            );
        """)
        ###
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS orcamento1 (
    			id_orc1 INTEGER PRIMARY KEY,
    			cliente_orc NUMERIC(8) NOT NULL,
    			placa_orc VARCHAR(12) NOT NULL,
    			descp1 VARCHAR(120) NOT NULL,
    			descp2 VARCHAR(120) NOT NULL,
    			descp3 VARCHAR(120) NOT NULL,
    			dia NUMERIC(4) NOT NULL,
    			mes NUMERIC(4) NOT NULL,
    			ano NUMERIC(4) NOT NULL,
    			totalizador NUMERIC(8) NOT NULL
    			);
    	""")
        ###
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS orcamento2 (
    			cod_orc2 INTEGER PRIMARY KEY,
    			id_orc2 NUMERIC(10) NOT NULL,
    			cod_item NUMERIC(8) NOT NULL,
    			desc_item VARCHAR(120) NOT NULL,
    			valor NUMERIC(8) NOT NULL,
    			quant NUMERIC(8) NOT NULL,
    			total NUMERIC(8) NOT NULL
    			);
    	""")
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS empresa (
                cod_emp INTEGER PRIMARY KEY,
                nome_emp CHAR(40) NOT NULL,
                endereco_emp CHAR(40) NOT NULL,
                bairro_emp CHAR(20) NOT NULL,
                municipio_emp CHAR(20) NOT NULL,
                uf_emp CHAR(2) NOT NULL,
                fone_emp CHAR(12) NOT NULL,
                cep_emp CHAR(12) NOT NULL,
                cpf_emp CHAR(12) NOT NULL,
                rg_emp CHAR(10) NOT NULL,
                obs_emp CHAR(200) NOT NULL
            );
        """)
        ###
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS frota (
                id INTEGER PRIMARY KEY,
    			veiculo CHAR NOT NULL,
    			anoveic CHAR NOT NULL,
                placa CHAR NOT NULL,
    			renavan CHAR NOT NULL,
    			cliente CHAR NOT NULL,
    			combust CHAR NOT NULL,
    			motor CHAR NOT NULL,
    			cor CHAR NOT NULL


            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS itens_orc (
                cod_item INTEGER PRIMARY KEY,
                quant INTEGER,
    			valor INTEGER,
                item INTEGER

            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod_cli INTEGER PRIMARY KEY,
                nome CHAR(40) NOT NULL,
    			nascdia NUMERIC(2) NOT NULL,
    			nascmes NUMERIC(2) NOT NULL,
    			endereco CHAR(40) NOT NULL,
    			complemento CHAR(40) NOT NULL,
    			bairro CHAR(20) NOT NULL,
                municipio CHAR(20) NOT NULL,
    			cep NUMERIC(12) NOT NULL,
                uf CHAR(2) NOT NULL,
    			numcasa CHAR(20) NOT NULL,
                fone1ddd NUMERIC(2) NOT NULL,
    			fone1 NUMERIC(10) NOT NULL,
    			fone2ddd NUMERIC(2) NOT NULL,
    			fone2 NUMERIC(10) NOT NULL,
                cpf NUMERIC(12) NOT NULL,
                rg NUMERIC(10) NOT NULL,
    			email CHAR(40) NOT NULL,
                obs CHAR(200) NOT NULL,
    			nascano NUMERIC(4) NOT NULL

            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS codfalha (
                cod_falha CHAR(40) NOT NULL,
                falha CHAR(40) NOT NULL,
    			falha2 CHAR(20),
    			falha3 CHAR(20),
    			falha4 CHAR(20),
    			falha5 NUMERIC(20)

            );
        """)
        ####
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS orcfalha (
                id_orcfalha NUMERIC(10),
                cod_orcfalha VARCHAR(40),
                orcfalha CHAR(40),
    			orcfalha2 CHAR(200),
    			orcfalha3 CHAR(200),
    			orcfalha4 CHAR(200),
    			orcfalha5 NUMERIC(10)

            );
        """)
        ####
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS formapag (
    	    	id INTEGER PRIMARY KEY,
    			ordem CHAR NOT NULL,
    			tipopag CHAR NOT NULL,
    	        valorpagar CHAR NOT NULL,
    			valordeduzir CHAR NOT NULL,
    			dia CHAR NOT NULL,
    			mes CHAR NOT NULL,
    			ano CHAR NOT NULL,
    			pago CHAR NOT NULL,
    			fpag10 CHAR NULL,
    			fpag11 CHAR NULL

    	        );
    	    """)
        ####
        self.cursor.execute("""
    		CREATE TABLE IF NOT EXISTS meiopag (
    	    	id INTEGER PRIMARY KEY,
    			meiopag CHAR NOT NULL,
    			meiopag2 CHAR NOT NULL,
    	        meiopag3 CHAR NOT NULL,
    			meiopag4 CHAR NOT NULL

    	        );
    	    """)
        self.conn.commit()
        self.desconecta_Glac()