from models import TbOvos, TbGastos, TbVendas

def inserir_tb_ovos(dt_ovos, qt_ovos):
    ovo = TbOvos(dt_ovos=dt_ovos, qt_ovos=qt_ovos)
    ovo.save()

def consultar_tb_ovos_por_data(dt_ovos):
    ovo = TbOvos.query.filter_by(dt_ovos=dt_ovos).first()
    if ovo:
        print("Data do registro de ovos: " + str(ovo.dt_ovos) + "\nQuantidade de ovos: " + str(ovo.qt_ovos))
    else:
        print("Nenhum registro encontrado para a data especificada.")

def alterar_qt_ovos(dt_ovos, qt_ovos):
    ovo = TbOvos.query.filter_by(dt_ovos=dt_ovos).first()
    if ovo:
        ovo.qt_ovos = qt_ovos
        ovo.save()
    else:
        print("Nenhum registro encontrado para a data especificada.")

def inserir_tb_gastos(dt_gastos, qt_gastos, tp_gastos):
    gasto = TbGastos(dt_gastos=dt_gastos, qt_gastos=qt_gastos, tp_gastos=tp_gastos)
    gasto.save()

def consultar_tb_gastos_por_data(dt_gastos):
    gasto = TbGastos.query.filter_by(dt_gastos=dt_gastos).first()
    if gasto:
        print("Data do registro de gastos: " + str(gasto.dt_gastos) + "\nQuantidade de gastos: " + str(gasto.qt_gastos) + "\nTipo de gastos: " + gasto.tp_gastos)
    else:
        print("Nenhum registro encontrado para a data especificada.")

def alterar_gasto(dt_gastos, qt_gastos, tp_gastos):
    gasto = TbGastos.query.filter_by(dt_gastos=dt_gastos).first()
    if gasto:
        gasto.qt_gastos = qt_gastos
        gasto.tp_gastos = tp_gastos
        gasto.save()
    else:
        print("Nenhum registro encontrado para a data especificada.")

def inserir_tb_vendas(dt_vendas, vl_vendas):
    venda = TbVendas(dt_vendas=dt_vendas, vl_vendas=vl_vendas)
    venda.save()

def consultar_tb_vendas_por_data(dt_vendas):
    venda = TbVendas.query.filter_by(dt_vendas=dt_vendas).first()
    if venda:
        print("Data do registro de vendas: " + str(venda.dt_vendas) + "\nValor da venda: " + str(venda.vl_vendas))
    else:
        print("Nenhum registro encontrado para a data especificada.")

def alterar_venda(dt_vendas, vl_vendas):
    venda = TbVendas.query.filter_by(dt_vendas=dt_vendas).first()
    if venda:
        venda.vl_vendas = vl_vendas
        venda.save()
    else:
        print("Nenhum registro encontrado para a data especificada.")

def consultar_todos_tb_ovos():
    ovos = TbOvos.query.all()
    for ovo in ovos:
        print("\nData do registro de ovos: " + str(ovo.dt_ovos) + "\nQuantidade de ovos: " + str(ovo.qt_ovos))

def consultar_todos_tb_gastos():
    gastos = TbGastos.query.all()
    for gasto in gastos:
        print("\nData do registro de gastos: " + str(gasto.dt_gastos) + "\nQuantidade de gastos: " + str(gasto.qt_gastos) + "\nTipo de gastos: " + gasto.tp_gastos)

def consultar_todos_tb_vendas():
    vendas = TbVendas.query.all()
    for venda in vendas:
        print("\nData do registro de vendas: " + str(venda.dt_vendas) + "\nValor da venda: " + str(venda.vl_vendas))