from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from models import TbOvos, TbGastos, TbVendas
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class TbOvosResource(Resource):
    def get(self, id_regovos=None):
        if id_regovos:
            ovo = TbOvos.query.get(id_regovos)
            if ovo:
                return {
                    'id_regovos': ovo.id_regovos,
                    'dt_ovos': ovo.dt_ovos.isoformat(),
                    'qt_ovos': ovo.qt_ovos
                }
            return {'message': 'Registro de ovos não encontrado'}, 404
        else:
            ovos = TbOvos.query.all()
            return [
                {
                    'id_regovos': ovo.id_regovos,
                    'dt_ovos': ovo.dt_ovos.isoformat(),
                    'qt_ovos': ovo.qt_ovos
                }
                for ovo in ovos
            ]

    def post(self):
        data = request.get_json()
        dt_ovos_str = data.get('dt_ovos')
        qt_ovos = data.get('qt_ovos')
        if not dt_ovos_str or not qt_ovos:
            return {'message': 'Dados incompletos'}, 400
        
        # Convertendo a string da data para um objeto datetime
        try:
            dt_ovos = datetime.fromisoformat(dt_ovos_str)
        except ValueError:
            return {'message': 'Formato de data inválido. Utilize o formato ISO 8601 (YYYY-MM-DDTHH:mm:ss)'}, 400

        ovo = TbOvos(dt_ovos=dt_ovos, qt_ovos=qt_ovos)
        ovo.save()
        return {
            'id_regovos': ovo.id_regovos,
            'dt_ovos': ovo.dt_ovos.isoformat(),
            'qt_ovos': ovo.qt_ovos
        }, 201

    def put(self, id_regovos):
        data = request.get_json()
        dt_ovos_str = data.get('dt_ovos')
        qt_ovos = data.get('qt_ovos')
        if not dt_ovos_str or not qt_ovos:
            return {'message': 'Dados incompletos'}, 400
        
        # Convertendo a string da data para um objeto datetime
        try:
            dt_ovos = datetime.fromisoformat(dt_ovos_str)
        except ValueError:
            return {'message': 'Formato de data inválido. Utilize o formato ISO 8601 (YYYY-MM-DDTHH:mm:ss)'}, 400

        ovo = TbOvos.query.get(id_regovos)
        if not ovo:
            return {'message': 'Registro de ovos não encontrado'}, 404
        
        ovo.dt_ovos = dt_ovos
        ovo.qt_ovos = qt_ovos
        ovo.save()

        return {
            'id_regovos': ovo.id_regovos,
            'dt_ovos': ovo.dt_ovos.isoformat(),
            'qt_ovos': ovo.qt_ovos
        }

    def delete(self, id_regovos):
        ovo = TbOvos.query.get(id_regovos)
        if not ovo:
            return {'message': 'Registro de ovos não encontrado'}, 404
        ovo.delete()
        return {'message': 'Registro de ovos excluído com sucesso'}, 200

class TbGastosResource(Resource):
    def get(self, id_gastos=None):
        if id_gastos:
            gasto = TbGastos.query.get(id_gastos)
            if gasto:
                return {
                    'id_gastos': gasto.id_gastos,
                    'dt_gastos': gasto.dt_gastos.isoformat(),
                    'qt_gastos': gasto.qt_gastos,
                    'tp_gastos': gasto.tp_gastos
                }
            return {'message': 'Registro de gastos não encontrado'}, 404
        else:
            gastos = TbGastos.query.all()
            return [
                {
                    'id_gastos': gasto.id_gastos,
                    'dt_gastos': gasto.dt_gastos.isoformat(),
                    'qt_gastos': gasto.qt_gastos,
                    'tp_gastos': gasto.tp_gastos
                }
                for gasto in gastos
            ]

    def post(self):
        data = request.get_json()
        dt_gastos_str = data.get('dt_gastos')
        qt_gastos = data.get('qt_gastos')
        tp_gastos = data.get('tp_gastos')
        if not dt_gastos_str or not qt_gastos or not tp_gastos:
            return {'message': 'Dados incompletos'}, 400
        
        # Convertendo a string da data para um objeto datetime
        try:
            dt_gastos = datetime.fromisoformat(dt_gastos_str)
        except ValueError:
            return {'message': 'Formato de data inválido. Utilize o formato ISO 8601 (YYYY-MM-DDTHH:mm:ss)'}, 400

        gasto = TbGastos(dt_gastos=dt_gastos, qt_gastos=qt_gastos, tp_gastos=tp_gastos)
        gasto.save()
        return {
            'id_gastos': gasto.id_gastos,
            'dt_gastos': gasto.dt_gastos.isoformat(),
            'qt_gastos': gasto.qt_gastos,
            'tp_gastos': gasto.tp_gastos
        }, 201

    def put(self, id_gastos):
        data = request.get_json()
        dt_gastos_str = data.get('dt_gastos')
        qt_gastos = data.get('qt_gastos')
        tp_gastos = data.get('tp_gastos')
        if not dt_gastos_str or not qt_gastos or not tp_gastos:
            return {'message': 'Dados incompletos'}, 400
        
        # Convertendo a string da data para um objeto datetime
        try:
            dt_gastos = datetime.fromisoformat(dt_gastos_str)
        except ValueError:
            return {'message': 'Formato de data inválido. Utilize o formato ISO 8601 (YYYY-MM-DDTHH:mm:ss)'}, 400

        gasto = TbGastos.query.get(id_gastos)
        if not gasto:
            return {'message': 'Registro de gastos não encontrado'}, 404

        gasto.dt_gastos = dt_gastos
        gasto.qt_gastos = qt_gastos
        gasto.tp_gastos = tp_gastos
        gasto.save()

        return {
            'id_gastos': gasto.id_gastos,
            'dt_gastos': gasto.dt_gastos.isoformat(),
            'qt_gastos': gasto.qt_gastos,
            'tp_gastos': gasto.tp_gastos
        }

    def delete(self, id_gastos):
        gasto = TbGastos.query.get(id_gastos)
        if not gasto:
            return {'message': 'Registro de gastos não encontrado'}, 404
        gasto.delete()
        return {'message': 'Registro de gastos excluído com sucesso'}, 200

