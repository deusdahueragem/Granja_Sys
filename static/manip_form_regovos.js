// Função para carregar os ovos registrados na tabela
function carregarOvosRegistrados() {
    // Realizar a requisição GET para a API (usando Fetch API)
    fetch('http://192.168.3.14/tb_ovos')
    .then(response => response.json())
    .then(data => {
        // Limpar a tabela para inserir os novos dados
        const tabelaOvos = document.getElementById('tabelaOvos');
        tabelaOvos.innerHTML = `
            <tr>
                <th>ID</th>
                <th>Data e Hora</th>
                <th>Quantidade</th>
                <th>Deletar</th>
            </tr>
        `;

        // Inserir os ovos registrados na tabela
        data.forEach(ovo => {
            const newRow = tabelaOvos.insertRow();
            newRow.innerHTML = `
                <td>${ovo.id_regovos}</td>
                <td>${ovo.dt_ovos}</td>
                <td>${ovo.qt_ovos}</td>
                <td><button onclick="deletarOvo(${ovo.id_regovos})">Deletar</button></td>
            `;
        });
    })
    .catch(error => console.error('Erro:', error));
}

// Carregar os ovos registrados na tabela ao carregar a página
carregarOvosRegistrados();

// Função para deletar um registro de ovo
function deletarOvo(id) {
    // Realizar a requisição DELETE para a API (usando Fetch API)
    fetch(`http://192.168.3.14/tb_ovos/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        // Carregar novamente os ovos registrados na tabela após deletar
        carregarOvosRegistrados();
    })
    .catch(error => console.error('Erro:', error));
}

// Evento de clique no botão "Registrar"
document.getElementById('btnRegistrar').addEventListener('click', function() {
    const quantidade = document.getElementById('qt_ovos').value;
    const dataHora = document.getElementById('dt_ovos').value;

    // Verifica se os campos estão vazios
    if (!quantidade || !dataHora) {
        // Pintar as bordas de vermelho
        if (!quantidade) {
            document.getElementById('qt_ovos').style.border = '2px solid red';
        }
        if (!dataHora) {
            document.getElementById('dt_ovos').style.border = '2px solid red';
        }

        // Mostrar mensagem de aviso
        alert('Preencha todos os campos para registrar as informações.');
        return; // Sai da função sem continuar o código
    }

    // Restaurar as bordas para o estado normal
    document.getElementById('qt_ovos').style.border = '1px solid #ccc';
    document.getElementById('dt_ovos').style.border = '1px solid #ccc';

    // Criação do objeto de dados para enviar ao servidor
    const dados = {
        "qt_ovos": quantidade,
        "dt_ovos": dataHora
    };

    // Restante do código para enviar os dados ao servidor
    fetch('http://192.168.3.14/tb_ovos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('qt_ovos').value = "";
        document.getElementById('dt_ovos').value = "";
        alert('O Registro foi realizado com sucesso !');
        // Inserir o novo registro na tabela de ovos registrados
        const tabelaOvos = document.getElementById('tabelaOvos');
        const newRow = tabelaOvos.insertRow();
        newRow.innerHTML = `
            <td>${data.id_regovos}</td>
            <td>${data.dt_ovos}</td>
            <td>${data.qt_ovos}</td>
            <td><button onclick="deletarOvo(${data.id_regovos})">Deletar</button></td>
        `;
    })
    .catch(error => console.error('Erro:', error));
});