document.getElementById("vl_vendas").addEventListener("input", function() {
    var inputValue = this.value.replace(/\D/g, ''); // Remove caracteres não numéricos

    if (inputValue.length > 2) {
        inputValue = inputValue.replace(/^0+/, ''); // Remove zeros à esquerda após os dois primeiros dígitos
    }

    // Adiciona zeros à esquerda para garantir pelo menos dois dígitos para os centavos
    while (inputValue.length < 3) {
        inputValue = '0' + inputValue;
    }

    // Formata o valor para o formato desejado: R$ 000.000,00
    var formattedValue = "R$ " + inputValue.substring(0, inputValue.length - 2) + "." + inputValue.substring(inputValue.length - 2);

    this.value = formattedValue;
});

function formatCurrency(inputString) {
    var inputValue = inputString.replace(/[^\d.-]/g, ''); // Remover tudo exceto dígitos, ponto e hífen

    var parts = inputValue.split('.');
    var dollars = parts[0] || "0";
    var cents = parts[1];

    // Adicionar separador de milhar nos dólares
    var formattedDollars = "";
    for (var i = dollars.length - 1, count = 0; i >= 0; i--) {
        formattedDollars = dollars[i] + formattedDollars;
        count++;
        if (count === 3 && i !== 0) {
            formattedDollars = "." + formattedDollars;
            count = 0;
        }
    }

    if (!cents) {
        cents = "00";
    } else if (cents.length === 1) {
        cents = cents + "0";
    } else if (cents.length > 2) {
        cents = cents.substring(0, 2); // Limitar a 2 casas decimais
    }

    var formattedValue = "R$ " + formattedDollars + "," + cents;

    return formattedValue;
};







// Função para carregar as vendas registrados na tabela
function carregarvendasRegistrados() {
    // Realizar a requisição GET para a API (usando Fetch API)
    fetch('http://192.168.3.14/tb_vendas')
    .then(response => response.json())
    .then(data => {
        // Limpar a tabela para inserir as vendas dados
        const tabelavendas = document.getElementById('tabelavendas');
        tabelavendas.innerHTML = `
            <tr>
                <th>ID</th>
                <th>Data e Hora</th>
                <th>Valor</th>
                <th>Deletar</th>
            </tr>
        `;

        var qt_totalvendas = 0;
        // Inserir as vendas registrados na tabela
        data.forEach(venda => {
            const newRow = tabelavendas.insertRow();
            var valor_venda = venda.vl_vendas;
            valor_venda = valor_venda.toString();
            var valor_formatado = formatCurrency(valor_venda);
            //console.log("Valor recebido: " + valor_venda + " Valor formatado: " + valor_formatado);
            newRow.innerHTML = `
                <td>${venda.id_vendas}</td>
                <td>${venda.dt_vendas}</td>
                <td>${valor_formatado}</td>
                <td><button onclick="deletarvenda(${venda.id_vendas})">Deletar</button></td>
            `;
            qt_totalvendas = qt_totalvendas + venda.vl_vendas;
        });
        qt_totalvendas = qt_totalvendas.toString();
        qt_totalvendas = formatCurrency(qt_totalvendas);
        document.getElementById('qt_tvendas').textContent = qt_totalvendas;
    })
    .catch(error => console.error('Erro:', error));
}

// Carregar as vendas registrados na tabela ao carregar a página
carregarvendasRegistrados();

// Função para deletar um registro de venda
function deletarvenda(id) {
    // Realizar a requisição DELETE para a API (usando Fetch API)
    fetch(`http://192.168.3.14/tb_vendas/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        // Carregar novamente as vendas registrados na tabela após deletar
        carregarvendasRegistrados();
    })
    .catch(error => console.error('Erro:', error));
}

// Evento de clique no botão "Registrar"
document.getElementById('btnRegistrar').addEventListener('click', function() {
    var quantidade = document.getElementById('vl_vendas').value;
    quantidade = quantidade.replace("R$ ", "");
    quantidade = parseFloat(quantidade);
    const dataHora = document.getElementById('dt_vendas').value;

    // Verifica se os campos estão vazios
    if (!quantidade || !dataHora) {
        // Pintar as bordas de vermelho
        if (!quantidade) {
            document.getElementById('vl_vendas').style.border = '2px solid red';
        }
        if (!dataHora) {
            document.getElementById('dt_vendas').style.border = '2px solid red';
        }

        // Mostrar mensagem de aviso
        alert('Preencha todos os campos para registrar as informações.');
        return; // Sai da função sem continuar o código
    }

    // Restaurar as bordas para o estado normal
    document.getElementById('vl_vendas').style.border = '1px solid #ccc';
    document.getElementById('dt_vendas').style.border = '1px solid #ccc';

    // Criação do objeto de dados para enviar ao servidor
    const dados = {
        "vl_vendas": quantidade,
        "dt_vendas": dataHora
    };

    // Restante do código para enviar os dados ao servidor
    fetch('http://192.168.3.14/tb_vendas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('vl_vendas').value = "";
        document.getElementById('dt_vendas').value = "";
        alert('O Registro foi realizado com sucesso !');
        // Inserir o novo registro na tabela de vendas registrados
        const tabelavendas = document.getElementById('tabelavendas');
        const newRow = tabelavendas.insertRow();
        newRow.innerHTML = `
            <td>${data.id_vendas}</td>
            <td>${data.dt_vendas}</td>
            <td>${data.vl_vendas}</td>
            <td><button onclick="deletarvenda(${data.id_vendas})">Deletar</button></td>
        `;
    })
    .catch(error => console.error('Erro:', error));
});