class TbVendasResource(Resource):
    def get(self, id_vendas=None):
        if id_vendas:
            venda = TbVendas.query.get(id_vendas)
            if venda:
                return {
                    'id_vendas': venda.id_vendas,
                    'dt_vendas': venda.dt_vendas.isoformat(),
                    'vl_vendas': venda.vl_vendas
                }
            return {'message': 'Registro de vendas não encontrado'}, 404
        else:
            vendas = TbVendas.query.all()
            return [
                {
                    'id_vendas': venda.id_vendas,
                    'dt_vendas': venda.dt_vendas.isoformat(),
                    'vl_vendas': venda.vl_vendas
                }
                for venda in vendas
            ]

    def post(self):
        data = request.get_json()
        dt_vendas_str = data.get('dt_vendas')
        vl_vendas = data.get('vl_vendas')
        if not dt_vendas_str or not vl_vendas:
            return {'message': 'Dados incompletos'}, 400
        
        # Convertendo a string da data para um objeto datetime
        try:
            dt_vendas = datetime.fromisoformat(dt_vendas_str)
        except ValueError:
            return {'message': 'Formato de data inválido. Utilize o formato ISO 8601 (YYYY-MM-DDTHH:mm:ss)'}, 400

        venda = TbVendas(dt_vendas=dt_vendas, vl_vendas=vl_vendas)
        venda.save()
        return {
            'id_vendas': venda.id_vendas,
            'dt_vendas': venda.dt_vendas.isoformat(),
            'vl_vendas': venda.vl_vendas
        }, 201

    def put(self, id_vendas):
        data = request.get_json()
        dt_vendas_str = data.get('dt_vendas')
        vl_vendas = data.get('vl_vendas')
        if not dt_vendas_str or not vl_vendas:
            return {'message': 'Dados incompletos'}, 400
        
        # Convertendo a string da data para um objeto datetime
        try:
            dt_vendas = datetime.fromisoformat(dt_vendas_str)
        except ValueError:
            return {'message': 'Formato de data inválido. Utilize o formato ISO 8601 (YYYY-MM-DDTHH:mm:ss)'}, 400

        venda = TbVendas.query.get(id_vendas)
        if not venda:
            return {'message': 'Registro de vendas não encontrado'}, 404

        venda.dt_vendas = dt_vendas
        venda.vl_vendas = vl_vendas
        venda.save()

        return {
            'id_vendas': venda.id_vendas,
            'dt_vendas': venda.dt_vendas.isoformat(),
            'vl_vendas': venda.vl_vendas
        }

    def delete(self, id_vendas):
        venda = TbVendas.query.get(id_vendas)
        if not venda:
            return {'message': 'Registro de vendas não encontrado'}, 404
        venda.delete()
        return {'message': 'Registro de vendas excluído com sucesso'}, 200

api.add_resource(TbOvosResource, '/tb_ovos', '/tb_ovos/<int:id_regovos>')
api.add_resource(TbGastosResource, '/tb_gastos', '/tb_gastos/<int:id_gastos>')
api.add_resource(TbVendasResource, '/tb_vendas', '/tb_vendas/<int:id_vendas>')

@app.route('/')
def index():
    return render_template('regovos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)