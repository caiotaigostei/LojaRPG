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
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                sexo = input("Sexo (M/F/O): ")
                data = input("Data de nascimento (YYYY-MM-DD): ")
                cliente.inserir_cliente(nome, idade, sexo, data)
            elif op == "2":
                cliente.listar_clientes()
            elif op == "3":
                cid = int(input("ID do cliente: "))
                cliente.buscar_cliente_por_id(cid)
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
                nome = input("Nome: ")
                causa = input("Causa social: ")
                tipo = input("Tipo (comum/vip): ")
                nota = float(input("Nota média: "))
                cargo_id = int(input("ID do cargo: "))
                vendedor.inserir_vendedor(nome, causa, tipo, nota, cargo_id)
            elif op == "2":
                vends = vendedor.listar_vendedores()
                for v in vends:
                    print(f"ID:{v[0]} | Nome:{v[1]} | Tipo:{v[3]} | Nota:{v[4]} | Cargo:{v[5]}")
            elif op == "3":
                vid = int(input("ID do vendedor: "))
                v = vendedor.buscar_vendedor_por_id(vid)
                if v:
                    print(f"ID:{v[0]} | Nome:{v[1]} | Causa:{v[2]} | Tipo:{v[3]} | Nota:{v[4]} | Cargo:{v[5]}")
                else:
                    print("Vendedor não encontrado.")
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
                transp = transportadora.listar_transportadoras()
                for t in transp:
                    print(f"ID:{t[0]} | Nome:{t[1]} | Cidade:{t[2]}")
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

def main():
    while True:
        print("\n=== SISTEMA E-COMMERCE RPG ===")
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
            produto.menu_produtos()
        elif op == "5":
            vendas.menu_vendas()
        elif op == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
