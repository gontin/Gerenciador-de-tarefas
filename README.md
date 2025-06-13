# ✅ Gerenciador de Atividades no Terminal

Um programa simples em Python que permite ao usuário adicionar, remover, atualizar e listar atividades com prioridade e categoria. Ideal como projeto introdutório para prática de listas, dicionários e interações com o usuário no terminal.

---

## 📁 Estrutura do Projeto

```
gerenciador-atividades/
└── gerenciador.py
```

---

## ▶️ Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/gerenciador-atividades.git
cd gerenciador-atividades
```

2. Execute o programa:

```bash
python gerenciador.py
```

3. Siga o menu interativo para:

   * Adicionar nova atividade
   * Listar atividades por prioridade
   * Listar atividades por categoria
   * Atualizar atividade (marcar como feita)
   * Remover atividade
   * Fechar o programa

---

## 🧾 Exemplo de Atividade

Cada atividade é armazenada como:

```python
{
  "Nome": "Estudar Python",
  "Prioridade": 4,
  "Descrição": "Praticar estruturas de dados",
  "Categoria": "Estudos",
  "Feito": False
}
```

---

## 🧠 Conceitos Utilizados

* Listas e dicionários em Python
* Funções com parâmetros
* Filtros com `lambda`
* Manipulação de strings e entradas do usuário
* Estruturas condicionais e de repetição

---

## 🛠️ Melhorias Futuras

* Salvar dados em arquivo JSON para manter progresso
* Interface gráfica com Tkinter ou web com Flask
* Ordenação personalizada
* Suporte a múltiplos usuários

---

## 👤 Autor

**Gustavo Silveira Nicoletti**
Desenvolvedor Full Stack
[GitHub - gontin](https://github.com/gontin)

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usá-lo, modificá-lo e distribuí-lo.
