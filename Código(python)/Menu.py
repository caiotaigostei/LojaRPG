from bd import conectar, desconectar
import cliente
import vendedor
import transportadora
import produto
import vendas

def menu_clientes():
    while True:
        print("\n--- CLIENTES ---")
        print("1) Inserir cliente")
        print("2) Listar clientes")
        print("3) Buscar cliente por ID")
        print("4) Inserir cliente especial")
        print("5) Listar clientes especiais")
        print("6) Atualizar cashback de cliente especial")
        print("0) Voltar")
        op = input("Escolha: ").strip()

        try:
            if op == "1":
                _id = int(input("ID (ou 0 para automático): "))
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                sexo = input("Sexo (M/F/O): ")
                data = input("Data de nascimento (YYYY-MM-DD): ")
                if _id == 0:
                    _id = None
                cliente.inserir_cliente(_id, nome, idade, sexo, data)
            elif op == "2":
                cliente.listar_clientes()
            elif op == "3":
                _id = int(input("ID do cliente: "))
                cliente.buscar_cliente_por_id(_id)
            elif op == "4":
                cid = int(input("ID do cliente: "))
                cb = float(input("Cashback inicial: "))
                cliente.inserir_cliente_especial(cid, cb)
            elif op == "5":
                cliente.listar_clientes_especiais()
            elif op == "6":
                cid = int(input("ID do cliente: "))
                cb = float(input("Novo cashback: "))
                cliente.atualizar_cashback(cid, cb)
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"⚠️ Erro: {e}")

def menu_vendedores():
    while True:
        print("\n--- VENDEDORES ---")
        print("1) Inserir vendedor")
        print("2) Listar vendedores")
        print("3) Buscar vendedor por ID")
        print("0) Voltar")
        op = input("Escolha: ").strip()

        try:
            if op == "1":
                _id = int(input("ID (ou 0 para automático): "))
                nome = input("Nome: ")
                causa = input("Causa social: ")
                nota = float(input("Nota média: "))
                tipo = ""
                vendedor.inserir_vendedor(_id, nome, causa, tipo, nota)
            elif op == "2":
                vendedor.listar_vendedores()
            elif op == "3":
                _id = int(input("ID do vendedor: "))
                vendedor.buscar_vendedor_por_id(_id)
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"⚠️ Erro: {e}")

def menu_transportadoras():
    while True:
        print("\n--- TRANSPORTADORAS ---")
        print("1) Inserir transportadora")
        print("2) Listar transportadoras")
        print("3) Atualizar transportadora")
        print("4) Remover transportadora")
        print("0) Voltar")
        op = input("Escolha: ").strip()

        try:
            if op == "1":
                nome = input("Nome: ")
                cidade = input("Cidade: ")
                transportadora.inserir_transportadora(nome, cidade)
            elif op == "2":
                transportadora.listar_transportadoras()
            elif op == "3":
                _id = int(input("ID da transportadora: "))
                nome = input("Novo nome: ")
                cidade = input("Nova cidade: ")
                transportadora.atualizar_transportadora(_id, nome, cidade)
            elif op == "4":
                _id = int(input("ID da transportadora: "))
                transportadora.remover_transportadora(_id)
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"⚠️ Erro: {e}")

def menu_produtos():
    while True:
        print("\n--- PRODUTOS ---")
        print("1) Inserir produto")
        print("2) Listar produtos")
        print("3) Buscar produto por ID")
        print("4) Atualizar produto")
        print("5) Remover produto")
        print("6) Atualizar estoque")
        print("7) Listar produtos por vendedor")
        print("0) Voltar")
        op = input("Escolha: ").strip()

        try:
            if op == "1":
                nome = input("Nome: ")
                desc = input("Descrição: ")
                estq = int(input("Quantidade em estoque: "))
                val = float(input("Valor: "))
                obs = input("Observações: ")
                vend = int(input("ID do vendedor: "))
                produto.inserir_produto(nome, desc, estq, val, obs, vend)
            elif op == "2":
                produto.listar_produtos()
            elif op == "3":
                _id = int(input("ID do produto: "))
                produto.buscar_produto_por_id(_id)
            elif op == "4":
                _id = int(input("ID do produto: "))
                nome = input("Nome: ") or None
                desc = input("Descrição: ") or None
                estq = input("Estoque: "); estq = int(estq) if estq else None
                val = input("Valor: "); val = float(val) if val else None
                obs = input("Observações: ") or None
                vend = input("ID vendedor: "); vend = int(vend) if vend else None
                produto.atualizar_produto(_id, nome, desc, estq, val, obs, vend)
            elif op == "5":
                _id = int(input("ID do produto: "))
                produto.remover_produto(_id)
            elif op == "6":
                _id = int(input("ID do produto: "))
                estq = int(input("Nova quantidade: "))
                produto.atualizar_estoque(_id, estq)
            elif op == "7":
                vend = int(input("ID do vendedor: "))
                produto.listar_produtos_por_vendedor(vend)
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"⚠️ Erro: {e}")

def menu_vendas():
    while True:
        print("\n--- VENDAS ---")
        print("1) Criar venda")
        print("2) Listar vendas")
        print("3) Detalhes da venda")
        print("4) Remover venda")
        print("0) Voltar")
        op = input("Escolha: ").strip()

        try:
            if op == "1":
                cid = int(input("ID do cliente: "))
                tid = int(input("ID da transportadora: "))
                end = input("Endereço de destino: ")
                frete = float(input("Valor do frete: "))
                itens = []
                while True:
                    s = input("Produto ID (vazio para encerrar): ").strip()
                    if not s:
                        break
                    pid = int(s)
                    qtd = int(input("Quantidade: "))
                    itens.append((pid, qtd))
                vendas.criar_venda(cid, tid, end, frete, itens)
            elif op == "2":
                vendas.listar_vendas()
            elif op == "3":
                vid = int(input("ID da venda: "))
                vendas.detalhes_venda(vid)
            elif op == "4":
                vid = int(input("ID da venda: "))
                vendas.remover_venda(vid)
            elif op == "0":
                break
            else:
                print("Opção inválida.")
        except Exception as e:
            print(f"⚠️ Erro: {e}")

def main():
    try:
        conn = conectar()
        desconectar(conn)
    except Exception:
        print("⚠️ Aviso: conexão inicial falhou.")
    while True:
        print("\n=== SISTEMA E-COMMERCE (MENU PRINCIPAL) ===")
        print("1) Clientes")
        print("2) Vendedores")
        print("3) Transportadoras")
        print("4) Produtos")
        print("5) Vendas")
        print("0) Sair")
        op = input("Escolha: ").strip()
        if op == "1":
            menu_clientes()
        elif op == "2":
            menu_vendedores()
        elif op == "3":
            menu_transportadoras()
        elif op == "4":
            menu_produtos()
        elif op == "5":
            menu_vendas()
        elif op == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
