/*
    Importando el paquete Request
    cmd: npm install request
*/
const request = require('request');

// Autenticación
let subscription_key = '';
let end_point = '';

uriBase = end_point + 'vision/v3.1/analyze';

// Obtener imagen por enlace
const imgUrl = '';

// Parámetros de Request
const params = {
    'visualFeatures': 'Categories,Description,Color',
    'details': '',
    'language': 'es'
};

// Ingresando datos para Rquest
const options = {
    uri: uriBase,
    qs: params,
    body: '{ "url": ' + '"' + imgUrl + '" }',
    headers: {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
    }
};

// Ejecutando Request
request.post(
    options,
    (error, response, body) => {
        if (error) {
            console.log('JSON Response\n');
            return;
        }
        let jsonReponse = JSON.stringify(JSON.parse(body), null, '  ');
        console.log('JSON Reponse\n');
        console.log(jsonReponse);
    }
);