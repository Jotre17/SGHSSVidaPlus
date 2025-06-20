-- SCRIPT USADO PARA CRIAÇÃO DO BANCO DE DADOS E DAS TABELAS. 

-- CRIA O BANCO DE DADOS.
CREATE DATABASE sghss;

-- SELECIONA O BANCO DE DADOS PARA USO.
USE sghss;

-- CRIACAO DAS TABELAS

-- Tabela unidade_saude
CREATE TABLE unidade_saude (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    tipo ENUM('Clínica', 'Hospital', 'Home Care', 'Laboratório') NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    cep VARCHAR(8) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    telefone VARCHAR(15) NOT NULL
);

-- Tabela paciente
CREATE TABLE paciente (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    unidade_saude_id BIGINT NOT NULL,
    nome VARCHAR(200) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    sexo ENUM ('Feminino','Masculino') NOT NULL,
    data_nascimento DATE NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    cep VARCHAR(8) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    email VARCHAR(100)
);

-- Tabela profissional
CREATE TABLE profissional (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    user_id BIGINT UNIQUE,
    unidade_saude_id BIGINT NOT NULL,
    nome VARCHAR(200) NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    crm_coren VARCHAR(20) NOT NULL
);

-- Tabela administrador
CREATE TABLE administrador (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    nome VARCHAR(200) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    permissao ENUM('Total', 'Parcial') NOT NULL
);

-- Tabela registro_acesso
CREATE TABLE registro_acesso (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    usuario_id BIGINT NOT NULL,
    data_hora DATETIME NOT NULL,
    acao TEXT NOT NULL,
    descricao TEXT
);

-- Tabela consulta
CREATE TABLE consulta (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    paciente_id BIGINT NOT NULL,
    profissional_id BIGINT NOT NULL,
    data_hora DATETIME NOT NULL,
    tipo ENUM('Online', 'Presencial') NOT NULL,
    status ENUM('Agendada', 'Realizada', 'Cancelada') NOT NULL
);

-- Tabela agendamento
CREATE TABLE agendamento (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    paciente_id BIGINT NOT NULL,
    profissional_id BIGINT NOT NULL,
    unidade_saude_id BIGINT NOT NULL,
    especialidade VARCHAR(100) NOT NULL,
    data_hora DATETIME NOT NULL,
    status ENUM('Agendado', 'Cancelado', 'Concluído') NOT NULL
);

-- Tabela prontuario
CREATE TABLE prontuario (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    paciente_id BIGINT NOT NULL,
    profissional_id BIGINT NOT NULL,
    data_registro DATETIME NOT NULL,
    descricao TEXT NOT NULL
);

-- Tabela prescricao
CREATE TABLE prescricao (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE ,
    prontuario_id BIGINT NOT NULL,
    medicamento VARCHAR(255) NOT NULL,
    dosagem VARCHAR(50) NOT NULL,
    instrucoes TEXT
);

-- Tabela leito
CREATE TABLE leito (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    unidade_saude_id BIGINT NOT NULL,
    profissional_id BIGINT NOT NULL,
    paciente_id BIGINT NOT NULL,
    tipoLeito ENUM('Enfermaria', 'UTI', 'Isolamento') NOT NULL,
    status ENUM('Disponível', 'Ocupado', 'Manutenção') NOT NULL
);

-- Tabela internacao
CREATE TABLE internacao (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    paciente_id BIGINT NOT NULL,
    profissional_id BIGINT NOT NULL,
    leito_id BIGINT NOT NULL,
    data_entrada DATETIME NOT NULL,
    data_saida DATETIME,
    diagnostico TEXT
);

-- Tabela suprimentos
CREATE TABLE suprimentos (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    unidade_saude_id BIGINT NOT NULL,
    nome VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    validade DATE NOT NULL
);

-- Tabela relatorio_financeiro
CREATE TABLE relatorio_financeiro (
    id BIGINT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    unidade_saude_id BIGINT NOT NULL,
    descricao TEXT,
    valor DECIMAL(10,2) NOT NULL,
    data_registro DATETIME NOT NULL
);

-- CRIAÇÃO DAS FKs DO BANCO DE DADOS.

ALTER TABLE paciente
    ADD CONSTRAINT fk_paciente_unidade FOREIGN KEY (unidade_saude_id) REFERENCES unidade_saude(id);

ALTER TABLE registro_acesso
    ADD CONSTRAINT fk_registroAcesso_administrador FOREIGN KEY (usuario_id) REFERENCES administrador(id);

ALTER TABLE profissional
	ADD CONSTRAINT fk_profissional_user FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE,
    ADD CONSTRAINT fk_profissional_unidade FOREIGN KEY (unidade_saude_id) REFERENCES unidade_saude(id) ON DELETE CASCADE;
    
ALTER TABLE consulta
    ADD CONSTRAINT fk_consulta_paciente FOREIGN KEY (paciente_id) REFERENCES paciente(id),
    ADD CONSTRAINT fk_consulta_profissional FOREIGN KEY (profissional_id) REFERENCES profissional(id);

ALTER TABLE agendamento
    ADD CONSTRAINT fk_agendamento_paciente FOREIGN KEY (paciente_id) REFERENCES paciente(id),
    ADD CONSTRAINT fk_agendamento_profissional FOREIGN KEY (profissional_id) REFERENCES profissional(id),
    ADD CONSTRAINT fk_agendamento_unidade FOREIGN KEY (unidade_saude_id) REFERENCES unidade_saude(id);

ALTER TABLE prontuario
    ADD CONSTRAINT fk_prontuario_paciente FOREIGN KEY (paciente_id) REFERENCES paciente(id),
    ADD CONSTRAINT fk_prontuario_profissional FOREIGN KEY (profissional_id) REFERENCES profissional(id);

ALTER TABLE prescricao
    ADD CONSTRAINT fk_prescricao_prontuario FOREIGN KEY (prontuario_id) REFERENCES prontuario(id);

ALTER TABLE leito
    ADD CONSTRAINT fk_leito_unidade FOREIGN KEY (unidade_saude_id) REFERENCES unidade_saude(id),
    ADD CONSTRAINT fk_leito_profissional FOREIGN KEY (profissional_id) REFERENCES profissional(id),
    ADD CONSTRAINT fk_leito_paciente FOREIGN KEY (paciente_id) REFERENCES paciente(id);

ALTER TABLE internacao
    ADD CONSTRAINT fk_internacao_paciente FOREIGN KEY (paciente_id) REFERENCES paciente(id),
    ADD CONSTRAINT fk_internacao_profissional FOREIGN KEY (profissional_id) REFERENCES profissional(id),
    ADD CONSTRAINT fk_internacao_leito FOREIGN KEY (leito_id) REFERENCES leito(id);

ALTER TABLE suprimentos
    ADD CONSTRAINT fk_suprimentos_unidade FOREIGN KEY (unidade_saude_id) REFERENCES unidade_saude(id);

ALTER TABLE relatorio_financeiro
    ADD CONSTRAINT fk_relatorio_unidade FOREIGN KEY (unidade_saude_id) REFERENCES unidade_saude(id);
	